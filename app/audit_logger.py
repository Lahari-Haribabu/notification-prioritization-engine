from app.models import AuditLog

def log_decision(db, event_id, decision, reason):
    log = AuditLog(
        event_id=event_id,
        decision=decision,
        reason=reason
    )
    db.add(log)
    db.commit()