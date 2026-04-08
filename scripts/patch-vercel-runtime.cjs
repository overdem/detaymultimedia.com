#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

function copyRecursive(src, dest) {
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }

  const files = fs.readdirSync(src);
  for (const file of files) {
    const srcPath = path.join(src, file);
    const destPath = path.join(dest, file);

    if (fs.statSync(srcPath).isDirectory()) {
      copyRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

try {
  // 1. Patch render function runtime to Node.js 20.x
  const configPath = path.join(process.cwd(), '.vercel/output/functions/render.func/.vc-config.json');
  if (fs.existsSync(configPath)) {
    const config = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
    config.runtime = 'nodejs20.x';
    fs.writeFileSync(configPath, JSON.stringify(config, null, '\t'));
    console.log('✓ Patched render function runtime to Node.js 20.x');
  }

  // 2. Copy API folder to .vercel/output/functions
  const apiSrcDir = path.join(process.cwd(), 'api');
  const functionsDir = path.join(process.cwd(), '.vercel/output/functions');

  if (fs.existsSync(apiSrcDir)) {
    // Copy entire api folder structure
    const apiDestDir = path.join(functionsDir, 'api');
    copyRecursive(apiSrcDir, apiDestDir);
    console.log('✓ Copied API folder to functions output');
  }
} catch (err) {
  console.error('✗ Error:', err.message);
  process.exit(1);
}
