// Checks the Eco Professional case models (Health track).
// Run: node tests/professional.test.mjs
import { dengue, dengueR0, DENGUE, subIndex, aqiOf, bandOf, air, BIS, water, problemsOf } from '../js/tiers/professional/health/models.js';

let fail = 0;
const check = (name, ok, info = '') => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${name}${info ? '  (' + info + ')' : ''}`); if (!ok) fail++; };

// Dengue
{
  const R0 = dengueR0(DENGUE);
  check('dengue R0 in the published 2-5 range', R0 > 2 && R0 < 5, R0.toFixed(2));
  const none = dengue({});
  const all = dengue({ source: 0.55, fog: true, protect: 0.35, care: true });
  check('unchecked outbreak infects a large share of the ward', none.cases > DENGUE.N * 0.25, String(none.cases));
  check('cases never exceed the population', none.cases <= DENGUE.N);
  check('combined response cuts cases by more than half', all.cases < none.cases * 0.5, `${all.cases} vs ${none.cases}`);
  const fogOnly = dengue({ fog: true });
  const srcOnly = dengue({ source: 0.55 });
  check('source reduction beats fogging alone', srcOnly.cases < fogOnly.cases, `${srcOnly.cases} vs ${fogOnly.cases}`);
  check('early care lowers deaths for the same cases', dengue({ care: true }).deaths < none.deaths);
  // Threshold: below R0 = 1 the outbreak dies out.
  const low = dengue({}, { ...DENGUE, m: 0.4 });
  check('below threshold (R0 < 1) the outbreak fizzles', dengueR0({ ...DENGUE, m: 0.4 }) < 1 && low.cases < 50, String(low.cases));
}

// CPCB AQI breakpoints
{
  check('PM2.5 30 -> AQI 50 (Good upper edge)', subIndex('pm25', 30) === 50);
  check('PM2.5 60 -> AQI 100', subIndex('pm25', 60) === 100);
  check('PM2.5 250 -> AQI 400', subIndex('pm25', 250) === 400);
  check('PM10 100 -> AQI 100', subIndex('pm10', 100) === 100);
  check('PM10 350 -> AQI 300', subIndex('pm10', 350) === 300);
  check('AQI is the worse of the two sub-indices', aqiOf(45, 300) === subIndex('pm10', 300));
  check('band names follow CPCB', bandOf(45) === 'good' && bandOf(150) === 'moderate' && bandOf(450) === 'severe');
  const base = air({}), acted = air({ measures: { dust: true, burning: true, traffic: true, industry: true }, advice: true });
  check('measures cut the mean AQI and the very poor/severe days', acted.mean < base.mean && acted.bad < base.bad, `${base.mean}->${acted.mean}, ${base.bad}->${acted.bad} days`);
  check('measures avoid hospital visits', acted.visitsAvoided > 0 && base.visitsAvoided === 0);
}

// BIS 10500 water
{
  const ok = { id: 'a', ph: 7.2, turbidity: 0.6, tds: 380, fluoride: 0.6, nitrate: 20, arsenic: 0.002, ecoli: 0, people: 100 };
  check('clean sample has no problems', problemsOf(ok).length === 0);
  check('E. coli in any 100 mL fails', problemsOf({ ...ok, ecoli: 3 }).includes('ecoli'));
  check('fluoride above 1.5 mg/L fails', problemsOf({ ...ok, fluoride: 2.1 }).includes('fluoride'));
  check('fluoride 1.2 passes when no other source (permissible 1.5)', !problemsOf({ ...ok, fluoride: 1.2 }).includes('fluoride'));
  check('arsenic above 0.01 mg/L fails', problemsOf({ ...ok, arsenic: 0.03 }).includes('arsenic'));
  check('nitrate has no relaxation above 45', problemsOf({ ...ok, nitrate: 60 }).includes('nitrate') && BIS.nitrate.perm === null);
  const fl = { ...ok, id: 'f', fluoride: 2.4 };
  check('boiling does not remove fluoride', water([fl], { f: 'boil' }).rows[0].safe === false);
  check('defluoridation makes it safe', water([fl], { f: 'defluoride' }).rows[0].safe === true);
  const muddy = { ...ok, id: 'm', turbidity: 12, ecoli: 40 };
  check('chlorine alone fails in turbid water', water([muddy], { m: 'chlorine' }).rows[0].safe === false);
  check('filter then chlorinate works', water([muddy], { m: 'filterChlorine' }).rows[0].safe === true);
}

console.log(fail ? `\n${fail} check(s) failed` : '\nall checks passed');
process.exit(fail ? 1 : 0);
