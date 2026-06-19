# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: ServiceBoard
def validate_customer_name(name):
    if not name.strip() or len(name) > 50:
        raise ValueError("Customer name must be between 1 and 50 characters.")
    return True

def validate_request_id(request_id):
    import re
    pattern = r'^REQ-\d{4}$'
    if not re.match(pattern, request_id.strip()):
        raise ValueError(f"Request ID must match format 'REQ-XXXX'.")
    return True

def validate_priority(priority_str):
    valid_priorities = {'low', 'medium', 'high', 'critical'}
    if priority_str.lower() not in valid_priorities:
        raise ValueError(f"Priority must be one of {valid_priorities}.")
    return priority_str.upper()

def validate_deadline(deadline_str):
    from datetime import datetime, timedelta
    try:
        deadline = datetime.strptime(deadline_str.strip(), '%Y-%m-%d')
        if deadline < datetime.now():
            raise ValueError("Deadline cannot be in the past.")
        return deadline
    except ValueError as e:
        raise ValueError(f"Invalid date format or logic. {e}")

def validate_short_text(text, max_len=200):
    if not text.strip() or len(text) > max_len:
        raise ValueError(f"Text must be between 1 and {max_len} characters.")
    return text.strip()
