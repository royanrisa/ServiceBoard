# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: ServiceBoard
def clear_state(self):
        """Reset board to initial conditions after confirmation."""
        if not self._cleared:
            print("State has unsaved changes. Clearing will discard them.")
            confirm = input("Confirm? [y/N]: ").strip().lower()
            if confirm != "y":
                return
        self.customers.clear()
        self.assignments.clear()
        self.priorities.clear()
        self.deadlines.clear()
        self.resolution_history.clear()
        self._cleared = True
        print("Board state cleared.")
