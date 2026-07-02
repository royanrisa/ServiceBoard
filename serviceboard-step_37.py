# === Stage 37: Add recommendations for the next useful action ===
# Project: ServiceBoard
class ActionRecommender:
    def __init__(self, board):
        self.board = board
        self.history_window = 30

    def get_next_action(self, user_id=None):
        now = datetime.now()
        candidates = []
        
        for req in self.board.requests.values():
            if not req.resolved:
                urgency = 0.5
                
                if req.deadline and (req.deadline - now).total_seconds() < 86400 * 3:
                    urgency += 1.0
                elif req.priority == 'high':
                    urgency += 0.7
                    
                if not req.assignee or req.assignee != user_id:
                    candidates.append((urgency, req))

        if not candidates:
            return "No urgent actions required."

        candidates.sort(key=lambda x: x[0], reverse=True)
        top_req = candidates[0][1]

        if top_req.deadline and (top_req.deadline - now).total_seconds() < 3600:
            return f"URGENT: Complete request #{top_req.id} for {top_req.customer_name} before deadline."
        
        if not top_req.assignee or top_req.assignee != user_id:
            return f"Assign request #{top_req.id} to yourself or another available agent."

        recent_actions = [h['action'] for h in self.board.history[-self.history_window:]]
        common_actions = set(recent_actions) if len(recent_actions) > 1 else None
        
        if top_req.resolution_history and not any('escalated' in str(h) for h in top_req.resolution_history):
            return f"Review request #{top_req.id} resolution notes before closing."

        return f"Focus on high-priority items: {', '.join(f'Request #{r.id}' for r, _ in candidates[:3])}"
