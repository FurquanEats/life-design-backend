from abc import ABC, abstractmethod
from typing import List
from app.models.schemas import ActivityCreate, ActivityResponse

class BaseRepository(ABC):
    """
    Abstract Interface for data persistence.
    
    Decouples the service layer from the underlying storage mechanism,
    allowing for seamless migration from in-memory storage to a SQL/NoSQL database.
    """
    
    @abstractmethod
    def add(self, activity: ActivityCreate) -> ActivityResponse:
        """Persist a new activity record."""
        pass

    @abstractmethod
    def get_by_goal(self, goal_id: str) -> List[ActivityResponse]:
        """Retrieve all activity logs associated with a specific goal."""
        pass
    
    @abstractmethod
    def get_all(self) -> List[ActivityResponse]:
        """Retrieve all records from storage."""
        pass