// Checks every authored question works through the game's own quiz builder,
// and that the chapters found missing in the 28-Oct-2026 audit now have questions.
// Run: node tests/questions.test.mjs
import { readFileSync } from 'node:fs';
import { bankItems } from '../js/Quiz.js';

let fail = 0;
const check = (name, ok, info = '') => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${name}${info ? '  (' + info + ')' : ''}`); if (!ok) fail++; };
const load = (p) => JSON.parse(readFileSync(new URL(`../content/questions/${p}`, import.meta.url), 'utf8'));
const sci = [0, 1, 2, 3].flatMap((f) => load(`scientist/form-${f}.json`));
const ex = Array.from({ length: 10 }, (_, i) => load(`explorer/class-${i + 1}.json`)).flat();
const au = [...sci, ...ex].filter((q) => String(q.id).startsWith('au-'));

check('690 authored questions are in the packs', au.length === 690, String(au.length));
const built = bankItems(au, au.length);
check('every authored question builds into a 4-option quiz item', built.length === au.length, `${built.length}/${au.length}`);
check('the right answer is kept after shuffling', built.every((b) => { const src = au.find((q) => q.q === b.q); return src && b.opts[b.ans] === src.opts[src.ans]; }));

const has = (list, cls, topic) => list.some((q) => q.cls === cls && q.topic === topic);
const want = {
  12: ['Organisms and Populations', 'Ecosystem', 'Biodiversity and Conservation', 'Principles of Inheritance and Variation', 'Molecular Basis of Inheritance',
    'Biotechnology: Principles and Processes', 'Biotechnology and its Applications', 'Electrochemistry', 'Chemical Kinetics', 'The d- and f-Block Elements',
    'Haloalkanes and Haloarenes', 'Alcohols, Phenols and Ethers', 'Amines', 'Moving Charges and Magnetism', 'Magnetism and Matter', 'Alternating Current',
    'Dual Nature of Radiation and Matter', 'Atoms', 'Nuclei'],
  11: ['Biological Classification', 'Biomolecules', 'Breathing and Exchange of Gases', 'Body Fluids and Circulation', 'Excretory Products and their Elimination',
    'Locomotion and Movement', 'Neural Control and Coordination', 'Chemical Coordination and Integration', 'Some Basic Concepts of Chemistry',
    'Classification of Elements and Periodicity in Properties', 'Equilibrium', 'Units and Measurements', 'Mechanical Properties of Solids',
    'Mechanical Properties of Fluids', 'Thermal Properties of Matter', 'Thermodynamics', 'Kinetic Theory', 'Oscillations'],
};
for (const [cls, topics] of Object.entries(want)) {
  const missing = topics.filter((t) => !has(sci, Number(cls), t));
  check(`Class ${cls}: every chapter found missing now has questions`, !missing.length, missing.join(', '));
}
const exNeed = [[6, 'pollution'], [7, 'pollution'], [8, 'pollution'], [5, 'foodchain'], [6, 'foodchain'], [7, 'foodchain'], [9, 'biodiversity'], [10, 'biodiversity']];
for (const [cls, m] of exNeed) {
  const n = ex.filter((q) => q.cls === cls && q.m === m).length;
  check(`Explorer Class ${cls} ${m} has at least 15 questions`, n >= 15, String(n));
}
console.log(fail ? `\n${fail} check(s) failed` : '\nall checks passed');
process.exit(fail ? 1 : 0);
