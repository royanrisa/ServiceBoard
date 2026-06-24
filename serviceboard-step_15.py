# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: ServiceBoard
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, text_command):
        if not text_command.strip():
            return None
        command_name = text_command.split()[0].lower()
        args = text_command.split()[1:] if len(text_command.split()) > 1 else []
        handler = self.handlers.get(command_name)
        if handler:
            try:
                result = handler(*args)
                return f"Executed '{command_name}': {result}"
            except Exception as e:
                return f"Error executing '{command_name}': {e}"
        return f"Unknown command: '{text_command}' (try 'help')"

    def register(self, name, handler):
        self.handlers[name.lower()] = handler
