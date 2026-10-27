// main.js - boots the path screen; each tier is loaded only when it is chosen.
import { Shell } from './app/Shell.js';
import { saveKeyFor } from './app/Profile.js';

const $ = (id) => document.getElementById(id);

// Eco Scientist: the original game (4 forms, Lab, Codex, evolve quiz).
async function startScientist(profile) {
  const [{ Game, setSaveKey }, { UI }, { Sound }, { loadBank }] = await Promise.all([
    import('./GameLoop.js'), import('./UI.js'), import('./Sound.js'), import('./Quiz.js'),
  ]);
  setSaveKey(saveKeyFor(profile));
  const sound = new Sound();
  const ui = new UI(sound);
  try {
    const game = new Game($('stage'), ui, sound);
    ui.bind(game);
    window.ecos = game; // handy for testing from the browser console
    window.ecosUI = ui;
    loadBank(game.tier);
    for (const fn of scientistAddOns) await fn(game, ui, profile);
  } catch (err) {
    console.error(err);
    $('fatal').hidden = false;
  }
}

// Later modules add to the Scientist game (dashboard, journal, experiments, tutor).
export const scientistAddOns = [];
scientistAddOns.push((game, ui, profile) => import('./tiers/scientist/AddOns.js').then((m) => m.mount(game, ui, profile)));

const tiers = {
  explorer: { available: true, start: (p) => import('./tiers/explorer/ExplorerGame.js').then((m) => m.start(p)) },
  scientist: { available: true, start: startScientist },
  professional: { available: true, total: 3, start: (p) => import('./tiers/professional/ProfessionalGame.js').then((m) => m.start(p)) },
};

const shell = new Shell(tiers);
window.ecosApp = { shell, tiers, scientistAddOns };
shell.show();

// Offline play: cache what has been opened (only on http/https pages).
if ('serviceWorker' in navigator && /^https?:$/.test(location.protocol)) {
  window.addEventListener('load', () => { navigator.serviceWorker.register('sw.js').catch(() => {}); });
}
