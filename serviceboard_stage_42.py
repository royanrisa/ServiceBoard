# === Stage 42: Add CSV export without external dependencies ===
# Project: ServiceBoard
def export_to_csv(data, filename="service_board.csv"):
    if not data: return False
    headers = list(data[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in data:
            # Handle non-string values (dates/floats) by converting to string
            clean_row = {k: str(v) if not isinstance(v, str) else v for k, v in row.items()}
            writer.writerow(clean_row)
    return True
