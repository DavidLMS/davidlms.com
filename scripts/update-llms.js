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
  if (!content.startsWith('---')) return {};
  const end = content.indexOf('\n---', 3);
  if (end === -1) return {};
  const frontMatter = content.slice(3, end).trim();

  const titleMatch = frontMatter.match(/^title:\s*(.+)$/m);
  const dateMatch = frontMatter.match(/^date:\s*(.+)$/m);
  const draftMatch = frontMatter.match(/^draft:\s*(.+)$/m);

  const title = titleMatch ? stripQuotes(titleMatch[1]) : undefined;
  const dateValue = dateMatch ? stripQuotes(dateMatch[1]) : undefined;
  const draftValue = draftMatch ? stripQuotes(draftMatch[1]) : undefined;

  let date;
  if (dateValue) {
    const parsed = new Date(dateValue);
    if (!Number.isNaN(parsed.getTime())) {
      date = parsed;
    }
  }

  const draft = typeof draftValue === 'string' ? draftValue.toLowerCase() === 'true' : false;

  return { title, date, draft };
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

    const { title, date, draft } = extractFrontMatter(content);
    if (!title || !date || draft) continue;

    const slug = slugify(entry.name);
    entries.push({ lang, title, date, slug });
  }

  entries.sort((a, b) => b.date - a.date);
  return entries;
}

function buildUrl({ lang, type, slug }) {
  const langSegment = lang ? `/${lang}` : '';
  const section = type === 'post' ? 'posts' : 'micro';
  const url = `${ROOT_URL}${langSegment}/${section}/${slug}.md`;
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

function formatList(entries, type) {
  return entries.slice(0, LIST_SIZE).map((entry) => {
    const url = buildUrl({ lang: entry.lang, type, slug: entry.slug });
    return `- [${entry.title}](${url})`;
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
      lines: formatList(combinedPosts, 'post'),
    },
    {
      heading: 'Recent Microblog',
      lines: formatList(combinedMicro, 'micro'),
    },
  ];

  const esUpdates = [
    {
      heading: 'Artículos Recientes',
      lines: formatList(postsByLang.es, 'post'),
    },
    {
      heading: 'Microblog Reciente',
      lines: formatList(microByLang.es, 'micro'),
    },
  ];

  const enUpdates = [
    {
      heading: 'Recent Posts',
      lines: formatList(postsByLang.en, 'post'),
    },
    {
      heading: 'Recent Microblog',
      lines: formatList(microByLang.en, 'micro'),
    },
  ];

  await updateFile(path.resolve(__dirname, '..', 'site', 'static', 'llms.md'), bilingualUpdates);
  await updateFile(path.resolve(__dirname, '..', 'site', 'static', 'es', 'llms.md'), esUpdates);
  await updateFile(path.resolve(__dirname, '..', 'site', 'static', 'en', 'llms.md'), enUpdates);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
