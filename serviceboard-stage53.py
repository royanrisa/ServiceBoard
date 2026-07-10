# === Stage 53: Add command help text and usage examples ===
# Project: ServiceBoard
def show_help():
    """Print usage examples and command help for ServiceBoard."""
    print("ServiceBoard - Service Request Board")
    print("=" * 40)
    print(f"Usage: python service_board.py <command> [options]")
    print()
    print("Commands:")
    print("  add-customer     Add a new customer to the board")
    print("  list-customers   List all customers with their priorities and deadlines")
    print("  assign-ticket    Assign an unresolved ticket to a technician")
    print("  update-priority  Change priority of a ticket (low, medium, high)")
    print("  show-deadlines   Display upcoming deadlines in order")
    print("  resolve-ticket   Mark a ticket as resolved with notes")
    print("  history          Show resolution history for all tickets")
    print()
    print("Examples:")
    print("  python service_board.py add-customer --name Alice --email alice@example.com")
    print("  python service_board.py list-customers")
    print("  python service_board.py assign-ticket --ticket-id T-001 --tech John")
    print("  python service_board.py update-priority --ticket-id T-002 --priority high")
    print("  python service_board.py show-deadlines")
    print("  python service_board.py resolve-ticket --ticket-id T-003 --note \"Fixed by patch v1.2\"")
