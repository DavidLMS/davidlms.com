#!/usr/bin/env node
const fs = require('fs/promises');
const path = require('path');

const ROOT_URL = 'https://davidlms.com';
const LANGS = ['es', 'en'];
const LIST_SIZE = 6;

function slugify(input) {
  return input
    .trim()
    .toLowerCase()
    .normalize('NFKC')
    .replace(/[^\p{L}\p{N}]+/gu, '-')
    .replace(/^-+|-+$/g, '')
    .replace(/-+/g, '-');
}

function stripQuotes(value) {
  if (!value) return value;
  const trimmed = value.trim();
  if ((trimmed.startsWith('"') && trimmed.endsWith('"')) || (trimmed.startsWith("'") && trimmed.endsWith("'"))) {
    return trimmed.slice(1, -1);
  }
  return trimmed;
}

function extractFrontMatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n?/);
  if (!match) {
    return { frontMatter: {}, body: content };
  }

  const raw = match[1];
  const body = content.slice(match[0].length);

  const titleMatch = raw.match(/^title:\s*(.+)$/m);
  const dateMatch = raw.match(/^date:\s*(.+)$/m);
  const draftMatch = raw.match(/^draft:\s*(.+)$/m);
  const descriptionMatch = raw.match(/^description:\s*(.+)$/m);
  const summaryMatch = raw.match(/^summary:\s*(.+)$/m);

  const title = titleMatch ? stripQuotes(titleMatch[1]) : undefined;
  const dateValue = dateMatch ? stripQuotes(dateMatch[1]) : undefined;
  const draftValue = draftMatch ? stripQuotes(draftMatch[1]) : undefined;
  const descriptionValue = descriptionMatch ? stripQuotes(descriptionMatch[1]) : undefined;
  const summaryValue = summaryMatch ? stripQuotes(summaryMatch[1]) : undefined;

  let date;
  if (dateValue) {
    const parsed = new Date(dateValue);
    if (!Number.isNaN(parsed.getTime())) {
      date = parsed;
    }
  }

  const draft = typeof draftValue === 'string' ? draftValue.toLowerCase() === 'true' : false;

  return {
    frontMatter: {
      title,
      dateValue,
      date,
      draft,
      description: descriptionValue,
      summary: summaryValue,
    },
    body,
  };
}

function cleanMarkdown(text) {
  return text
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/\*([^*]+)\*/g, '$1')
    .replace(/_([^_]+)_/g, '$1')
    .replace(/!\[[^\]]*]\([^)]*\)/g, '')
    .replace(/\[[^\]]*]\(([^)]*)\)/g, '$1')
    .replace(/<[^>]+>/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

function getFirstParagraph(body) {
  if (!body) return '';
  const paragraphs = body
    .split(/\n{2,}/)
    .map((p) => p.replace(/\n/g, ' ').trim())
    .filter(Boolean);

  const candidate = paragraphs.find((p) => !p.startsWith('![') && !p.startsWith('<figure'));
  return candidate || paragraphs[0] || '';
}

function truncate(text, maxLength = 200) {
  if (text.length <= maxLength) return text;
  const truncated = text.slice(0, maxLength - 1);
  const lastSpace = truncated.lastIndexOf(' ');
  if (lastSpace > maxLength * 0.6) {
    return `${truncated.slice(0, lastSpace)}…`;
  }
  return `${truncated}…`;
}

function deriveSummary({ description, summary }, body) {
  const source = description || summary || getFirstParagraph(body);
  const cleaned = cleanMarkdown(source || '');
  if (!cleaned) {
    return 'Sin resumen disponible.';
  }
  return truncate(cleaned, 200);
}

async function readMarkdown(filePath) {
  try {
    return await fs.readFile(filePath, 'utf8');
  } catch {
    return null;
  }
}

async function gatherEntries({ lang, section }) {
  const entries = [];
  const contentDir = path.resolve(__dirname, '..', 'site', 'content', lang, section);
  let dirEntries;
  try {
    dirEntries = await fs.readdir(contentDir, { withFileTypes: true });
  } catch {
    return entries;
  }

  for (const entry of dirEntries) {
    if (!entry.isDirectory()) continue;
    if (entry.name.startsWith('_')) continue;
    const dirPath = path.join(contentDir, entry.name);
    const indexPath = path.join(dirPath, 'index.md');
    const content = await readMarkdown(indexPath);
    if (!content) continue;

    const { frontMatter, body } = extractFrontMatter(content);
    const { title, date, dateValue, draft } = frontMatter;
    if (!title || !date || draft) continue;

    const slug = slugify(entry.name);
    const dateString = dateValue ? dateValue.slice(0, 10) : date.toISOString().slice(0, 10);
    const summary = deriveSummary(frontMatter, body);

    entries.push({ lang, section, title, date, slug, dateString, summary });
  }

  entries.sort((a, b) => b.date - a.date);
  return entries;
}

function buildUrl({ lang, section, slug }) {
  const langSegment = lang ? `/${lang}` : '';
  const sectionSegment = section === 'micro' ? '/micro' : '';
  const url = `${ROOT_URL}${langSegment}${sectionSegment}/${slug}.md`;
  return encodeURI(url);
}

function mergeTranslations(esEntries, enEntries) {
  const map = new Map();

  for (const entry of esEntries) {
    map.set(entry.slug, { es: entry });
  }

  for (const entry of enEntries) {
    const existing = map.get(entry.slug) || {};
    existing.en = entry;
    map.set(entry.slug, existing);
  }

  const merged = [];
  for (const value of map.values()) {
    const { es, en } = value;
    const preferred = en || es;
    if (!preferred) continue;
    const preferredDate = [en?.date, es?.date].filter(Boolean).sort((a, b) => b - a)[0];
    merged.push({ ...preferred, date: preferredDate || preferred.date });
  }

  merged.sort((a, b) => b.date - a.date);
  return merged;
}

function formatList(entries) {
  return entries.slice(0, LIST_SIZE).map((entry) => {
    const url = buildUrl({ lang: entry.lang, section: entry.section, slug: entry.slug });
    return `- [${entry.title}](${url})`;
  });
}

function formatFullList(entries) {
  return entries.map((entry) => {
    const url = buildUrl({ lang: entry.lang, section: entry.section, slug: entry.slug });
    const datePart = entry.dateString || entry.date.toISOString().slice(0, 10);
    const summary = entry.summary || 'Sin resumen disponible.';
    return `- ${datePart} — [${entry.title}](${url}): ${summary}`;
  });
}

function replaceSection(content, heading, lines) {
  const escapedHeading = heading.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const regex = new RegExp(`## ${escapedHeading}[\\s\\S]*?(?=\n## |$)`, 'u');
  const replacement = `## ${heading}\n\n${lines.join('\n')}\n\n`;
  if (!regex.test(content)) {
    throw new Error(`Heading "${heading}" not found while updating llms files.`);
  }
  return content.replace(regex, replacement);
}

async function updateFile(filePath, updates) {
  const original = await fs.readFile(filePath, 'utf8');
  let updated = original;
  for (const { heading, lines } of updates) {
    updated = replaceSection(updated, heading, lines);
  }
  if (updated !== original) {
    await fs.writeFile(filePath, updated, 'utf8');
  }
}

async function main() {
  const postsByLang = {};
  const microByLang = {};

  for (const lang of LANGS) {
    postsByLang[lang] = await gatherEntries({ lang, section: 'posts' });
    microByLang[lang] = await gatherEntries({ lang, section: 'micro' });
  }

  const combinedPosts = mergeTranslations(postsByLang.es, postsByLang.en);
  const combinedMicro = mergeTranslations(microByLang.es, microByLang.en);

  const bilingualUpdates = [
    {
      heading: 'Recent Posts',
      lines: formatList(combinedPosts),
    },
    {
      heading: 'Recent Microblog',
      lines: formatList(combinedMicro),
    },
  ];

  const esUpdates = [
    {
      heading: 'Artículos Recientes',
      lines: formatList(postsByLang.es),
    },
    {
      heading: 'Microblog Reciente',
      lines: formatList(microByLang.es),
    },
  ];

  const esFullUpdates = [
    {
      heading: 'Artículos',
      lines: formatFullList(postsByLang.es),
    },
    {
      heading: 'Microblog',
      lines: formatFullList(microByLang.es),
    },
  ];

  const enUpdates = [
    {
      heading: 'Recent Posts',
      lines: formatList(postsByLang.en),
    },
    {
      heading: 'Recent Microblog',
      lines: formatList(microByLang.en),
    },
  ];

  await updateFile(path.resolve(__dirname, '..', 'site', 'static', 'llms.md'), bilingualUpdates);
  await updateFile(path.resolve(__dirname, '..', 'site', 'static', 'es', 'llms.md'), esUpdates);
  await updateFile(path.resolve(__dirname, '..', 'site', 'static', 'en', 'llms.md'), enUpdates);
  await updateFile(path.resolve(__dirname, '..', 'site', 'static', 'es', 'llms-full.md'), esFullUpdates);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
