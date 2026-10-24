import os
import time
import subprocess

TOOLS_DIR = os.path.dirname(__file__)
WATCH_EXTENSIONS = ('.py', '.json')

def get_mtimes():
    mtimes = {}
    for root, _, files in os.walk(TOOLS_DIR):
        for f in files:
            if f.endswith(WATCH_EXTENSIONS) and not f.startswith("academic_master.db"):
                path = os.path.join(root, f)
                try:
                    mtimes[path] = os.path.getmtime(path)
                except OSError:
                    pass
    return mtimes

def run_update():
    print("\n[AutoUpdater] Change detected! Rebuilding database and game chunks...")
    subprocess.run(["python", os.path.join(TOOLS_DIR, "init_master_db.py")])
    subprocess.run(["python", os.path.join(TOOLS_DIR, "expand_bank_volume.py")])
    subprocess.run(["python", os.path.join(TOOLS_DIR, "expand_bank_volume_part2.py")])
    subprocess.run(["python", os.path.join(TOOLS_DIR, "ingest_batch4.py")])
    subprocess.run(["python", os.path.join(TOOLS_DIR, "auto_matrix_generator.py")])
    subprocess.run(["python", os.path.join(TOOLS_DIR, "export_chunks.py")])
    print("[AutoUpdater] Update complete. Game manifest and chunks refreshed.\n")

if __name__ == "__main__":
    print("[AutoUpdater] Watching tools/ directory for updates (Ctrl + C to stop)...")
    last_mtimes = get_mtimes()
    while True:
        time.sleep(2)
        current_mtimes = get_mtimes()
        if current_mtimes != last_mtimes:
            last_mtimes = current_mtimes
            run_update()
