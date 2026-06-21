# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: ServiceBoard
class FilterServiceBoard:
    def __init__(self, board):
        self.board = board

    def filter_requests(self, status=None, category=None, owner=None, tag=None):
        filtered = []
        for req in self.board.requests:
            if status and req.status != status: continue
            if category and req.category != category: continue
            if owner and req.owner_id != owner: continue
            if tag and not any(req.tags.get(t) == True for t in tag): continue
            filtered.append(req)
        return filtered

    def filter_by_deadline(self, before=None, after=None):
        filtered = []
        now = datetime.now()
        for req in self.board.requests:
            if before and req.deadline > before: continue
            if after and req.deadline < after: continue
            filtered.append(req)
        return filtered

    def filter_by_priority(self, min_level=1):
        filtered = []
        for req in self.board.requests:
            if req.priority >= min_level:
                filtered.append(req)
        return filtered
