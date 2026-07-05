# === Stage 44: Add backup creation for the data file ===
# Project: ServiceBoard
import os, json, datetime
BACKUP_DIR = "backups"
os.makedirs(BACKUP_DIR, exist_ok=True)
def create_backup():
    if not os.path.exists(DATA_FILE): return False
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    src_path = DATA_FILE
    dst_name = f"{BACKUP_DIR}/backup_{now}.json"
    try:
        with open(src_path, "r", encoding="utf-8") as f_src, \
             open(dst_name, "w", encoding="utf-8") as f_dst:
            json.dump(json.load(f_src), f_dst, indent=2)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    print("Backup created:", create_backup())
