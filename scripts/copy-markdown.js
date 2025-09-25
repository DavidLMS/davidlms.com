#!/usr/bin/env node
const fs = require('fs/promises');
const path = require('path');

const languages = ['es', 'en'];
const txtVariants = [
  { slug: 'llms', lang: null },
  { slug: 'llms-full', lang: null },
  { slug: 'llms', lang: 'es' },
  { slug: 'llms-full', lang: 'es' },
  { slug: 'llms', lang: 'en' },
  { slug: 'llms-full', lang: 'en' },
];

async function exists(filePath) {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
}

async function copyIndexFiles(currentDir, baseDir) {
  const entries = await fs.readdir(currentDir, { withFileTypes: true });

  for (const entry of entries) {
    if (!entry.isDirectory()) continue;

    const dirPath = path.join(currentDir, entry.name);
    await copyIndexFiles(dirPath, baseDir);

    const indexPath = path.join(dirPath, 'index.md');
    if (!(await exists(indexPath))) continue;

    const relative = path.relative(baseDir, dirPath);
    if (!relative) continue;

    const targetPath = path.join(baseDir, `${relative}.md`);
    await fs.mkdir(path.dirname(targetPath), { recursive: true });
    await fs.copyFile(indexPath, targetPath);
  }
}

async function copyTxtFiles(distDir) {
  for (const { slug, lang } of txtVariants) {
    const baseDir = lang ? path.join(distDir, lang) : distDir;
    const source = path.join(baseDir, `${slug}.md`);
    const target = path.join(baseDir, `${slug}.txt`);

    if (await exists(source)) {
      await fs.mkdir(path.dirname(target), { recursive: true });
      await fs.copyFile(source, target);
    }
  }
}

async function main() {
  const distDir = path.resolve(__dirname, '..', 'dist');
  if (!(await exists(distDir))) {
    console.error('No dist directory found. Run `npm run build` first.');
    process.exit(1);
  }

  for (const lang of languages) {
    const langDir = path.join(distDir, lang);
    if (await exists(langDir)) {
      await copyIndexFiles(langDir, langDir);
    }
  }

  await copyTxtFiles(distDir);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
