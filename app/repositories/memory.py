import uuid
from typing import List
from app.repositories.base import BaseRepository
from app.models.schemas import ActivityCreate, ActivityResponse

class InMemoryRepository(BaseRepository):
    """
    In-memory implementation of the BaseRepository.
    Stores data in a local list structure for prototyping purposes.
    """
    
    def __init__(self):
        self._storage = []

    def add(self, activity: ActivityCreate) -> ActivityResponse:
        # Generate unique identifier (UUID) to simulate DB primary key
        record_id = str(uuid.uuid4())
        
        activity_data = activity.model_dump()
        activity_data["id"] = record_id
        
        saved_activity = ActivityResponse(**activity_data)
        
        self._storage.append(saved_activity)
        return saved_activity

    def get_by_goal(self, goal_id: str) -> List[ActivityResponse]:
        return [act for act in self._storage if act.goal_id == goal_id]
    
    def get_all(self) -> List[ActivityResponse]:
        return self._storage