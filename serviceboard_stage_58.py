# === Stage 58: Add bulk update behavior for selected records ===
# Project: ServiceBoard
def bulk_update(selected_ids, updates):
    """Update multiple records at once based on their IDs."""
    if len(selected_ids) != len(updates):
        raise ValueError("Number of selected IDs must match number of updates")
    
    result = []
    for sid, update in zip(selected_ids, updates):
        record = _find_record(sid)
        if record is None:
            print(f"Warning: Record with ID {sid} not found and was skipped.")
            continue
        
        # Apply only the keys present in 'update' to avoid overwriting defaults
        for key, value in update.items():
            if hasattr(record, key):
                setattr(record, key, value)
        
        record._updated_at = datetime.now()
        result.append(record)
    
    return result
