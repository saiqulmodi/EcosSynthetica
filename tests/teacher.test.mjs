// Checks the report card and the teacher's class table with 30 students.
// Run: node tests/teacher.test.mjs
import { buildPayload, makeReport, readReport, classTable, toCSV, unlockCode, checkUnlock, EXPLORER } from '../js/teacher/report.js';

let fail = 0;
const check = (name, ok, info = '') => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${name}${info ? '  (' + info + ')' : ''}`); if (!ok) fail++; };

const names = ['Aarav', 'Diya', 'Ishaan', 'Meera', 'Kabir', 'Ananya', 'Rohan', 'Saanvi', 'Vihaan', 'Aditi', 'Arjun', 'Kavya', 'Reyansh', 'Myra', 'Sai', 'Anika', 'Dev', 'Tara', 'Yash', 'Riya',
  'Ayaan', 'Nisha', 'Om', 'Pari', 'Rudra', 'Sneha', 'Tanvi', 'Uday', 'Veda', 'রাহুল'];
const files = [];
for (let i = 0; i < 30; i++) {
  const modules = {};
  EXPLORER.slice(0, (i % 7) + 1).forEach((id, k) => { modules[id] = { status: 'done', stars: (k % 3) + 1 }; });
  const pr = { modules, seeds: i * 3, trees: i, badges: { a: 1 }, cases: i % 5 === 0 ? { dengue: { status: 'done', stars: 2, impact: 10 } } : {}, journal: [] };
  const rep = await makeReport(buildPayload({ name: names[i], cls: 7, classCode: '7b-green' }, pr, i % 2 ? { tier: 2, completed: false } : null));
  files.push(JSON.stringify(rep));
}
const read = await Promise.all(files.map(readReport));
check('all 30 report files verify', read.every((r) => r.ok));
const table = classTable(read.map((r) => r.report), '7B-GREEN');
check('class table has 30 students', table.rows.length === 30, String(table.rows.length));
check('trees add up (0+1+...+29 = 435)', table.totals.trees === 435, String(table.totals.trees));
check('students who finished all 7 Explorer modules', table.totals.explorerDone === 4, String(table.totals.explorerDone));
check('a case column appears', table.caseIds.includes('dengue'));
const csv = toCSV(table);
check('CSV has a header and 30 rows', csv.split('\n').length === 31);

const changed = JSON.parse(files[0]); changed.trees = 999;
check('a hand-edited file is rejected', (await readReport(JSON.stringify(changed))).error === 'check');
check('a random file is rejected', (await readReport('{"hello": 1}')).error === 'format');
check('other class codes are filtered out', classTable(read.map((r) => r.report), '8A').rows.length === 0);
const twice = [...read.map((r) => r.report), { ...read[0].report, at: '2099-01-01', trees: 50 }];
check('a student who sends twice counts once (latest)', classTable(twice, '7B-GREEN').rows.length === 30);

const code = await unlockCode('7B-GREEN', 'professional');
check('unlock code is 6 characters', /^[0-9A-F]{6}$/.test(code), code);
check('unlock code opens the right tier for that class', (await checkUnlock('7b-green', code)) === 'professional');
check('unlock code does not work for another class', (await checkUnlock('8A', code)) === null);
check('report card is small enough for a QR code', Math.max(...files.map((f) => new TextEncoder().encode(f).length)) < 1200, Math.max(...files.map((f) => f.length)) + ' bytes');

console.log(fail ? `\n${fail} check(s) failed` : '\nall checks passed');
process.exit(fail ? 1 : 0);
