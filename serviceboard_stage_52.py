# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: ServiceBoard
def format_ticket_summary(ticket: Ticket) -> str:
    """Return a one-line summary of a ticket's status, priority, customer, and deadline."""
    return (f"#{ticket.id} | {ticket.customer.name} | "
            f"{PRIORITY_LABELS.get(ticket.priority)} | "
            f"[{ticket.status}] | due {ticket.deadline}")


def format_resolution_history(resolutions: list[Resolution]) -> str:
    """Return a multi-line string listing each resolution's action and timestamp."""
    lines = [f"=== Resolution History ==="]
    for r in resolutions:
        lines.append(f"- [{r.timestamp}] {r.action} by {r.assigned_to}")
    return "\n".join(lines)


def build_escalation_prompt(ticket: Ticket, history: list[Resolution]) -> str:
    """Return a prompt string suggesting the next human action based on ticket age and history."""
    age = (ticket.deadline - datetime.now()).total_seconds() / 3600 if ticket.deadline else float('inf')
    open_resolutions = [r for r in history if r.action == "resolved"]
    return (f"Ticket #{ticket.id} from {ticket.customer.name} is approaching its deadline "
            f"({age:.1f}h remaining). It has been resolved {len(open_resolutions)} times. "
            f"Suggested next step: reassign or escalate.")


def export_board_csv(board: Board) -> str:
    """Return a CSV string containing all tickets and their resolution history on the board."""
    import csv, io
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["ticket_id", "customer", "priority", "status", "deadline"])
    for t in board.tickets:
        writer.writerow([t.id, t.customer.name, PRIORITY_LABELS.get(t.priority), t.status, t.deadline])
    return buf.getvalue()


def print_board_dashboard(board: Board) -> None:
    """Print a formatted dashboard showing ticket counts by status and priority distribution."""
    from collections import Counter
    status_counts = Counter(t.status for t in board.tickets)
    priority_counts = Counter(PRIORITY_LABELS.get(t.priority, "unknown") for t in board.tickets)
    print("\n=== ServiceBoard Dashboard ===")
    print(f"Total tickets: {len(board.tickets)}")
    print("By status:")
    for s, c in sorted(status_counts.items()):
        print(f"  - {s}: {c}")
    print("By priority:")
    for p, c in sorted(priority_counts.items()):
        print(f"  - {p}: {c}")


def merge_resolutions(ticket: Ticket, resolution: Resolution) -> None:
    """Append a new resolution to the ticket's history list without replacing existing entries."""
    ticket.resolutions.append(resolution)


def generate_report(board: Board, export_path: str | None = None) -> str:
    """Generate and optionally save a full board report as plain text; return the report string."""
    lines = [f"ServiceBoard Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}", "=" * 50]
    for t in board.tickets:
        history_str = "\n".join(f"- {r.action} at {r.timestamp}" for r in t.resolutions)
        lines.append(f"Ticket #{t.id}: {t.customer.name} [{PRIORITY_LABELS.get(t.priority)}]")
        lines.append(f"  Status: {t.status}, Deadline: {t.deadline}")
        if history_str:
            lines.append(f"  History:\n{history_str}")
        else:
            lines.append("  No resolutions yet.")
    report = "\n".join(lines)
    if export_path:
        with open(export_path, "w") as f:
            f.write(report)
    return report


def validate_ticket_data(ticket: Ticket) -> list[str]:
    """Return a list of validation errors for the given ticket; empty list means valid."""
    errors = []
    if not ticket.customer or not ticket.customer.name:
        errors.append("Customer name is required.")
    if ticket.priority not in PRIORITY_LABELS:
        errors.append(f"Invalid priority '{ticket.priority}'.")
    if ticket.deadline and ticket.deadline < datetime.now():
        errors.append("Deadline must be in the future or None.")
    return errors


def display_ticket_card(ticket: Ticket) -> str:
    """Return a visually formatted card string for displaying a single ticket."""
    border = "+" + "-" * 40 + "+"
    inner = (f"| #{ticket.id} | {ticket.customer.name:<25} "
             f"| {PRIORITY_LABELS.get(ticket.priority):<10} | "
             f"[{ticket.status}] | {ticket.deadline or 'No deadline'}")
    return "\n".join([border, inner, border])


def sort_tickets_by_deadline(board: Board) -> list[Ticket]:
    """Return a new list of tickets sorted by deadline ascending; None deadlines go last."""
    def _sort_key(t):
        if t.deadline is None:
            return datetime.max
        return t.deadline
    return sorted(board.tickets, key=_sort_key)


def count_pending_deadlines(board: Board, hours_ahead: int = 24) -> list[Ticket]:
    """Return tickets whose deadline is within the given number of hours from now."""
    cutoff = datetime.now() + timedelta(hours=hours_ahead)
    return [t for t in board.tickets if t.deadline and t.deadline <= cutoff]


def clear_resolved_tickets(board: Board) -> list[Ticket]:
    """Return a new board copy with only unresolved tickets; print how many were removed."""
    remaining = [t for t in board.tickets if t.status != "resolved"]
    removed = len(board.tickets) - len(remaining)
    print(f"Removed {removed} resolved ticket(s). Remaining: {len(remaining)}")
    return Board(tickets=remaining, resolutions=[])
