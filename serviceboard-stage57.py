# === Stage 57: Add structured result objects for command handlers ===
# Project: ServiceBoard
class Result:
    def __init__(self, success=True, message="", data=None, errors=None):
        self.success = success
        self.message = message
        self.data = data
        self.errors = errors or []

    @classmethod
    def ok(cls, data=None, msg=""):
        return cls(success=True, message=msg, data=data)

    @classmethod
    def error(cls, msg="", errors=None):
        return cls(success=False, message=msg, errors=errors or [])

    def to_dict(self):
        result = {"success": self.success, "message": self.message}
        if self.data is not None:
            result["data"] = self.data
        if self.errors:
            result["errors"] = self.errors
        return result
