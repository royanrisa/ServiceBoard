# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: ServiceBoard
def manage_tags(tags, item):
    if 'tags' not in item: item['tags'] = []
    for t in tags:
        if t not in item['tags']: item['tags'].append(t)
        else: item['tags'].remove(t)
    return item

def get_tag_summary(items, tag=None):
    summary = {'total': len(items), 'by_priority': {}, 'by_deadline_status': {}}
    for i in items:
        p = i.get('priority', 'low')
        d = 'overdue' if i.get('deadline') and datetime.datetime.now() > datetime.datetime.fromisoformat(i['deadline']) else 'ok'
        summary['by_priority'][p] = summary['by_priority'].get(p, 0) + 1
        summary['by_deadline_status'][d] = summary['by_deadline_status'].get(d, 0) + 1
    if tag: filtered = [x for x in items if tag in x.get('tags', [])]; summary['tagged'] = len(filtered); summary['tagged_items'] = filtered
    return summary

from datetime import datetime
