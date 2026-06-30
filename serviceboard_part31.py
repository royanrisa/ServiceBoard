# === Stage 31: Add compact table rendering for long lists ===
# Project: ServiceBoard
def render_compact_table(data, columns):
    if not data: return ""
    width = max(len(str(col)) for col in columns) + 2
    header = " | ".join(f"{c:<{width}}" for c in columns).upper()
    line = "-" * len(header)
    rows = []
    for item in data[:10]:
        row_parts = [str(item.get(col, "")) for col in columns]
        rows.append(" | ".join(r.ljust(width) for r in row_parts))
    if len(data) > 10:
        rows[-1] += "..."
    return "\n".join([header, line] + rows)
