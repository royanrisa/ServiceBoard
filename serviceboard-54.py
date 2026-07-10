# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: ServiceBoard
def colorize(text, color):
    codes = {"red": "\033[91m", "green": "\033[92m", "yellow": "\033[93m",
             "blue": "\033[94m", "magenta": "\033[95m", "cyan": "\033[96m"}
    return codes.get(color, "") + text + "\033[0m"

class ColoredOutput:
    def __init__(self):
        self.enabled = True

    def set_enabled(self, flag):
        self.enabled = flag

    def print_header(self, title):
        if not self.enabled: return
        print(colorize(title.upper(), "blue"))

    def print_row(self, label, value):
        if not self.enabled:
            print(f"{label}: {value}")
            return
        print(f"  {colorize(label, 'green')} : {value}")
