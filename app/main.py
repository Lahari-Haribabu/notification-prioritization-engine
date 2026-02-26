from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app.models import Event
from app.schemas import EventCreate
from app.decision_engine import decide
from app.audit_logger import log_decision

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/events")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    decision, reason = decide(db, event)

    db_event = Event(
        user_id=event.user_id,
        event_type=event.event_type,
        message=event.message,
        decision=decision
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    log_decision(db, db_event.id, decision, reason)

    return {
        "id": db_event.id,
        "decision": decision,
        "reason": reason
    }

@app.get("/")
def health():
    return {"status": "running"}