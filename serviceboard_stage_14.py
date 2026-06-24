# === Stage 14: Add file load support with fallback demo data ===
# Project: ServiceBoard
import json, os

def load_or_demo(data_file):
    try:
        with open(data_file) as f: return json.load(f)
    except FileNotFoundError:
        demo = {"requests": [], "customers": []}
        if not os.path.exists(os.path.dirname(data_file)):
            os.makedirs(os.path.dirname(data_file))
        with open(data_file, 'w') as f: json.dump(demo, f)
        return demo
