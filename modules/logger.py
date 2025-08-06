# logger.py

import pandas as pd
from datetime import datetime

LOG_FILE = "data/proof_log.csv"

def log_attempt(user_text, matched_axioms):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a new entry as a DataFrame
    entry = pd.DataFrame([{
        "timestamp": timestamp,
        "proof": user_text,
        "matched_axioms": ", ".join(matched_axioms)
    }])

    try:
        # Read existing log file
        df = pd.read_csv(LOG_FILE)
        # Concatenate new entry
        df = pd.concat([df, entry], ignore_index=True)
    except FileNotFoundError:
        # If log file doesn't exist, start with the new entry
        df = entry

    # Save updated log
    df.to_csv(LOG_FILE, index=False)

# import pandas as pd
# from datetime import datetime

# LOG_FILE = "data/proof_log.csv"

# def log_attempt(user_text, matched_axioms):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     entry = {
#         "timestamp": timestamp,
#         "proof": user_text,
#         "matched_axioms": ", ".join(matched_axioms)
#     }

#     try:
#         df = pd.read_csv(LOG_FILE)
#         df = df.append(entry, ignore_index=True)
#     except FileNotFoundError:
#         df = pd.DataFrame([entry])

#     df.to_csv(LOG_FILE, index=False)
