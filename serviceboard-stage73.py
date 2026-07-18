# === Stage 73: Add a lightweight HTML report export ===
# Project: ServiceBoard
import json, os

def export_report(board_file):
    with open(board_file) as f:
        data = json.load(f)
    lines = []
    for cust in data["customers"]:
        lines.append(f"Customer: {cust['name']}")
        for req in cust.get("requests", []):
            lines.append(f"  Request #{req['id']}: {req['title']} [{req['status']}] - Priority: {req['priority']}")
    with open(board_file.replace(".json", ".txt"), "w") as f:
        f.write("\n".join(lines))
