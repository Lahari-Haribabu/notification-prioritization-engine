from datetime import datetime, timedelta
from app.models import Event

def is_duplicate(db, event):
    five_min_ago = datetime.utcnow() - timedelta(minutes=5)

    existing = db.query(Event).filter(
        Event.user_id == event.user_id,
        Event.message == event.message,
        Event.created_at >= five_min_ago
    ).first()

    return existing is not None