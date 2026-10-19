// Quiz.js - builds the end-of-form quiz: questions made from the player's own
// discoveries (in the chosen language) plus questions from the School MCQ Bank.
import { organismsOfTier, COMPONENTS, TROPHIC_LABEL } from './Database.js';
import { BANK } from './quizbank.js';
import { t, o, comp, dict } from './i18n.js';

const shuffle = (arr) => {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
};
const recipeText = (r) => r.map((id) => comp(id, 'name', COMPONENTS[id].name)).join(' + ');

// Look-alike questions (same first five words, or half their words shared; numbers ignored) are kept
// apart, also from the questions of the last few quizzes this session.
const sigOf = (text) => { const w = String(text).toLowerCase().match(/[\p{L}]+/gu) || []; return { set: new Set(w), head: w.slice(0, 5).join(' ') }; };
const alike = (a, b) => {
  if (a.head && a.head === b.head) return true;
  let both = 0;
  for (const x of a.set) if (b.set.has(x)) both++;
  const all = a.set.size + b.set.size - both;
  return all ? both / all >= 0.5 : false;
};
const recent = [];
function spreadOrder(items, text, limit = Infinity, win = 6) {
  const rest = shuffle(items).map((it) => ({ it, s: sigOf(text(it)) }));
  const out = [];
  while (rest.length && out.length < limit) {
    const last = recent.slice(-win);
    let k = rest.findIndex((r) => !last.some((l) => alike(r.s, l)));
    if (k < 0) k = 0;
    const [r] = rest.splice(k, 1);
    out.push(r.it);
    recent.push(r.s);
    if (recent.length > 30) recent.shift();
  }
  return out;
}

// One correct answer plus three different wrong ones, shuffled.
function options(correct, wrongPool) {
  const wrong = shuffle([...new Set(wrongPool.filter((w) => w && w !== correct))]).slice(0, 3);
  if (wrong.length < 3) return null;
  const opts = shuffle([correct, ...wrong]);
  return { opts, ans: opts.indexOf(correct) };
}

const MAKERS = {
  defence(org, all) {
    const r = options(recipeText(org.recipes[0]), all.filter((x) => x !== org).map((x) => recipeText(x.recipes[0])));
    return r && { q: t(org.role === 'mutualist' ? 'quiz.qPartner' : 'quiz.qDefence', { name: o(org, 'name') }), ...r, why: o(org, 'counter') };
  },
  energy(org) {
    const label = (k) => dict('trophic', k, TROPHIC_LABEL[k]);
    const r = options(label(org.trophic), Object.keys(TROPHIC_LABEL).filter((k) => k !== org.trophic).map(label));
    return r && { q: t('quiz.qEnergy', { name: o(org, 'name') }), ...r, why: o(org, 'energy') };
  },
  side(org, all) {
    const r = options(o(org, 'name'), all.filter((x) => x !== org).map((x) => o(x, 'name')));
    return r && { q: t('quiz.qSide'), quote: o(org, 'survival'), ...r, why: o(org, 'role_') };
  },
  science(org, all) {
    const r = options(o(org, 'science'), all.filter((x) => x !== org).map((x) => o(x, 'science')));
    return r && { q: t('quiz.qScience', { name: o(org, 'name') }), ...r, why: o(org, 'observed') };
  },
};

export function buildQuiz(scanned, tier, nGame = 3, nBank = 2) {
  const all = organismsOfTier(tier);
  const known = all.filter((x) => scanned.has(x.id));
  const pool = shuffle(known.length >= nGame ? known : all);
  const kinds = shuffle(Object.keys(MAKERS));
  const qs = [];
  for (let i = 0; i < pool.length && qs.length < nGame; i++) {
    const q = MAKERS[kinds[i % kinds.length]](pool[i], all);
    if (q) qs.push({ ...q, source: 'game' });
  }
  for (const b of spreadOrder(BANK[tier] || [], (x) => x.q, nBank)) {
    const r = options(b.opts[b.ans], b.opts.filter((_, i) => i !== b.ans));
    if (r) qs.push({ q: b.q, ...r, why: b.why, source: 'bank', cls: b.cls, topic: b.topic });
  }
  return spreadOrder(qs, (x) => x.q);
}
