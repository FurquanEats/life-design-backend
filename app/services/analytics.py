from datetime import datetime, timedelta
from typing import List, Dict, Any
from app.repositories.base import BaseRepository
from app.models.schemas import ActivityResponse

class AnalyticsService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def _calculate_streak(self, activities: List[ActivityResponse]) -> float:
        """
        Calculates consistency index (0.0 - 1.0) based on consecutive active days.
        """
        if not activities:
            return 0.0

        dates = sorted({act.timestamp.date() for act in activities})
        
        max_streak = 0
        current_streak = 0
        previous_date = None

        for date in dates:
            if previous_date is None:
                current_streak = 1
            elif date == previous_date + timedelta(days=1):
                current_streak += 1
            else:
                current_streak = 1
            
            max_streak = max(max_streak, current_streak)
            previous_date = date

        # Normalization: 7-day streak = 1.0 score
        return min(max_streak / 7.0, 1.0)

    def generate_optimization_insights(self) -> Dict[str, Any]:
        """
        Evaluates user data against health thresholds and balance logic.
        """
        all_activities = self.repository.get_all()
        
        # Metric 1: Consistency
        consistency_score = self._calculate_streak(all_activities)

        # Metric 2: Weekly Aggregations
        one_week_ago = datetime.now() - timedelta(days=7)
        recent_activities = [a for a in all_activities if a.timestamp >= one_week_ago]

        health_minutes = sum(a.value for a in recent_activities if a.activity_type == "Health")
        learning_minutes = sum(a.value for a in recent_activities if a.activity_type == "Learning")

        response = {
            "consistency_score": round(consistency_score, 2),
            "wellness_warning": False,
            "recommendation": "Maintain your current balance."
        }

        # Rule: Minimum Health Threshold (150 mins/week)
        if health_minutes < 150:
            response["wellness_warning"] = True
        
        # Rule: Balance Check (High Learning vs Low Health)
        if learning_minutes > 300 and health_minutes < 150:
            response["recommendation"] = "Rebalance your growth plan: High learning detected with low physical wellness."

        return response