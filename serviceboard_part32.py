# === Stage 32: Add pagination helpers for long console output ===
# Project: ServiceBoard
def paginate_table(data, columns, page_size=10):
    total_pages = (len(data) + page_size - 1) // page_size if data else 1
    print(f"\n{'='*60}")
    for i in range(total_pages):
        start = i * page_size
        end = min(start + page_size, len(data))
        chunk = data[start:end]
        print(f"Page {i+1}/{total_pages} (rows {start}-{end})")
        if not chunk: break
        for row in chunk:
            line = " | ".join(str(row.get(col, '')) for col in columns)
            print(line)
    print('='*60 + "\n")
