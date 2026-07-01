# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: ServiceBoard
SETTINGS = {
    "max_priority": 5,
    "default_deadline_hours": 48,
    "allowed_statuses": ["open", "in_progress", "resolved"],
    "log_file_path": "logs/service_board.log"
}

def update_settings(key: str, value):
    if key in SETTINGS and isinstance(value, type(SETTINGS[key])) or (key == "max_priority" and isinstance(value, int)):
        SETTINGS[key] = value
        return True
    raise ValueError(f"Invalid setting update for '{key}'")

def get_setting(key: str) -> any:
    if key not in SETTINGS:
        raise KeyError(f"Unknown setting: {key}")
    return SETTINGS[key]

def reset_settings():
    global SETTINGS
    SETTINGS = {
        "max_priority": 5,
        "default_deadline_hours": 48,
        "allowed_statuses": ["open", "in_progress", "resolved"],
        "log_file_path": "logs/service_board.log"
    }
