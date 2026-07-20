# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: ServiceBoard
def get_priority_label(priority: int) -> str:
    """Return a human-readable label for a priority level."""
    labels = {1: "Critical", 2: "High", 3: "Medium", 4: "Low"}
    return labels.get(priority, f"Priority-{priority}")


def format_deadline(deadline_str: str) -> tuple[str, str]:
    """Parse a deadline string and return (date_part, time_part)."""
    if not deadline_str or len(deadline_str.split()) != 2:
        raise ValueError("Deadline must be in 'YYYY-MM-DD HH:MM' format")
    date_part, time_part = deadline_str.split()
    return date_part, time_part


def calculate_age_in_days(start_date: str, end_date: str) -> int:
    """Calculate the number of days between two dates (inclusive)."""
    from datetime import datetime, timedelta

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = (end - start).days + 1
    return max(delta, 0)


def truncate_text(text: str, max_length: int) -> str:
    """Truncate text to a maximum length with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def generate_id(prefix: str = "ID", counter: list[int] | None = None) -> str:
    """Generate a unique identifier string with optional auto-increment."""
    if counter is None:
        counter = [0]
    counter[0] += 1
    return f"{prefix}-{counter[0]:04d}"


def validate_priority(priority: int, valid_priorities: list[int]) -> bool:
    """Validate that a priority value is in the allowed set."""
    if not isinstance(priority, int):
        raise TypeError("Priority must be an integer")
    return priority in valid_priorities and 1 <= priority <= 4


def format_resolution_history(resolution: dict) -> str:
    """Format a resolution dictionary into a readable string."""
    parts = [f"Resolved by {resolution.get('agent', 'Unknown')}"]
    if "reason" in resolution:
        parts.append(f"- Reason: {resolution['reason']}")
    if "feedback" in resolution:
        parts.append(f"- Feedback: {resolution['feedback']}")
    return "\n".join(parts)


def calculate_overdue_days(deadline_str: str, current_date: str = None) -> int:
    """Calculate how many days a deadline is overdue."""
    if current_date is None:
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")

    deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
    today = datetime.strptime(current_date, "%Y-%m-%d")
    return max((today - deadline).days, 0)


def normalize_priority_string(priority: str | int) -> int:
    """Convert a string or integer priority to an integer."""
    if isinstance(priority, int):
        return priority
    mapping = {"critical": 1, "high": 2, "medium": 3, "low": 4}
    return mapping.get(str(priority).lower(), 0)


def display_board_summary(boards: dict[str, list[dict]]) -> str:
    """Generate a summary string for all service boards."""
    lines = ["=== Service Board Summary ===", f"Total Boards: {len(boards)}"]
    for board_name, tickets in boards.items():
        open_count = sum(1 for t in tickets if not t.get("resolved"))
        lines.append(f"{board_name}: {open_count} open ticket(s)")
    return "\n".join(lines)
