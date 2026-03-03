from fastapi import APIRouter
from models import database as db
from datetime import datetime, timedelta
import random

router = APIRouter()

@router.get("/summary")
def get_summary(user_id: str = "user_demo"):
    jobs = db.get_jobs(user_id)
    total = len(jobs)
    completed = sum(1 for j in jobs if j["status"] == "completed")
    total_formats = sum(len(j["formats"]) for j in jobs if j["status"] == "completed")
    by_status = {"queued": 0, "processing": 0, "completed": 0, "failed": 0}
    for j in jobs:
        by_status[j["status"]] = by_status.get(j["status"], 0) + 1
    monthly = []
    for m in range(5, 0, -1):
        dt = datetime.now() - timedelta(days=m * 30)
        monthly.append({
            "month": dt.strftime("%b %Y"),
            "jobs": random.randint(3, 12),
            "formats": random.randint(20, 90),
        })
    return {
        "total_jobs": total,
        "completed_jobs": completed,
        "total_formats_generated": total_formats,
        "formats_this_month": random.randint(15, 45),
        "avg_completion_time_minutes": round(random.uniform(2.5, 8.0), 1),
        "top_format": "twitter_thread",
        "jobs_by_status": by_status,
        "monthly_usage": monthly,
    }
