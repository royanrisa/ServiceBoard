# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: ServiceBoard
import math

def suggest_priority(customer, assignment, deadline):
    score = 0
    if customer.get('risk', 0) > 5:
        score += 30
    else:
        risk_level = customer.get('risk', 0)
        score += int(risk_level / 10 * 10)
    if assignment and assignment.get('assigned_to'):
        assignee = assignment['assigned_to']
        if assignee.get('capacity') < 50:
            score -= 20
        else:
            score -= 10
    else:
        score += 20
    remaining_hours = max(0, (deadline - now()) / 3600)
    deadline_score = min(remaining_hours * 5, 40)
    score += deadline_score
    return 'critical' if score >= 70 else ('high' if score >= 40 else ('medium' if score >= 10 else 'low'))
