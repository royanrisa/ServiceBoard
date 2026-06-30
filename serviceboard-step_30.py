# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: ServiceBoard
def parse_date(date_str: str) -> datetime.date | None:
    """Parse date string returning None on failure with clear error."""
    if not date_str.strip():
        raise ValueError("Empty date string provided.")
    
    formats = [
        "%Y-%m-%d",      # 2023-10-27
        "%d.%m.%Y",      # 27.10.2023
        "%d/%m/%Y",      # 27/10/2023
        "%B %d, %Y",     # October 27, 2023
    ]
    
    for fmt in formats:
        try:
            return datetime.date.fromtimestamp(
                time.mktime(datetime.datetime.strptime(date_str.strip(), fmt).timetuple())
            )
        except ValueError:
            continue
    
    raise ValueError(f"Unable to parse date '{date_str}'. Supported formats: {', '.join(formats)}")
