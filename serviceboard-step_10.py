# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: ServiceBoard
class SearchFilter:
    def __init__(self, data):
        self.data = data
    
    def search(self, query, fields=None):
        if not fields:
            fields = ['customer', 'service_name', 'priority', 'status']
        query_lower = query.lower()
        results = []
        for item in self.data:
            match = False
            for field in fields:
                val = str(item.get(field, '')).lower()
                if query_lower in val:
                    match = True
                    break
            if match:
                results.append(item)
        return results
