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

// 690 until 08-Nov-2026; the 85 Class 1-7 ones were removed with the rest of the Class 1-7 Q/A.
// 604 since repeated questions were removed (one authored item repeated an older one).
check('604 authored questions are in the packs', au.length === 604, String(au.length));
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
const exNeed = [[8, 'pollution'], [9, 'biodiversity'], [10, 'biodiversity']];
for (const [cls, m] of exNeed) {
  const n = ex.filter((q) => q.cls === cls && q.m === m).length;
  check(`Explorer Class ${cls} ${m} has at least 15 questions`, n >= 15, String(n));
}
// Class 1-7 Q/A removed on 08-Nov-2026: the files stay (same code), but hold nothing.
check('Class 1-7 explorer packs are empty', ex.every((q) => q.cls >= 8) && [1, 2, 3, 4, 5, 6, 7].every((c) => !load(`explorer/class-${c}.json`).length));
check('scientist packs hold no Class 1-7 items', sci.every((q) => q.cls >= 8));

// Extra-Edge bank: Class 8-12 + NEET/MBBS, all subjects, no repeats.
const xeIndex = load('extraedge/index.json');
const xe = xeIndex.flatMap((f) => load(`extraedge/${f}`).map((q) => ({ ...q, file: f })));
check('Extra-Edge has the 6 class files', xeIndex.join() === 'class-8.json,class-9.json,class-10.json,class-11.json,class-12.json,neet-mbbs.json', xeIndex.join());
const xeBuilt = bankItems(xe, xe.length);
check('every Extra-Edge question builds into a 4-option quiz item', xeBuilt.length === xe.length && xe.every((q) => q.opts.length === 4 && new Set(q.opts).size === 4), `${xeBuilt.length}/${xe.length}`);
check('Extra-Edge right answers survive shuffling', xeBuilt.every((b) => { const src = xe.find((q) => q.q === b.q); return src && b.opts[b.ans] === src.opts[src.ans]; }));
const normQ = (s) => String(s).toLowerCase().replace(/[^a-z0-9]+/g, '');
check('no Extra-Edge question repeats inside the bank', new Set(xe.map((q) => normQ(q.q))).size === xe.length);
const others = new Set([...sci, ...ex, ...load('professional/index.json').flatMap((f) => load(`professional/${f}`))].map((q) => normQ(q.q)));
const clash = xe.filter((q) => others.has(normQ(q.q)));
check('no Extra-Edge question repeats another bank', !clash.length, clash.slice(0, 3).map((q) => q.q).join(' | '));
for (const f of xeIndex) {
  const subs = new Set(xe.filter((q) => q.file === f).map((q) => q.subject));
  const need = ['Physics', 'Chemistry', 'Biology', 'Botany'];
  check(`Extra-Edge ${f} covers ${need.join(', ')}`, need.every((s) => subs.has(s)), [...subs].join(', '));
}
console.log(fail ? `\n${fail} check(s) failed` : '\nall checks passed');
process.exit(fail ? 1 : 0);
