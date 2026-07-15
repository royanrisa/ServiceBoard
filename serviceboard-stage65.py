# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: ServiceBoard
def merge_imports(existing, new):
    """Merge a list of new import statements into existing ones, skipping obvious duplicates."""
    merged = []
    seen = set()
    for stmt in existing:
        canonical = _canonical_form(stmt)
        if not canonical or canonical in seen:
            continue
        seen.add(canonical)
        merged.append(stmt)
    for stmt in new:
        canonical = _canonical_form(stmt)
        if canonical and canonical not in seen:
            seen.add(canonical)
            merged.append(stmt)
    return merged


def _canonical_form(stmt):
    """Return a normalised string that identifies the import line."""
    s = stmt.strip()
    s = re.sub(r'\s+', ' ', s)
    if s.startswith('import'):
        # handle `import foo, bar` -> split into per-name entries
        parts = [p.strip().split(',') for p in s.split(';')]
        return tuple(p[0].strip() for p in parts if p)
    elif s.startswith('from'):
        m = re.match(r'from\s+(\S+)\s+import\s+(.*)', s, re.DOTALL)
        if m:
            mod = m.group(1).strip().split('.')[-1]
            names = [n.strip() for n in m.group(2).split(',') if n.strip()]
            return (mod,) + tuple(names)
    else:
        return s
