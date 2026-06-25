# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: ServiceBoard
class ServiceBoardDryRun:
    def __init__(self, board):
        self.board = board
        self.dry_run_mode = False

    def activate(self):
        self.dry_run_mode = True

    def deactivate(self):
        self.dry_run_mode = False

    def _log_action(self, action_type: str, details: dict) -> None:
        if not self.dry_run_mode:
            return
        print(f"[DRY-RUN] {action_type}: {details}")

    def assign_task(self, task_id: int, user_id: int):
        self._log_action("assign", {"task": task_id, "user": user_id})
        # Actual assignment logic omitted for dry-run safety

    def update_priority(self, task_id: int, priority: str):
        self._log_action("update_priority", {"task": task_id, "priority": priority})

    def set_deadline(self, task_id: int, deadline: datetime.datetime):
        self._log_action("set_deadline", {"task": task_id, "deadline": deadline.isoformat()})

    def close_task(self, task_id: int, resolution_notes: str):
        self._log_action("close", {"task": task_id, "notes": resolution_notes[:50] + "..."})
