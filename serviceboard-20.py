# === Stage 20: Add duplicate detection for newly created records ===
# Project: ServiceBoard
from typing import Optional, List
import hashlib

def find_duplicates(records: List[dict], new_record: dict) -> bool:
    """Check if a record with same customer and priority exists."""
    key = f"{new_record.get('customer_name')}|{new_record.get('priority')}"
    for r in records:
        if (r.get("customer_name") == new_record.get("customer_name") and 
            r.get("priority") == new_record.get("priority")):
            return True
    return False

def get_duplicate_hash(records: List[dict], new_record: dict) -> Optional[str]:
    """Generate a unique hash for the record to detect duplicates later."""
    content = f"{new_record.get('customer_name')}{new_record.get('request_date')}|{new_record.get('priority')}"
    return hashlib.md5(content.encode()).hexdigest()[:8]

def validate_new_request(records: List[dict], new_request: dict) -> tuple[bool, Optional[str]]:
    """Validate a new request against existing records. Returns (is_valid, duplicate_hash)."""
    if find_duplicates(records, new_request):
        return False, get_duplicate_hash(records, new_request)
    hash_val = get_duplicate_hash([], new_request)
    return True, hash_val
