from datetime import datetime
from app.dedupe_engine import is_duplicate
from app.fatigue_engine import is_fatigued
from app.rule_engine import apply_priority_rules

def decide(db, event):
    if event.expires_at and event.expires_at < datetime.utcnow():
        return "Never", "Expired notification"

    if is_duplicate(db, event):
        return "Never", "Duplicate notification"

    rule_decision, rule_reason = apply_priority_rules(event)
    if rule_decision:
        return rule_decision, rule_reason

    if is_fatigued(db, event.user_id):
        return "Later", "User fatigue threshold exceeded"

    return "Now", "Default delivery"