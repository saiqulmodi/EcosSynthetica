# EcosSynthetica: Three-Tier Redesign

**Technical design document**, 27 Oct 2026
Repo: https://github.com/saiqulmodi/EcosSynthetica, live at https://saiqulmodi.github.io/EcosSynthetica/

EcosSynthetica becomes a learning path that grows with the student:

```
ECO EXPLORER  (Class 1-10, easy)
      |  complete -> unlock
ECO SCIENTIST (Class 11-12, medium)
      |  complete -> unlock
ECO PROFESSIONAL (advanced, choose a track)
   Health/MBBS | Engineering | Agriculture | Forestry & Env. Science | Research
```

The design starts from what the game already is. It does not start from a blank page.

---

## 0. Starting point (what exists today)

| Area | Today | Where it goes in the redesign |
|---|---|---|
| Engine | Three.js 0.160 through an import map, plain ES modules, no build step, GitHub Pages | Kept. Shared engine for all three tiers |
| Game | 4 forms (Single Cell, Plant Seedling, Honey Bee, Human), 42 organisms, 70 Lab parts, scan, Synthesis Lab, immune memory, ecosystem balance, evolve quiz | Becomes the core of **Eco Scientist**. Nothing is removed |
| Content | `js/Database.js` (Data Hub), `js/lang/*.js` (hi/bn), `js/lang/why.js` | Split into per-tier content packs |
| Questions | `js/quizbank.js` (5.8 MB, loaded at start), `data/neet_academic_bank.json`, `data/chapters/*.json`, `tools/academic_master.db` | Loaded per tier and per class, only when needed |
| Language | `js/i18n.js`: en/hi/bn, falls back to English | Becomes a language registry, so new languages are data only |
| Voice | `js/Speech.js` (device voices) | Core of Explorer (voice-first) |
| Save | `localStorage` key `ecos-synthetica-v1` | Migrated to profile v2. Old progress is kept |
| Privacy | No analytics (Firebase and GoatCounter removed) | Stays this way. School tracking is designed without telemetry (section 7) |

---

## Size limit: the whole game fits within 20 MB

All three tiers together, with every language, question, voice file and dataset, ship in **20 MB or less**. That is the full offline install: the website files the service worker caches, and the zip. Today the game is about 7 MB, and `js/quizbank.js` alone is 6 MB because it is pretty-printed JSON.

| Part | Budget | How it stays inside |
|---|---|---|
| Three.js engine (kept locally for offline play) | 1.3 MB | One minified module; no extra Three.js add-ons |
| Game code, all tiers | 1.5 MB | Plain ES modules, minified at release |
| Content text packs (en/hi/bn) | 2.5 MB | Compact JSON with short keys and no indentation; each text is stored once and reused by key |
| Question banks (Class 1-12 + tracks) | 5.0 MB | Compact JSON (today's 6 MB bank becomes about 3.5 MB); split into per-class packs |
| Narration audio | 6.0 MB | Opus, mono, 16 kbps (about 2 KB per second) gives about 50 minutes. Recorded audio is used where a device voice is missing (Bengali first); en/hi use the device voice when present |
| Fonts (Devanagari + Bengali) | 0.6 MB | Noto woff2, cut down to the characters actually used |
| Icons and pictures | 0.5 MB | SVG only; 3D bodies stay procedural (low-poly, built in code), so there are no 3D model files or textures |
| Professional/Research datasets | 1.5 MB | Pre-aggregated CSV (district or state level, not raw records) |
| Reserve | 1.1 MB | For fixes and new content |
| **Total** | **20.0 MB** | |

**Rules that keep it there**
- `tools/check_size.py` adds up everything that ships and fails the build if the total is over 20 MB or any row is over its budget. Every phase runs it before commit.
- Map tiles in Research mode are online-only and are never stored, so they do not count towards the 20 MB.
- The live AI (optional) runs on a server, so it adds nothing on the device.
- The Android app is the same 20 MB of files plus the Capacitor wrapper (about 4 MB).
- New content must fit the budget. If something must grow, another row shrinks first, or that content becomes an optional download pack outside the core 20 MB.

---

## 1. Software architecture

```
                         index.html (one page, import map)
                                    |
                               js/app/main.js
                                    |
          +-------------------------+--------------------------+
          |                         |                          |
     App Shell                Tier Router                Platform services
 (start, profile,        loads one tier module       i18n registry, Speech, Sound,
  path map, settings)    on demand (dynamic import)  Storage (IndexedDB), ContentLoader,
          |                         |                  Mentor (AI), Progress, Badges
          |        +----------------+----------------+
          |        |                |                |
          |   tiers/explorer   tiers/scientist   tiers/professional
          |   (Nature Trail)   (today's game +   (track picker + scenario
          |                     dashboard,        engine; one module per track)
          |                     journal, experiments)
          |        \                |                /
          |         +----- Engine core (Three.js) --+
          |          scene, Controls, Scanner, biome builder,
          |          mesh builders, energy burst, render loop
          |
     Content packs (static JSON, versioned, per tier / class / track / language)
```

**Rules of the architecture**

1. **One engine, three games.** `Controls`, `ScannerSystem`, `Organisms.js` meshes, `Speech`, `Sound` and `i18n` are shared. Each tier only adds its own rules and UI.
2. **Load only what is needed.** Each tier is a dynamic `import()`. Question banks and content load per tier and per class, so a Class 3 child never downloads 5.8 MB of NEET questions.
3. **Offline first, no server needed.** The whole MVP runs as static files on GitHub Pages and works offline once a service worker caches it. A server is optional and only for schools that choose to sync (section 14).
4. **Content is data.** Missions, modules, scenarios, questions and translations are JSON, built from the SQLite authoring databases by Python tools in `tools/`. Code never holds lesson text.
5. **One explanation, three registers.** Every concept has an `explorer`, a `scientist` and a `professional` text. The AI Mentor and the UI pick the one that fits the player's tier (section 8).

---

## 2. Folder structure

The MVP leaves today's files in place and adds new folders next to them. Old modules move into `core/` only in Phase 4, when that can be done safely and tested.

```
EcosSynthetica/
  index.html                  one page; import map for three
  sw.js                       service worker (offline cache), NEW
  js/
    app/                      NEW
      main.js                 boot, Tier Router
      Shell.js                start screen, path map, profile picker
      Profile.js              profile v2, migration from ecos-synthetica-v1
      Progress.js             unlocks, mastery, badges
      Storage.js              IndexedDB wrapper (localStorage fallback)
      ContentLoader.js        fetch + cache JSON packs by tier/class/lang
    core/                     engine (today's files, moved in Phase 4)
      GameLoop.js  Controls.js  ScannerSystem.js  Organisms.js
      Sound.js  Speech.js  i18n.js
    ai/                       NEW
      Mentor.js               one engine, three personas
      registers.js            explorer / scientist / professional wording rules
      LlmBridge.js            optional, off by default (Advanced)
    tiers/
      explorer/               NEW
        ExplorerGame.js       Nature Trail world and mission runner
        missions/             plantTree.js rescueAnimal.js cleanRiver.js
                              sortWaste.js renewableEnergy.js
        ExplorerUI.js         big-button, icon-first HUD
      scientist/
        ScientistGame.js      wraps today's Game (4 forms, Lab, quiz)
        Dashboard.js          live charts (NEW)
        Journal.js            observation journal (NEW)
        Experiments.js        scenario simulator (NEW)
        models/               logistic.js lotkaVolterra.js carbon.js nitrogen.js
      professional/           NEW
        TrackPicker.js
        ScenarioEngine.js     shared case runner: brief, data, decisions, outcome, debrief
        health/  engineering/  agriculture/  forestry/  research/
    charts/                   tiny SVG chart helper (no library)
  content/                    NEW, generated by tools/, never edited by hand
    manifest.json             every pack with version + hash
    explorer/{class-1..10}/{en,hi,bn}.json
    scientist/{core,experiments}/{en,hi,bn}.json
    professional/{health,engineering,agriculture,forestry,research}/{en,hi,bn}.json
    questions/{explorer|scientist|professional}/{class or track}.json
    lang/registry.json        languages, fonts, speech codes
  data/                       today's question data (kept)
  tools/
    build_content.py          SQLite -> content/ packs, NEW
    build_quiz.py             today's quiz builder (kept)
    validate_content.py       every key exists in en+hi+bn, NEW
  docs/
    REDESIGN_THREE_TIERS.md   this file
```

---

## 3. Database schema

There are three layers. Only the first two exist in the MVP.

### 3a. Authoring database (SQLite, `tools/ecos_content.db`)

Used by Claude and the build tools. Its output is the static JSON in `content/`.

```sql
CREATE TABLE tier      (id TEXT PRIMARY KEY,            -- explorer | scientist | professional
                        ord INTEGER, min_class INTEGER, max_class INTEGER);
CREATE TABLE track     (id TEXT PRIMARY KEY,            -- health, engineering, agriculture, forestry, research
                        tier_id TEXT REFERENCES tier(id), ord INTEGER);
CREATE TABLE module    (id TEXT PRIMARY KEY,            -- e.g. exp_water_cycle, sci_nitrogen, pro_vector_disease
                        tier_id TEXT REFERENCES tier(id), track_id TEXT REFERENCES track(id),
                        class_band TEXT,                -- '1-3', '4-7', '8-10', '11-12', 'pro'
                        ord INTEGER, unlock_after TEXT REFERENCES module(id));
CREATE TABLE concept   (id TEXT PRIMARY KEY, module_id TEXT REFERENCES module(id),
                        source TEXT NOT NULL);          -- NCERT chapter, WHO, CPCB, ICMR ... (real source required)
CREATE TABLE text      (key TEXT, lang TEXT, register TEXT,   -- register: explorer | scientist | professional
                        body TEXT NOT NULL, audio TEXT,       -- optional recorded narration file
                        PRIMARY KEY (key, lang, register));
CREATE TABLE activity  (id TEXT PRIMARY KEY, module_id TEXT REFERENCES module(id),
                        kind TEXT,                      -- mission | minigame | experiment | scenario | case
                        config JSON NOT NULL,           -- world, goals, model parameters
                        est_minutes INTEGER);
CREATE TABLE question  (id INTEGER PRIMARY KEY, module_id TEXT REFERENCES module(id),
                        class INTEGER, track_id TEXT, difficulty INTEGER,   -- 1..5
                        q_key TEXT, opts_key TEXT, ans INTEGER, why_key TEXT,
                        origin TEXT);                   -- game | school_mcq_bank | neet_hub | authored
CREATE TABLE badge     (id TEXT PRIMARY KEY, tier_id TEXT, rule JSON, icon TEXT);
CREATE TABLE dataset   (id TEXT PRIMARY KEY, track_id TEXT, title_key TEXT,
                        source_url TEXT, licence TEXT, as_of DATE, file TEXT);
```

Existing sources feed it: `Database.js` organisms and parts, `tools/academic_master.db`, the School MCQ Bank (Class 1-12) and the NEET Data Hub.

### 3b. On-device store (IndexedDB `ecos`, one per browser)

```
profiles     { id, name, avatar, class, lang, tier, track, createdAt, schoolCode? }
progress     { profileId, moduleId, status: locked|open|done, stars 0-3, bestScore, updatedAt }
attempts     { profileId, questionId, correct, at }        -- powers spaced review
journal      { profileId, id, activityId, text, data(JSON), photo?, at }
badges       { profileId, badgeId, at }
saves        { profileId, tier, state(JSON) }                -- e.g. today's 4-form game state
settings     { key, value }                                  -- sound, language, text size
```

Several children can share one tablet: each has a profile, with no login.

**Migration:** on first run, `ecos-synthetica-v1` is read and copied into a profile's `saves.scientist`. That player is placed in Eco Scientist with every form, scan and counter kept. The old key is left in place.

### 3c. School server (optional, Advanced, PostgreSQL)

```sql
school(id, name, district, state, board, created_at)
class_group(id, school_id, name, grade, teacher_id, join_code)
app_user(id, role, display_name, school_id, created_at)   -- no email for students
enrollment(user_id, class_group_id)
progress_snapshot(user_id, module_id, status, stars, best_score, synced_at)
assignment(id, class_group_id, module_id, due_on)
```

Only module-level results are stored. There are no clicks, no events and no location data.

---

## 4. User roles

| Role | Where | Can do |
|---|---|---|
| **Student: Explorer** | device | Play Class 1-10 missions; voice and pictures; badges |
| **Student: Scientist** | device | Today's game, dashboard, journal, experiments, AI Tutor |
| **Student: Professional** | device | Choose tracks, run cases, export reports |
| **Teacher** | device or school server | Make a class code, see class progress (from the report file or sync), assign modules, unlock a tier for a whole class |
| **Parent** | device | See their child's progress card (read-only), set screen-time limit |
| **School admin** | school server | Manage teachers and classes |
| **Content editor** | authoring DB + tools | Add or translate content; `validate_content.py` must pass |

---

## 5. Learning progression model

### Tiers, bands and unlocks

| Tier | Band | Modules | Unlock rule |
|---|---|---|---|
| Explorer | 1-3 (picture and voice only) | Plants, Animals, Water | Start here, or the child's class is 1-3 |
| Explorer | 4-7 | + Food Chains, Water Cycle, Pollution | 70% of the band before it, or class placement |
| Explorer | 8-10 | + Biodiversity, Climate Basics | 70% of 4-7, or class placement |
| Scientist | 11-12 | Carbon Cycle, Nitrogen Cycle, Ecosystem Dynamics, Population Growth, Biodiversity Loss, Climate Change, Conservation Biology, plus today's 4 forms | Explorer 8-10 done, **or** placement test passed |
| Professional | Tracks A-E | Health/MBBS, Engineering, Agriculture, Forestry & Env. Science, Research | Scientist done, **or** placement test passed; tracks can be taken in any order |

**Placement test (in addition to the unlock chain).** A Class 12 student or an MBBS student should not have to finish Class 1 missions first. Each tier gate has a 10-question placement test. With 7 or more correct, the tier opens and the earlier tiers stay open to replay. A teacher code can also unlock a tier for a whole class.

### Mastery inside a module

```
Learn (story / case brief) -> Do (mission / experiment / scenario) -> Check (3-5 questions)
       -> stars: 1 = done, 2 = 60%+, 3 = 90%+ and no hints
Module done = activity finished + check >= 60%
```

Questions the player gets wrong come back after 1, 3 and 7 days (spaced review, from the `attempts` store). The next question is picked at random but is never a look-alike of the last few (`spreadOrder`, as the quiz does today).

---

## 6. Gamification system

| Element | Explorer | Scientist | Professional |
|---|---|---|---|
| Currency | **Seeds**: plant real trees in your own world | **Evolution points** (as today) | **Impact score**: lives protected, tonnes CO2 avoided, hectares restored |
| Badges | Picture badges: "River Friend", "Seed Planter", "Waste Wizard" | Discovery badges: every organism scanned, every cycle balanced | Credentials: "Outbreak Investigator I-III", "Net-Zero Planner" |
| Visible growth | Your world gets greener after each mission | Ecosystem balance meter, the 4 forms | A case portfolio (exportable PDF) |
| Social | Whole-class goal ("our class planted 500 trees") | Share a journal entry with the teacher | Peer review of case reports (Advanced) |
| Streak | Gentle daily seed, never punished for a missed day | Weekly research goal | None |

**Rules we keep:** no leaderboards ranking young children against each other, no loot boxes, no paid items, no countdown pressure in Explorer, and no analytics. Sound comes only from actions (no music loops), as today.

---

## 7. School progress without tracking

The brief asks for school progress tracking, and the project rule is no analytics. Both are met like this:

1. **MVP: report card file.** The student taps "Share with teacher". The game makes a small signed JSON (or a QR code) with module results only. The teacher opens `teacher.html` (a static page) and drops in the files to see the class table. No server, nothing leaves the device without a tap.
2. **Advanced: school sync (opt-in).** A school can run its own sync server (section 14). The student joins with a class code. Only `progress_snapshot` rows are sent (section 3c).

---

## 8. AI integration design

### One Mentor engine, three personas

| Persona | Tier | Voice | Example: "Why do plants need sunlight?" |
|---|---|---|---|
| **AI Mentor** (Mitra) | Explorer | Short, warm, spoken aloud, one idea at a time | "Leaves catch sunlight and make food from it, like a kitchen. That food helps the plant grow tall." |
| **AI Teacher** | Scientist | Scientific, NCERT terms, asks back | "Photosynthesis: 6CO2 + 6H2O -> C6H12O6 + 6O2, light reactions in thylakoids make ATP and NADPH for the Calvin cycle. What limits the rate on a cloudy day?" |
| **AI Research Assistant** | Professional | Professional terms, cites sources, gives numbers | "Net primary productivity sets the energy budget of the system. For this crop model, light-use efficiency is about 1.5-3 g/MJ PAR; check your irradiance input against IMD data." |

### Two layers

**Layer 1: offline Mentor (MVP, always on, free).** No model and no network. `Mentor.js` answers from the content database:

```
ask(question | conceptId, profile) ->
   match concept (keywords + current activity)
   -> text[conceptId][profile.lang][register(profile.tier)]
   -> hint ladder (nudge -> clue -> worked step), as the Lab hints do today
   -> Speech.speak() for Explorer
```

Because each `concept` has three authored registers in en/hi/bn, the age-matched explanation is guaranteed correct and works offline on a low-end phone. Explorer children only see tap-to-ask buttons ("What is this?", "Why?", "Help me"), with no free typing, which is the safe design for Class 1-10.

**Layer 2: optional live model (Advanced, Scientist and Professional only, off by default).**

```
browser LlmBridge.js --HTTPS--> school or project proxy (Cloudflare Worker)
                                 | holds the API key, rate-limits, strips names,
                                 | adds system prompt + retrieved concept texts
                                 v
                           Claude API (claude-haiku-5-5 for tutoring;
                                       claude-sonnet-5-5 for Research Assistant reports)
```

- The API key is never in the browser.
- System prompt = persona + register rules + "answer only from the supplied concept texts and cite them; if unsure, say so".
- Retrieval: the matching `concept`/`text` rows are sent with the question, so the model explains our checked content and does not invent it.
- If the proxy is missing or offline, the game falls back to Layer 1 without breaking.
- No local AI model runs on the device, so older phones and laptops keep working.

---

## 9. API structure

### MVP: module interfaces (no server)

```js
// app/ContentLoader.js
loadPack(tier, part, lang)            // -> JSON, cached by the service worker
loadQuestions(tier, classOrTrack)     // -> [{id, q, opts, ans, why, module}]

// app/Progress.js
complete(profileId, activityId, score)   // -> { stars, unlocked: [...], badges: [...] }
isUnlocked(profileId, moduleId)
placement(profileId, tier, answers)      // -> { passed, score }

// ai/Mentor.js
ask({ text?, conceptId?, activityId }, profile)  // -> { answer, register, source, hintLevel }

// tiers/*/  every tier module exports the same contract
export async function mount(stageEl, ctx)   // ctx = { profile, lang, mentor, progress, content }
export function unmount()
```

### Advanced: school sync REST (`/api/v1`, JSON, token from class code)

```
POST /auth/join            { classCode, displayName }      -> { token, userId }
GET  /classes/:id/assignments                              -> [ {moduleId, dueOn} ]
PUT  /progress             [ {moduleId, status, stars, bestScore} ]   (batch upsert)
GET  /classes/:id/progress (teacher)                       -> table of students x modules
POST /mentor/ask           { conceptIds, question, register, lang }   -> { answer, sources }
GET  /content/manifest                                     -> pack versions (for updates)
```

---

## 10. UI/UX design specification

| | Explorer | Scientist | Professional |
|---|---|---|---|
| Look | Bright day scene, rounded shapes, large friendly animals | Today's dark academic theme | Clean work-desk layout, light or dark |
| Buttons | 64 px minimum, icon + one word | 44 px minimum | 36 px minimum, keyboard shortcuts |
| Text | One line at most; every line has a speaker button; Class 1-3 runs with **no reading needed** | Paragraphs, equations, units | Dense tables, references, units |
| Controls | Tap where to walk; auto-scan when close | WASD / joystick (today) | Map + panels; 3D view is optional |
| Feedback | Big animation + sound + voice praise | Toasts, hint ladder | Outcome numbers + debrief |
| Screens | Home map -> Mission -> Celebrate | HUD + Dashboard + Journal + Lab + Codex | Track picker -> Case brief -> Data -> Decisions -> Outcome -> Report |

**Shared rules:**
- Theme colours as CSS tokens per tier (`[data-tier="explorer"]`).
- Fonts that cover Devanagari and Bengali (Noto Sans, Noto Sans Devanagari, Noto Sans Bengali), with text size settings at 100/125/150%.
- Works at 360 px phone width.
- Colour is never the only signal (shapes and icons too).
- Respects reduced-motion.
- The language button is on every screen, as now.

**Bengali voice:** this PC has no Bengali voice, and many phones have none. Explorer narration therefore also ships as recorded or pre-generated audio files (`text.audio`) for en/hi/bn, so Class 1-3 never depends on a device voice.

---

## 11. Implementation plan: Three.js (recommended) vs Unity

**Recommendation: stay on Three.js.**

| | Three.js (today) | Unity WebGL |
|---|---|---|
| Existing work | All 42 organisms, Lab and quiz kept | Full rewrite |
| Download | About 1 MB of engine + content | 15-40 MB first load |
| Low-end school phones | Good (low-poly, pixel ratio cap already in place) | Weak in browsers |
| Hosting | GitHub Pages, free | Same, but heavier |
| Android app | Capacitor wraps the same files | Separate build |
| Charts, forms, multilingual text | Native HTML | Harder (TextMeshPro + fonts) |

**Three.js plan by tier:**
- **Explorer.** One new biome builder "Nature Trail": village, river, school garden and field, built from the existing low-poly helpers in `Organisms.js`. Missions are state machines over shared entities: pick up a sapling, dig, plant, water, then see it grow. River cleaning uses floating litter meshes and a net. Waste sorting is a drag-and-drop HTML overlay over the 3D scene. The renewable-energy mini-game places solar panels and windmills and lights the village. Instanced meshes keep it fast.
- **Scientist.** Today's `Game` is wrapped by `ScientistGame.js`. The dashboard reads `game.balance`, energy, env and populations every second into a ring buffer and draws SVG charts. Experiments are 2D panels: sliders, then a model run (logistic, Lotka-Volterra, carbon/nitrogen box models), then a chart and a journal entry.
- **Professional.** Mostly 2D with HTML + SVG and an optional map (Leaflet 1.9.4 with OpenStreetMap tiles in Research mode). The 3D scene is reused for one "site visit" per case (a village for an outbreak, a field, a forest edge).

---

## 12. Development roadmap

Work goes one phase at a time. Each phase ends with: what changed, how to verify it, and the commit. Then it waits for "go".

| Phase | Content | Done when |
|---|---|---|
| **1. Shell + profiles** | Start screen "Choose your path", profiles in IndexedDB, v1 save migration, Tier Router, quizbank loaded per tier, service worker | Today's game plays exactly as before from "Eco Scientist"; old saves load; first load is smaller |
| **2. Explorer MVP** | Nature Trail world, 5 missions (plant, rescue, river, waste, energy), 7 modules, voice in en/hi/bn, badges, Class 1-10 questions from the School MCQ Bank | A Class 2 child can finish a mission without reading |
| **3. Scientist add-ons** | Dashboard charts, Observation Journal, 4 experiments (population growth, predator-prey, carbon cycle, nitrogen cycle), AI Teacher (offline), placement test | Experiments match textbook results |
| **4. Professional: Health track** | Scenario engine, 3 cases: dengue outbreak (SEIR + Aedes vector), city AQI and health (CPCB AQI bands), village water quality (BIS 10500 limits) | One full case runs brief -> report |
| **5. Teacher tools** | Report-card file/QR + `teacher.html`, class goals | A teacher sees a class table from 30 files |
| **6. More tracks** | Engineering, Agriculture, Forestry | 2-3 cases per track |
| **7. Research mode** | Maps, open datasets, model runs, biodiversity indices (Shannon, Simpson), CSV export | A student reproduces one published Indian dataset result |
| **8. Optional AI + sync** | LLM proxy, school sync server | Works on and off; falls back offline |

---

## 13. MVP plan (Phases 1-4)

**In scope**
- 3 tiers visible on the path map; Professional shows only the Health track (the others are marked "coming").
- Explorer: 1 world, 5 missions, 7 short modules (3 bands), voice-first, badges, Seeds.
- Scientist: today's full game + dashboard + journal + 4 experiments + placement test.
- Professional Health: 3 cases.
- Offline Mentor in 3 registers; en/hi/bn for every new string.
- Offline play; works on a 2 GB RAM Android phone at 360 px.

**Out of scope for the MVP:** live LLM, school server, GIS, Engineering/Agriculture/Forestry/Research tracks.

**MVP quality bar**
- `check_size.py` passes: everything that ships is 20 MB or less.
- `validate_content.py` passes: every key exists in en/hi/bn, every concept has a source.
- Every science claim is traced to NCERT, WHO, ICMR, CPCB, IMD, BIS, FSI or a peer-reviewed source.
- Old v1 saves still load.
- First screen loads in under 3 s on 4G.

---

## 14. Advanced version and scalability

### Advanced version
- **Engineering:** a city grid of tiles with power (solar, wind, grid, storage), water (supply, sewage, STP), waste (segregation, compost, biogas, landfill) and transport. Each turn shows the budget, CO2, outages and public health. Cases: "net-zero ward", "monsoon flood-proof drainage".
- **Agriculture:** a field model with soil N-P-K, organic carbon, moisture, crop choice, drip vs flood irrigation, and agroforestry rows. Uses Soil Health Card style inputs. Outcome: yield, water used, soil change over 5 seasons.
- **Forestry & Environmental Science:** population models for tiger/elephant/deer, corridors between protected areas, human-wildlife conflict, restoration with native species. Uses Forest Survey of India (ISFR) style cover data.
- **Research mode:** map layers (Leaflet), uploaded or bundled CSV datasets, model runner (SIR/SEIR, logistic, Lotka-Volterra, carbon box), "AI prediction" as transparent regression/forecast with uncertainty shown, biodiversity indices, and a report export.
- **Live AI** (section 8, Layer 2) and **school sync** (section 3c).

### Scalability plan

| Concern | Plan |
|---|---|
| Download size | Hard cap of 20 MB for everything that ships (see "Size limit"); per-tier dynamic imports; question packs split by class/track (about 50-300 KB each); service worker caches only what was opened |
| Many users | Static hosting needs no server, so the number of students does not matter. Pages can later move to Cloudflare Pages/Netlify with the same files |
| Content growth | Authoring SQLite -> JSON packs with versions and hashes in `content/manifest.json`; the service worker updates changed packs only |
| More languages | `content/lang/registry.json` + one folder of packs per language; the UI falls back to English per key (as today). Adding Tamil, Telugu, Marathi, Odia or Urdu needs no code change. Urdu needs the RTL flag in the registry |
| Low-end devices | Quality presets (pixel ratio, shadow off, entity cap), 2D fallback for Professional |
| School sync | Stateless API on a small VM or serverless; Postgres; one school per row; can be self-hosted by a state or university |
| AI cost | Offline Mentor answers most questions; the LLM is only for typed questions in Scientist/Professional, with Haiku-class models, caching and rate limits per class code |

---

## 15. School and university deployment strategy

| Setting | How it is delivered |
|---|---|
| **Schools with internet** | Open the GitHub Pages link; "Add to Home screen" installs it as an app (offline afterwards) |
| **Schools with poor internet** | One download zip / Android APK (Capacitor). A teacher's laptop can serve it on the classroom Wi-Fi with `serve.py` |
| **Smart classrooms** | Explorer "class mode": one projected screen, the class votes on choices |
| **Teachers** | 1-page guide per module mapped to NCERT chapters; class code; report-card import |
| **Colleges (MBBS, Engineering, Agriculture, Forestry, Env. Sc.)** | Track cases mapped to the syllabus (for example the MBBS Community Medicine competencies for environmental health and vector-borne diseases); case reports usable as assignments |
| **Pilots** | One school (Class 3-8) and one college department first; feedback in a simple form; then a district |
| **Partners to approach** | State SCERTs, DIKSHA (content upload), eco-clubs under the National Green Corps, college NSS units |
| **Privacy and safety** | No analytics; no student email; data stays on the device unless the school turns on sync; no free-text AI chat for Class 1-10 |
| **Cost** | Free to play; hosting free; AI only if a school or university funds its own proxy |

---

### Content rules kept from the current game
- Nature first: every organism's own survival story comes before what it does to people. Countered species are contained, never destroyed.
- Real, sourced science, with Indian history and examples.
- Every new text has English, Hindi and Bengali.
- Sound only from actions; no tracking.
