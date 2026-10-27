"""Records Explorer narration for languages most devices cannot speak (Bengali),
using Microsoft Edge neural voices (pip install edge-tts; needs internet).

Writes content/audio/<lang>/<hash>.mp3 and index.json {hash: file}. The hash is
FNV-1a of the exact text, the same as js/tiers/explorer/Voice.js, so the game
finds the clip for whatever line it is about to say. Only new lines are recorded.

Run:  python tools/build_narration.py [lang]      (default: bn)
"""
import asyncio
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOICES = {"bn": "bn-IN-TanishaaNeural", "hi": "hi-IN-SwaraNeural", "en": "en-IN-NeerjaNeural"}
# Lines with a {n} count are recorded for each count the missions use.
COUNTS = {"m.plant.again": [1, 2], "m.river.left": range(1, 8), "m.spot.left": range(1, 6)}
SPOKEN = re.compile(r"^(m\.|mini\.|sp\.|spn\.|w\.|c\.|it\.|bin\.|ex\.great|ex\.tryAgain|ex\.notThat|ex\.allDone)")


def fnv(s):
    h = 0x811C9DC5
    for b in s.encode("utf-8"):
        h ^= b
        h = (h * 0x01000193) & 0xFFFFFFFF
    return f"{h:08x}"


def lines(lang):
    data = json.loads((ROOT / "content" / "text" / "explorer.json").read_text(encoding="utf-8"))
    ui = {**data["ui"]["en"], **data["ui"].get(lang, {})}
    out = []
    for k, v in ui.items():
        if not SPOKEN.match(k):
            continue
        if k in COUNTS:
            out += [v.replace("{n}", str(n)) for n in COUNTS[k]]
        elif "{" not in v:
            out.append(v)
    for mod in data["modules"].values():
        for card in mod["story"] + [mod["more"], mod["deep"]]:
            out.append(card.get(lang) or card["en"])
        for q in mod["quiz"]:
            out.append(q["q"].get(lang) or q["q"]["en"])
            out += [o[1].get(lang) or o[1]["en"] for o in q["opts"]]
    return list(dict.fromkeys(out))


async def main(lang):
    import edge_tts
    folder = ROOT / "content" / "audio" / lang
    folder.mkdir(parents=True, exist_ok=True)
    index_file = folder / "index.json"
    index = json.loads(index_file.read_text(encoding="utf-8")) if index_file.exists() else {}
    todo = [t for t in lines(lang) if fnv(t) not in index or not (folder / index[fnv(t)]).exists()]
    print(f"{lang}: {len(todo)} new lines to record")
    sem = asyncio.Semaphore(4)

    async def one(text):
        h = fnv(text)
        async with sem:
            for attempt in range(3):
                try:
                    await edge_tts.Communicate(text, VOICES[lang], rate="-8%").save(str(folder / f"{h}.mp3"))
                    index[h] = f"{h}.mp3"
                    return
                except Exception as e:  # network hiccup: try again
                    print("  retry", attempt + 1, text[:40], e)
                    await asyncio.sleep(2)

    await asyncio.gather(*(one(t) for t in todo))
    keep = {fnv(t) for t in lines(lang)}
    for h in list(index):
        if h not in keep:
            (folder / index.pop(h)).unlink(missing_ok=True)
    index_file.write_text(json.dumps(index, separators=(",", ":")), encoding="utf-8")
    size = sum(f.stat().st_size for f in folder.glob("*.mp3"))
    print(f"{lang}: {len(index)} clips, {size / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "bn"))
