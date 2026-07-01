# === Stage 34: Add support for multiple local user profiles ===
# Project: ServiceBoard
from pathlib import Path
import json, uuid, hashlib

class User:
    def __init__(self, name): self.name = name; self.id = str(uuid.uuid4())[:8]
    def hash_password(self, pwd): return hashlib.sha256(f"{self.id}:{pwd}".encode()).hexdigest()
    def verify(self, pwd): return self.hash_password(pwd) == self._password

class UserStore:
    def __init__(self, path="users.json"):
        self.path = Path(path); self.data = {}
        if self.path.exists(): self.load()
    
    def load(self):
        try: data = json.loads(self.path.read_text()); [self.add(u["name"], u["password"]) for u in data]
        except: pass
    
    def add(self, name, pwd):
        user = User(name); user._password = self.hash_password(pwd)
        if not any(u.name == name for u in self.data.values()): self.data[name] = {"id": user.id, "password": user._password}
        else: raise ValueError(f"User {name} already exists")
    
    def login(self, name, pwd):
        try: return UserStore.load().data.get(name) if (u := next((u for n,u in self.data.items() if u["id"] == name), None)) and u["password"] == self.hash_password(pwd) else None
        except: pass
    
    def save(self): json.dump(list(self.data.values()), open(self.path, "w"), indent=2)
