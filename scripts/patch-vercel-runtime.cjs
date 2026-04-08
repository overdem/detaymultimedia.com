#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Path to the render function config
const configPath = path.join(process.cwd(), '.vercel/output/functions/render.func/.vc-config.json');

try {
  if (fs.existsSync(configPath)) {
    const config = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
    // Update Node.js runtime to 20.x
    config.runtime = 'nodejs20.x';
    fs.writeFileSync(configPath, JSON.stringify(config, null, '\t'));
    console.log('✓ Patched render function runtime to Node.js 20.x');
  } else {
    console.log('⚠ Render function config not found, skipping patch');
  }
} catch (err) {
  console.error('✗ Error patching runtime:', err.message);
  process.exit(1);
}
