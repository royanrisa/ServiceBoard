# === Stage 43: Add CSV import for the primary record type ===
# Project: ServiceBoard
import csv
from pathlib import Path

def load_csv_records(file_path: str, record_class):
    """Load records from a CSV file into a list of objects."""
    path = Path(file_path)
    if not path.exists():
        return []
    
    records = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                obj = record_class(**row)
                records.append(obj)
            except Exception:
                continue  # Skip malformed rows silently
    return records

# Usage example (uncomment to activate):
# customers_from_csv = load_csv_records('customers.csv', Customer)
