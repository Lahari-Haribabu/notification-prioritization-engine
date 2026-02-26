from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventCreate(BaseModel):
    user_id: str
    event_type: str
    message: str
    expires_at: Optional[datetime] = None