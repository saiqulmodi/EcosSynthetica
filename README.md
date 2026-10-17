# Ecos-Synthetica: The Evolutionary Shield

A 3D browser game (Three.js) for PC and phone, in English, Hindi and Bengali.
Fungi, bacteria, viruses, insects, algae, lichens, worms and others are shown from their
own side first: how they survive, what they give the living world, what Earth would lose
without them, and where their energy comes from and goes. Then the player answers them
with the defences life really evolved, and sees how humans came to understand each one:
belief, then observation, then science (with Indian history such as neem, turmeric,
Ayurveda, J. C. Bose, Ronald Ross in Secunderabad and the Madras TB study).

## Play
- Online: https://saiqulmodi.github.io/EcosSynthetica/
- On this PC: double-click `Play Ecos-Synthetica.bat` (needs Python; opens the browser).
- PC controls: WASD or arrows to move, drag to look, wheel to zoom, click or E to scan, L Lab, C Codex.
- Phone: joystick at bottom left, drag to look, pinch to zoom, tap to scan.
- Language: choose English, हिन्दी or বাংলা on the start screen (or the language button in the corner).

## How it works
1. **Scan** an organism (stay within 12 m). A burst of golden sunlight shows its energy
   arriving, then the profile opens: its side of the story, its gift, "without it", an
   animated energy-flow strip, what it does to you, how nature answers, how humans
   understood it, and a fact. **Read aloud** reads the whole profile in the chosen language.
2. **Synthesis Lab**: combine the real parts nature uses (for example CRISPR spacer memory
   + Cas nuclease against a phage). Wrong tries give growing hints.
3. Countered species go into **immune memory** and are contained on contact. They are not
   destroyed; they return to their role in nature. Partners give lasting bonuses.
4. **Ecosystem balance**: partners raise it; heat, drought and cold lower it. Below 50,
   opportunists (Serratia, Aspergillus, Candida) turn invasive.
5. **Evolve**: after enough counters and a partnership, pass a 5-question quiz (3 correct).
   Questions come from your own discoveries plus the School MCQ Bank.
   Single Cell -> Plant Seedling -> Honey Bee -> Human. 42 organisms, 70 Lab parts.

## Files
- `js/Database.js`: the Data Hub (organisms, parts, stories, energy, human history, truths)
- `js/i18n.js`, `js/lang/*.js`: English UI strings and the Hindi and Bengali translations
- `js/Quiz.js`, `js/quizbank.js`: quiz builder; questions copied from the School MCQ Bank
- `js/Speech.js`: read-aloud with the device's own voices
- `js/ScannerSystem.js`: raycast picking and scanning
- `js/SynthesisEngine.js`: recipe checking and hints
- `js/GameLoop.js`: scene, spawning, behaviour, balance, evolution, render loop
- `js/Organisms.js`: procedural low-poly meshes, biomes and the energy burst
- `js/Controls.js`: keyboard, mouse, touch joystick and pinch
- `js/UI.js`: HUD, profiles, Lab, Codex, quiz, dialogs
- `js/Sound.js`: short action sounds only (no music or loops)
- `tools/build_quiz.py`: rebuilds `js/quizbank.js` from `School_MCQ_Bank\output\mcq_bank.db`

Progress is saved in the browser (localStorage).
