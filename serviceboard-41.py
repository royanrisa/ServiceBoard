# === Stage 41: Add plain text import for a simple line-based format ===
# Project: ServiceBoard
from typing import List, Dict, Optional
import re

def parse_line_to_record(line: str) -> Optional[Dict]:
    if not line.strip(): return None
    parts = line.split('|')
    if len(parts) != 6: return None
    try:
        id_, customer, assignee, priority, deadline, history = [p.strip() for p in parts]
        return {
            'id': int(id_),
            'customer': customer,
            'assignee': assignee,
            'priority': int(priority),
            'deadline': deadline,
            'history': history.split(';') if history else []
        }
    except ValueError:
        return None

def load_plain_text_file(filepath: str) -> List[Dict]:
    records = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            record = parse_line_to_record(line)
            if record is not None:
                records.append(record)
    return sorted(records, key=lambda r: r['id'])
