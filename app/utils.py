from datetime import datetime

def is_expired(event):
    if "expires_at" in event.payload:
        return datetime.utcnow() > datetime.fromisoformat(event.payload["expires_at"])
    return False