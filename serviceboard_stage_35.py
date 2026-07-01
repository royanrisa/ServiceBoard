# === Stage 35: Add active user switching and user-specific records ===
# Project: ServiceBoard
class UserContext:
    def __init__(self, name): self.name = name
    def switch(self, new_name): self.name = new_name
    def get_records(self, board): return [r for r in board.records if r.customer == self.name] or []
    def add_record(self, board, customer, request_type, priority, deadline):
        record = {'id': len(board.records) + 1, 'customer': customer, 'type': request_type, 'priority': priority, 'deadline': deadline}
        board.records.append(record)
        return record

def run_board_demo():
    from datetime import date, timedelta
    today = date.today()
    board = {'records': []}
    ctx = UserContext("Alice")
    ctx.switch("Bob"); bob_records = ctx.get_records(board); print(f"Bob sees {len(bob_records)} records")
    ctx.add_record(board, "Client A", "Network Down", 1, today + timedelta(days=2))
    ctx.add_record(board, "Client B", "Login Issue", 3, today + timedelta(days=5))
    alice_records = UserContext("Alice").get_records(board); print(f"Alice sees {len(alice_records)} records")
