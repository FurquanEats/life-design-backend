from fastapi import APIRouter
from typing import List
from app.models.schemas import ActivityCreate, ActivityResponse
from app.repositories.memory import InMemoryRepository
from app.services.analytics import AnalyticsService

router = APIRouter()

# Dependency Initialization
# Note: In production, use a DI container (e.g., python-dependency-injector)
repository = InMemoryRepository()
analytics_service = AnalyticsService(repository)

@router.post("/activities", response_model=ActivityResponse)
def log_activity(activity: ActivityCreate):
    return repository.add(activity)

@router.get("/dashboard/{goal_id}", response_model=List[ActivityResponse])
def get_dashboard(goal_id: str):
    return repository.get_by_goal(goal_id)

@router.get("/insights/optimization")
def get_optimization_insights():
    return analytics_service.generate_optimization_insights()