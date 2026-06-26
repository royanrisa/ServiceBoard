# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: ServiceBoard
from datetime import datetime, timedelta
import json
import os

ARCHIVE_DIR = "archive"
CUTOFF_DAYS = 90

def archive_old_records(records):
    if not records: return
    now = datetime.now()
    cutoff_date = now - timedelta(days=CUTOFF_DAYS)
    archived = []
    active = []
    for r in records:
        completed_at = r.get("completed_at") or r.get("resolved_at")
        status = r.get("status", "open")
        if (not completed_at and status != "closed") or (datetime.fromisoformat(completed_at) > cutoff_date):
            active.append(r)
        else:
            archived.append(r)
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    with open(os.path.join(ARCHIVE_DIR, f"records_{now.strftime('%Y%m%d')}.json"), "w", encoding="utf-8") as f:
        json.dump(archived, f, ensure_ascii=False, indent=2)
    return active

def restore_records(source_file):
    if not os.path.exists(source_file): return []
    with open(source_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    now = datetime.now()
    cutoff_date = now - timedelta(days=CUTOFF_DAYS)
    restored = []
    for r in data:
        completed_at = r.get("completed_at") or r.get("resolved_at")
        if not completed_at: continue
        try:
            resolved_dt = datetime.fromisoformat(completed_at)
        except ValueError: continue
        if resolved_dt > cutoff_date:
            restored.append(r)
    return restored
