# === Stage 13: Add file save support using a configurable path ===
# Project: ServiceBoard
import os, json, sys
from pathlib import Path

def get_save_path():
    base = Path(os.environ.get('SERVICEBOARD_DATA_DIR', '.')) / 'data'
    base.mkdir(parents=True, exist_ok=True)
    return str(base / 'board.json')

class ServiceBoard:
    def __init__(self):
        self.path = get_save_path()
        self.data = []
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
            except (json.JSONDecodeError, IOError):
                pass

    def add_request(self, customer, assignment, priority, deadline, history=None):
        entry = {
            'customer': customer,
            'assignment': assignment,
            'priority': int(priority),
            'deadline': deadline,
            'history': history or []
        }
        self.data.append(entry)
        return self.save()

    def save(self):
        try:
            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
            return True
        except IOError as e:
            print(f"Error saving to {self.path}: {e}")
            return False

    def get_requests(self):
        return self.data
