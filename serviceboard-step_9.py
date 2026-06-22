# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: ServiceBoard
class SortableBoard(Board):
    def sort_requests(self, key="last_update", reverse=False):
        """Sort requests by title, date, priority, or last update."""
        if key == "title":
            return sorted(self.requests, key=lambda r: (r.title.lower(), -int(r.priority)))
        elif key == "date":
            return sorted(self.requests, key=lambda r: r.created_at)
        elif key == "priority":
            return sorted(self.requests, key=lambda r: int(r.priority), reverse=True)
        elif key == "last_update":
            return sorted(self.requests, key=lambda r: r.last_updated_at or r.created_at)
        else:
            raise ValueError(f"Unsupported sort key: {key}")

    def get_sorted_requests(self):
        """Return requests sorted by last update time by default."""
        try:
            return self.sort_requests("last_update")
        except Exception as e:
            print(f"Sorting error: {e}")
            return self.requests
