from datetime import datetime, timedelta
from app.models import Event

def is_fatigued(db, user_id):
    one_hour_ago = datetime.utcnow() - timedelta(hours=1)

    count = db.query(Event).filter(
        Event.user_id == user_id,
        Event.created_at >= one_hour_ago
    ).count()

    return count >= 5