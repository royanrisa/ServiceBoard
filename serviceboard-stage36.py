# === Stage 36: Add templates for quickly creating common records ===
# Project: ServiceBoard
class RecordTemplates:
    def __init__(self, db):
        self.db = db

    def create_customer_template(self, name="Template Customer"):
        return {
            "id": None,
            "name": name,
            "email": f"{name.lower().replace(' ', '.')}@example.com",
            "phone": "+1-000-000-0000"
        }

    def create_assignment_template(self, priority="medium", deadline_days=7):
        return {
            "id": None,
            "request_id": None,
            "assigned_to": None,
            "priority": priority,
            "deadline": self._add_days(deadline_days),
            "status": "open"
        }

    def create_resolution_template(self, status="resolved", notes="Issue resolved successfully."):
        return {
            "id": None,
            "assignment_id": None,
            "resolution_date": self._get_today(),
            "status": status,
            "notes": notes
        }

    def _add_days(self, days):
        from datetime import timedelta, date
        today = date.today()
        return (today + timedelta(days=days)).isoformat()

    def _get_today(self):
        from datetime import date
        return date.today().isoformat()
