import pandas as pd
from datetime import datetime

LOG_FILE = "data/proof_log.csv"

def log_attempt(user_text, matched_axioms):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "timestamp": timestamp,
        "proof": user_text,
        "matched_axioms": ", ".join(matched_axioms)
    }

    try:
        df = pd.read_csv(LOG_FILE)
        df = df.append(entry, ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([entry])

    df.to_csv(LOG_FILE, index=False)
