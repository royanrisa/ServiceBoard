# === Stage 60: Add saved views for frequently used filters ===
# Project: ServiceBoard
class SavedView:
    """A named filter preset that users can toggle on/off."""

    def __init__(self, name, filters=None):
        self.name = name
        self._filters = filters or {}  # e.g. {"priority": "high", "status": "open"}

    @property
    def is_active(self):
        return bool(self._filters)

    def apply(self, board):
        """Apply saved view to the board's display."""
        for key, value in self._filters.items():
            if hasattr(board, 'filter_by'):
                getattr(board, f'filter_{key}')(value)

    @staticmethod
    def create(name, filters=None):
        return SavedView(name, filters)

    def __repr__(self):
        status = "Active" if self.is_active else "Inactive"
        return f"<SavedView '{self.name}' [{status}]>"
