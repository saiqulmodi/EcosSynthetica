// Checks the Engineering, Agriculture and Forestry case models.
// Run: node tests/tracks.test.mjs
import { solarWard, rationalQ, drains, wheat, irrigation, tigers, mangroves } from '../js/tiers/professional/tracks/models.js';

let fail = 0;
const check = (name, ok, info = '') => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${name}${info ? '  (' + info + ')' : ''}`); if (!ok) fail++; };

// Engineering
{
  const base = solarWard({});
  check('ward uses 3,600 MWh a year', Math.round(base.demand) === 3600);
  check('1 MW of rooftop solar gives about 1,500 MWh a year', solarWard({ solarMW: 1 }).solar === 1500);
  const best = solarWard({ solarMW: 2, efficiency: 0.2, batteryMWh: 1 });
  check('2 MW solar + 20% efficiency reaches net zero', best.netZero === 1 && best.co2 === 0);
  check('battery lowers the evening peak', best.peak < solarWard({ solarMW: 2, efficiency: 0.2 }).peak);
  check('rational method: C 0.8, 60 mm/h, 40 ha -> 5.33 m³/s', Math.abs(rationalQ(0.8, 60, 40) - 5.333) < 0.01);
  const now = drains({});
  check('the old 3 m³/s drain floods in the 2-year storm', !now.storms[0].ok);
  check('greener catchment lowers runoff and recharges water', drains({ dC: 0.11 }).storms[0].Q < now.storms[0].Q && drains({ dC: 0.11 }).recharge > 0);
  check('a 6.5 m³/s drain plus a greener catchment handles every design storm', drains({ capacity: 6.5, dC: 0.11, desilt: true }).safety === 1);
}

// Agriculture
{
  const y0 = wheat({ dose: 0 }), y120 = wheat({ dose: 120, method: 'split' }), y180 = wheat({ dose: 180, method: 'split' });
  check('yield rises with nitrogen but with diminishing returns', y120.yieldQ > y0.yieldQ && (y180.yieldQ - y120.yieldQ) < (y120.yieldQ - y0.yieldQ));
  check('120 kg N in splits gives 45-50 q/ha (typical irrigated wheat)', y120.yieldQ > 45 && y120.yieldQ < 50, y120.yieldQ.toFixed(1));
  check('split doses lose less N than one basal dose', wheat({ dose: 120, method: 'split' }).lost < wheat({ dose: 120 }).lost);
  check('a legume before wheat raises yield at the same dose', wheat({ dose: 60, method: 'split', legume: true }).yieldQ > wheat({ dose: 60, method: 'split' }).yieldQ);
  const fl = irrigation({ method: 'flood' }), dr = irrigation({ method: 'drip', mulch: true, sensor: true });
  check('drip with mulch and sensor uses less than half the water of flooding', dr.volume < fl.volume * 0.5, `${Math.round(dr.volume)} vs ${Math.round(fl.volume)} m³`);
  check('drip saves pumping energy', dr.kwh < fl.kwh);
  check('drip earns more over 5 seasons even after paying its share', dr.income > fl.income);
}

// Forestry
{
  const bad = tigers({ poaching: 0.08, preyTarget: 20 });
  const good = tigers({ poaching: 0.02, preyTarget: 40, corridor: true, relocate: true });
  check('with poaching and few prey, tigers stay low', bad.tigers < 30, bad.tigers.toFixed(0));
  check('protection + prey recovery lets tigers grow', good.tigers > bad.tigers * 1.5, good.tigers.toFixed(0));
  const noCorr = tigers({ poaching: 0.02, preyTarget: 40, relocate: true });
  check('a corridor lowers human-tiger conflict', good.conflict < noCorr.conflict);
  const none = mangroves({}), m500 = mangroves({ width: 500 }), mono = mangroves({ width: 500, mix: 'mono' });
  check('with no mangroves the cyclone overtops the embankment', none.breach);
  check('500 m of native mangroves keeps the embankment safe', !m500.breach, m500.level.toFixed(2) + ' m');
  check('single-species planting survives worse and protects less', mono.level > m500.level);
  check('shelters cut people at risk when the embankment breaks', mangroves({ shelters: true }).atRisk < none.atRisk);
}

console.log(fail ? `\n${fail} check(s) failed` : '\nall checks passed');
process.exit(fail ? 1 : 0);
