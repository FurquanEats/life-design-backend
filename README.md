# Life Design Backend Service

A Python-based microservice designed to track user growth, calculate consistency scores, and provide AI-driven wellness optimization. Built with **FastAPI**, this project demonstrates a scalable, production-ready architecture using the **Repository Pattern**.

<br>

## Features

- **Growth Journal**: Log activities across different categories (Learning, Health, Work).
- **Analytics Engine**: Automatically calculates a "Consistency Index" (0.0 - 1.0) based on streak logic.
- **Smart Alerts**: Detects imbalances (e.g., High Learning vs. Low Health) and issues wellness warnings.
- **Modular Architecture**: Clean separation of concerns between API, Service Layer, and Data Persistence.

## Tech Stack

- **Framework**: FastAPI (Python 3.12+)
- **Validation**: Pydantic
- **Architecture**: Service-Repository Pattern
- **Storage**: In-Memory (Swappable Interface)

<br>

## Technical Rationale (Scalability & Efficiency)

### Architecture Decisions
I structured the application using a **Service-Repository Pattern** to ensure modularity.
- **Repositories**: I defined an abstract `BaseRepository` interface. This satisfies the requirement to allow swapping the In-Memory list for a real database (PostgreSQL/MongoDB) in the future without changing business logic.
- **Services**: The `AnalyticsService` encapsulates all business rules, keeping the API routes clean.

### Logic Efficiency
To ensure the **Consistency Score** logic stays efficient as logs grow (O(N)):
1.  I fetch raw logs and immediately extract/sort unique dates.
2.  I iterate through the sorted dates once to calculate streaks, avoiding expensive nested loops.
3.  Aggregations for the "Wellness Warning" are filtered by a time window (last 7 days) before processing, ensuring real-time performance.

<br>

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/FurquanEats/life-design-backend
   cd life-design-backend
   ```

2. **Set up the environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the server**:
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Test the API**:
   Open http://127.0.0.1:8000/docs in your browser to use the Swagger UI.

<br>

## Testing Guide (Quick Start)

You can test the API using the Swagger UI at `/docs` or via `curl`/Postman.

### 1. Log an Activity (Create Data)
**Endpoint:** `POST /activities`

**JSON Body:**
```json
{
  "goal_id": "goal_1",
  "activity_type": "Learning",
  "value": 60,
  "timestamp": "2026-01-14T10:00:00"
}
```

### 2. Check Dashboard (View History)
**Endpoint:** `GET /dashboard/{goal_id}`

**Example URL:** `/dashboard/goal_1`

**Response:**
```json
[
  {
    "goal_id": "goal_1",
    "activity_type": "Learning",
    "value": 60,
    "timestamp": "2026-01-14T10:00:00",
    "id": "uuid-string-here"
  }
]
```

### 3. Get Optimization Insights (AI Logic)
**Endpoint:** `GET /insights/optimization`

**Response:**
```json
{
  "consistency_score": 0.14,
  "wellness_warning": true,
  "recommendation": "Rebalance your growth plan: High learning detected with low physical wellness."
}
```