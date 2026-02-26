from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    event_type = Column(String)
    message = Column(Text)
    decision = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    decision = Column(String)
    reason = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)