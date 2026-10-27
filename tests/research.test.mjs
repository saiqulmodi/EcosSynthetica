// Checks Research mode maths and that students can reproduce published results.
// Run: node tests/research.test.mjs
import { readFileSync } from 'node:fs';
import { parseCSV, linreg, expfit, growth, diversity, t95, toCSV } from '../js/tiers/professional/research/stats.js';

let fail = 0;
const check = (name, ok, info = '') => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${name}${info ? '  (' + info + ')' : ''}`); if (!ok) fail++; };
const load = (f) => parseCSV(readFileSync(new URL(`../content/datasets/${f}`, import.meta.url), 'utf8'));

// Published result 1: Census of India 2011, decadal growth 2001-2011 = 17.7%.
{
  const { rows } = load('india_population_census.csv');
  const g = growth(rows.find((r) => r.year === 2001).population_millions, rows.find((r) => r.year === 2011).population_millions, 10);
  check('Census 2001-2011 decadal growth reproduces 17.7%', Math.abs(g.total * 100 - 17.7) < 0.05, (g.total * 100).toFixed(2) + '%');
  check('India population grew faster in 1961-71 than 2001-11', growth(439.2, 548.2, 10).total > g.total);
}
// Published result 2: NOAA Mauna Loa, CO2 rose about 2.4 ppm a year in 2010-2020.
{
  const { rows } = load('co2_mauna_loa.csv');
  const r = rows.filter((x) => x.year >= 2010 && x.year <= 2020);
  const lr = linreg(r.map((x) => x.year), r.map((x) => x.co2_ppm));
  check('CO2 trend 2010-2020 about 2.4 ppm per year', Math.abs(lr.b - 2.43) < 0.05, lr.b.toFixed(2));
  const all = linreg(rows.map((x) => x.year), rows.map((x) => x.co2_ppm));
  check('CO2 is accelerating: recent slope above the 1960-2023 average', lr.b > all.b, all.b.toFixed(2));
}
// Tigers: the 2006-2022 estimates fit exponential growth well.
{
  const { rows } = load('india_tigers_aite.csv');
  const f = expfit(rows.map((x) => x.year), rows.map((x) => x.tigers_mean));
  check('tiger numbers fit exponential growth (R² > 0.95)', f.r2 > 0.95, f.r2.toFixed(3));
  check('tiger growth about 6% a year', f.rate > 0.05 && f.rate < 0.075, (f.rate * 100).toFixed(1) + '%');
  const p = f.predict(2026);
  check('forecast has an uncertainty band around it', p.lo < p.y && p.y < p.hi);
}
// Regression basics
{
  const lr = linreg([1, 2, 3, 4], [3, 5, 7, 9]);
  check('perfect line: slope 2, intercept 1, R² 1', Math.abs(lr.b - 2) < 1e-12 && Math.abs(lr.a - 1) < 1e-12 && Math.abs(lr.r2 - 1) < 1e-12);
  check('t value for df 3 is 3.182', t95(3) === 3.182);
  check('CSV round trip', toCSV(['a', 'b'], [{ a: 1, b: 'x,y' }]) === 'a,b\n1,"x,y"');
}
// Diversity indices
{
  const even = diversity([10, 10, 10, 10]);
  check('4 equal species: Shannon = ln 4, Simpson = 0.75, evenness 1', Math.abs(even.shannon - Math.log(4)) < 1e-12 && Math.abs(even.simpson - 0.75) < 1e-12 && Math.abs(even.evenness - 1) < 1e-12);
  const one = diversity([40, 0, 0]);
  check('one species: Shannon 0, Simpson 0', one.shannon === 0 && one.simpson === 0);
  check('a dominated site is less diverse than an even one', diversity([85, 5, 5, 5]).shannon < even.shannon);
}

console.log(fail ? `\n${fail} check(s) failed` : '\nall checks passed');
process.exit(fail ? 1 : 0);
