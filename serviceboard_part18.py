# === Stage 18: Add an activity log with timestamps and action names ===
# Project: ServiceBoard
class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action_name: str, user: str, timestamp=None) -> None:
        if timestamp is None:
            from datetime import datetime
            timestamp = datetime.now()
        entry = {
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "action": action_name,
            "user": user
        }
        self.entries.append(entry)

    def get_history(self) -> list:
        return sorted(self.entries, key=lambda x: x["timestamp"], reverse=True)
