from datetime import datetime
from constants import LOG_FILE, ERROR_LOG_FILE

def log_event(event_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] EVENT: {event_text}\n")

def log_error(error_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ERROR_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] ERROR: {error_text}\n")
