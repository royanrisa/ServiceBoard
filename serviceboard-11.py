# === Stage 11: Add JSON export for the current application state ===
# Project: ServiceBoard
def export_state_to_json(data, filename="state.json"):
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"State exported to {filename}")
