from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal

# Restrict activity types to domain-specific categories
ActivityType = Literal["Learning", "Health", "Work", "Mindfulness"]

class ActivityCreate(BaseModel):
    """
    Input payload for logging a new user activity.
    """
    goal_id: str
    activity_type: ActivityType
    # Enforce positive values for data integrity
    value: float = Field(..., gt=0, description="Duration in minutes or repetition count")
    timestamp: datetime

class ActivityResponse(ActivityCreate):
    """
    Output representation of a stored activity, including the system-generated ID.
    """
    id: str

    class Config:
        from_attributes = True