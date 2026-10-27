"""Maximized build_quiz.py: compiles a massive, balanced PCB NEET bank from neet_hub.db."""
import json
import random
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HUB = Path(r"C:\Users\saiqu\Projects\NEET_Data_Hub\output\neet_hub.db")

# Maximize active questions per form (4,000 total across 4 forms)
PER_FORM = 5000

# Subject and theme weighting per gameplay tier/form:
# Form 0: Cytology, Microorganisms, Optics, Atomic Structure, Basic Nature
# Form 1: Plant Ecology, Photosynthesis, Thermodynamics, Solutions, Agriculture
# Form 2: Animal Physiology, Biomechanics, Buoyancy, Acids & Bases, Ecosystems
# Form 3: Genetics, Evolution, Human Health, Organic Chemistry, Disease & Hygiene
THEMES = {
    0: {"bio": ["%cell%", "%microb%", "%prokaryot%", "%living%"], "chem": ["%atom%", "%matter%", "%material%"], "phy": ["%optic%", "%lens%", "%mirror%", "%light%", "%refract%"]},
    1: {"bio": ["%plant%", "%photosynth%", "%respirat%", "%nutrit%", "%crop%"], "chem": ["%solution%", "%thermo%", "%mole%", "%state%"], "phy": ["%work%", "%energy%", "%power%", "%heat%"]},
    2: {"bio": ["%animal%", "%insect%", "%bee%", "%flower%", "%pollinat%", "%food%", "%habitat%"], "chem": ["%acid%", "%base%", "%salt%", "%react%"], "phy": ["%motion%", "%force%", "%newton%", "%gravit%", "%densit%", "%buoyan%", "%pressure%"]},
    3: {"bio": ["%gene%", "%hered%", "%evolut%", "%reproduc%", "%health%", "%diseas%", "%ill%"], "chem": ["%carbon%", "%compound%", "%biomolecul%", "%organic%"], "phy": ["%sound%", "%electr%", "%wave%"]}
}

def clean_text(val):
    if not val:
        return ""
    s = str(val).strip()
    s = s.replace("\u2014", "—").replace("\u2013", "–")
    s = s.replace("\u2018", "'").replace("\u2019", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    return s

def fetch_pool(con, subject, classes, patterns):
    if not patterns:
        return []
    where_parts = []
    params = [subject]
    for p in patterns:
        where_parts.append("LOWER(c.title) LIKE ?")
        params.append(p)
    class_placeholders = ",".join(["?"] * len(classes))
    params.extend(classes)
    
    query = f"""
        SELECT q.id, q.class_level, c.title, c.subject,
               q.question, q.option_a, q.option_b, q.option_c, q.option_d,
               q.correct_option, q.explanation
        FROM questions q
        JOIN chapters c ON c.id = q.chapter_id
        WHERE c.subject = ? AND ({' OR '.join(where_parts)}) AND q.class_level IN ({class_placeholders})
    """
    try:
        return con.execute(query, params).fetchall()
    except Exception as e:
        return []

def build_form(con, form_id, rng, limit=PER_FORM):
    theme = THEMES[form_id]
    
    # 1. Senior NEET Core (Classes 11 & 12): Biology, Chemistry, Physics
    neet_bio = fetch_pool(con, "Biology", [11, 12], theme.get("bio", []))
    neet_chem = fetch_pool(con, "Chemistry", [11, 12], theme.get("chem", []))
    neet_phy = fetch_pool(con, "Physics", [11, 12], theme.get("phy", []))
    
    # Fallback to general 11-12 pool if specific theme pattern count is light
    if len(neet_chem) < 50:
        neet_chem += con.execute("SELECT q.id, q.class_level, c.title, c.subject, q.question, q.option_a, q.option_b, q.option_c, q.option_d, q.correct_option, q.explanation FROM questions q JOIN chapters c ON c.id = q.chapter_id WHERE c.subject = 'Chemistry' AND q.class_level IN (11, 12) LIMIT 300").fetchall()
    if len(neet_phy) < 50:
        neet_phy += con.execute("SELECT q.id, q.class_level, c.title, c.subject, q.question, q.option_a, q.option_b, q.option_c, q.option_d, q.correct_option, q.explanation FROM questions q JOIN chapters c ON c.id = q.chapter_id WHERE c.subject = 'Physics' AND q.class_level IN (11, 12) LIMIT 300").fetchall()
    
    # 2. High School Foundations (Classes 9 & 10)
    found_bio = fetch_pool(con, "Biology", [9, 10], theme.get("bio", []))
    found_chem = fetch_pool(con, "Chemistry", [9, 10], theme.get("chem", []))
    found_phy = fetch_pool(con, "Physics", [9, 10], theme.get("phy", []))
    
    # 3. Early Foundations (Classes 1-8)
    early = con.execute("""
        SELECT q.id, q.class_level, c.title, c.subject,
               q.question, q.option_a, q.option_b, q.option_c, q.option_d,
               q.correct_option, q.explanation
        FROM questions q
        JOIN chapters c ON c.id = q.chapter_id
        WHERE q.class_level <= 8
    """).fetchall()
    
    # Target allocations
    t_neet_bio = int(limit * 0.35)
    t_neet_chem = int(limit * 0.15)
    t_neet_phy = int(limit * 0.10)
    t_found = int(limit * 0.25)
    t_early = limit - (t_neet_bio + t_neet_chem + t_neet_phy + t_found)
    
    s_neet_bio = rng.sample(neet_bio, min(t_neet_bio, len(neet_bio))) if neet_bio else []
    s_neet_chem = rng.sample(neet_chem, min(t_neet_chem, len(neet_chem))) if neet_chem else []
    s_neet_phy = rng.sample(neet_phy, min(t_neet_phy, len(neet_phy))) if neet_phy else []
    
    found_all = found_bio + found_chem + found_phy
    s_found = rng.sample(found_all, min(t_found, len(found_all))) if found_all else []
    s_early = rng.sample(early, min(t_early, len(early))) if early else []
    
    combined = s_neet_bio + s_neet_chem + s_neet_phy + s_found + s_early
    rng.shuffle(combined)
    
    out = []
    seen = set()
    for row in combined:
        qid, cls, topic, subject, q_text, opt_a, opt_b, opt_c, opt_d, corr, expl = row
        q_cleaned = clean_text(q_text)
        if q_cleaned in seen:
            continue
        seen.add(q_cleaned)
        
        opt_map = {"A": opt_a, "B": opt_b, "C": opt_c, "D": opt_d}
        correct_text = opt_map.get(str(corr).strip().upper(), opt_a)
        wrong_opts = [clean_text(v) for k, v in opt_map.items() if k != str(corr).strip().upper() and v]
        opts = [clean_text(correct_text)] + wrong_opts[:3]
        if len(opts) < 4:
            continue
            
        out.append({
            "id": int(qid),
            "cls": int(cls),
            "subject": clean_text(subject),
            "topic": clean_text(topic),
            "q": q_cleaned,
            "opts": opts,
            "ans": 0,
            "why": clean_text(expl) or f"Correct answer: {opts[0]}."
        })
        if len(out) >= limit:
            break
            
    return out

def main():
    if not HUB.exists():
        print(f"Error: Database not found at {HUB}")
        sys.exit(1)

    con = sqlite3.connect(HUB)
    rng = random.Random(42)
    bank_data = {}

    print(f"Maximizing Question Bank (Target: {PER_FORM} questions per form)...")
    for form_id in range(4):
        bank_data[str(form_id)] = build_form(con, form_id, rng, limit=PER_FORM)
        print(f"  Form {form_id}: {len(bank_data[str(form_id)])} questions extracted.")

    con.close()

    # The game loads one compact pack per form on demand (content/questions/scientist/form-N.json).
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from build_packs import write_scientist_packs
    size = write_scientist_packs(bank_data)
    print(f"\nSuccessfully wrote the scientist question packs ({size / 1024 / 1024:.2f} MB).")

if __name__ == "__main__":
    main()
