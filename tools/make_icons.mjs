// App icons for Ecos-Synthetica from the emblem (js/app/emblem.js, ecosEmblem(false): no words).
// Headless Chrome renders the vector straight at each size (sharp at 32 / 180 / 192 / 512).
//   icons/icon-192.png, icon-512.png         emblem on transparent corners
//   icons/icon-maskable-512.png              full-bleed deep green, emblem at 80 % (Android safe zone)
//   icons/apple-touch-icon.png (180)         full-bleed deep green, emblem at 92 % (iOS has no transparency)
//   icons/favicon-32.png                     browser tab
// Run from the project folder:  node tools/make_icons.mjs
import { execFileSync } from 'node:child_process';
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '..');
const { ecosEmblem } = await import(pathToFileURL(join(root, 'js/app/emblem.js')).href);
const svg = ecosEmblem(false).trim();
const out = join(here, '.icons');
mkdirSync(out, { recursive: true });
mkdirSync(join(root, 'icons'), { recursive: true });
writeFileSync(join(out, 'emblem.svg'), svg);

const chrome = [
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
].find((p) => existsSync(p));
if (!chrome) throw new Error('Chrome / Edge not found');

function render(name, size, scale, background) {
  const inner = Math.round(size * scale);
  const html = `<!doctype html><html><head><style>
    html,body{margin:0;width:${size}px;height:${size}px;overflow:hidden;background:${background};}
    body{display:flex;align-items:center;justify-content:center;}
    svg{width:${inner}px;height:${inner}px;display:block;}
  </style></head><body>${svg}</body></html>`;
  const page = join(out, `${name}.html`);
  writeFileSync(page, html);
  const target = join(root, 'icons', `${name}.png`);
  execFileSync(chrome, [
    '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
    '--default-background-color=00000000', `--window-size=${size},${size}`, `--screenshot=${target}`,
    pathToFileURL(page).href,
  ], { stdio: 'ignore' });
  console.log('wrote', target);
}

const DEEP = 'radial-gradient(circle at 50% 30%, #1f5a52 0%, #0b2a2e 60%, #04121a 100%)';
render('icon-512', 512, 1, 'transparent');
render('icon-192', 192, 1, 'transparent');
render('favicon-32', 32, 1, 'transparent');
render('icon-maskable-512', 512, 0.8, DEEP);
render('apple-touch-icon', 180, 0.92, DEEP);
