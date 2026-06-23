# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: ServiceBoard
import json, sys

def load_json_safe(path):
    try:
        with open(path) as f:
            return json.load(f), None
    except FileNotFoundError:
        print(f"[WARN] File {path} not found.")
        return {}, None
    except json.JSONDecodeError as e:
        print(f"[ERROR] Malformed JSON in {path}: {e}")
        sys.exit(1)

def parse_request(raw):
    try:
        data = json.loads(raw.strip())
        if isinstance(data, dict) and "id" in data and "customer" in data:
            return data
        print("[WARN] Invalid request structure.")
        return None
    except Exception as e:
        print(f"[ERROR] Parse error for line {e}.")
        return None

if __name__ == "__main__":
    records = []
    with open("requests.json", "r") as f:
        for i, raw in enumerate(f, 1):
            rec = parse_request(raw)
            if rec:
                records.append(rec)
    print(f"[OK] Loaded {len(records)} valid requests.")
