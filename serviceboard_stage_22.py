# === Stage 22: Add favorite records and quick favorite listing ===
# Project: ServiceBoard
class FavoriteManager:
    def __init__(self, db):
        self.db = db
    
    def toggle_favorite(self, request_id):
        if request_id in self.db['favorites']:
            del self.db['favorites'][request_id]
        else:
            self.db['favorites'][request_id] = True
        return len(self.db['favorites'])
    
    def get_favorites_summary(self):
        count = 0
        for req_id, is_fav in self.db['favorites'].items():
            if is_fav:
                req = self.db['requests'][req_id]
                print(f"[★] {req.get('customer', 'Unknown')}: {req.get('service_type', 'Service')}")
                count += 1
        return count
