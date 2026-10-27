// Checks the Eco Scientist experiment models against textbook results.
// Run: node tests/models.test.mjs
import { logistic, lotkaVolterra, peaks, carbon, nitrogen } from '../js/tiers/scientist/models.js';

let fail = 0;
const check = (name, ok, info = '') => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${name}${info ? '  (' + info + ')' : ''}`); if (!ok) fail++; };
const near = (a, b, tol) => Math.abs(a - b) <= tol;

// 1. Logistic growth: levels off at K; fastest growth at N = K/2; early growth is exponential.
{
  const r = logistic({ r: 0.5, K: 1000, N0: 10, years: 40 });
  const last = r.pts[r.pts.length - 1][1];
  check('logistic levels off at carrying capacity K', near(last, 1000, 1), last.toFixed(1));
  const half = r.pts.reduce((b, p) => (Math.abs(p[1] - 500) < Math.abs(b[1] - 500) ? p : b));
  check('logistic passes K/2 at t = ln((K-N0)/N0)/r', near(half[0], r.tHalf, 0.4), `${half[0].toFixed(2)} vs ${r.tHalf.toFixed(2)}`);
  check('fastest growth rK/4 at K/2', near(r.maxRate, 125, 1e-9));
  const early = r.pts[4];
  check('early logistic growth is close to exponential', Math.abs(early[1] - early[2]) / early[2] < 0.02);
}

// 2. Lotka-Volterra: cycles around H* = d/(cb), P* = a/b; predator peaks lag prey peaks; period about 2*pi/sqrt(ad).
{
  const p = { a: 0.6, b: 0.025, c: 0.4, d: 0.5 };
  const r = lotkaVolterra({ ...p, H0: 52, P0: 25, years: 80 });
  check('equilibrium prey H* = d/(cb) = 50', near(r.Heq, 50, 1e-9));
  check('equilibrium predator P* = a/b = 24', near(r.Peq, 24, 1e-9));
  const hp = peaks(r.pts, 1), pp = peaks(r.pts, 2);
  const per = (hp[hp.length - 1] - hp[0]) / (hp.length - 1);
  check('small cycles: period near 2*pi/sqrt(ad)', near(per, r.period, 0.3), `${per.toFixed(2)} vs ${r.period.toFixed(2)}`);
  check('predator peak follows prey peak', pp.find((t) => t > hp[0]) - hp[0] > 0 && pp.find((t) => t > hp[0]) - hp[0] < r.period / 2);
  // Conserved quantity V = c b H - d ln H + b P - a ln P stays constant (no drift).
  const V = ([, H, P]) => p.c * p.b * H - p.d * Math.log(H) + p.b * P - p.a * Math.log(P);
  const big = lotkaVolterra({ ...p, H0: 40, P0: 9, years: 80 });
  check('conserved quantity holds (no numerical drift)', near(V(big.pts[0]), V(big.pts[big.pts.length - 1]), 1e-3));
}

// 3. Carbon: with today's emissions about 45% of emitted CO2 stays in the air and CO2 rises about 2.3 ppm a year
// (Global Carbon Budget, 2014-2023 average: fossil 9.7 + land use 1.1 GtC/yr, air 5.2 GtC/yr = 2.4 ppm/yr, so about 48% stays in the air).
{
  const r = carbon({ years: 10 });
  const rise = (r.pts[10][1] - r.pts[0][1]) / 10;
  check('CO2 rises about 2-2.6 ppm per year at current emissions', rise > 2.0 && rise < 2.6, rise.toFixed(2) + ' ppm/yr');
  check('airborne fraction about 40-50%', r.airborne > 0.4 && r.airborne < 0.5, (r.airborne * 100).toFixed(0) + '%');
  const zero = carbon({ emit0: 0, forestLoss: 0, years: 30 });
  check('if emissions stop, CO2 slowly falls', zero.pts[30][1] < zero.pts[0][1] && zero.pts[30][1] > 280);
}

// 4. Nitrogen: legumes add nitrogen; waterlogging cuts nitrate (no oxygen for nitrifiers, more denitrification).
{
  const base = nitrogen({});
  const leg = nitrogen({ legume: true });
  const wet = nitrogen({ waterlogged: true });
  check('legume crop fixes 50-150 kg N/ha in a season', leg.fixed >= 50 && leg.fixed <= 150, leg.fixed.toFixed(0) + ' kg');
  check('legume field has more plant-available N', leg.uptake > base.uptake);
  const no3 = (r) => r.pts.reduce((s, p) => s + p[2], 0) / r.pts.length;
  check('waterlogged soil holds less nitrate', no3(wet) < no3(base), `${no3(wet).toFixed(1)} vs ${no3(base).toFixed(1)}`);
  const fert = nitrogen({ fertiliser: 120 });
  check('fertiliser raises losses (leaching + denitrification)', fert.lost > base.lost);
}

console.log(fail ? `\n${fail} check(s) failed` : '\nall checks passed');
process.exit(fail ? 1 : 0);
