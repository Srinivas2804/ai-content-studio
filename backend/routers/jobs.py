from fastapi import APIRouter, HTTPException
from models.schemas import JobCreate
from models import database as db
import threading, time, random
from datetime import datetime

router = APIRouter()

SAMPLE_CONTENT = {
    "twitter_thread": "Thread: {title}\n\n1/ Here's everything you need to know...\n2/ The key insight is...\n3/ Most people overlook this...\n4/ Actionable takeaway: Start small, iterate fast.\n\nSave this thread!",
    "linkedin_post": "I spent hours distilling this:\n\n{title}\n\nKey lessons:\n- Fundamentals matter more than ever\n- Consistency beats perfection\n- Authenticity wins long-term\n\nBiggest mistake? Waiting until you're 'ready'.\n\nWhat resonated? Comment below!",
    "blog_article": "# {title}\n\n## Introduction\nUnderstanding {title} has never been more critical...\n\n## Key Insights\nThree critical findings reshape how we think about this topic.\n\n## Actionable Steps\n1. Start with fundamentals\n2. Build consistency\n3. Measure what matters\n\n## Conclusion\nThose who act now will lead tomorrow.",
    "newsletter": "Subject: The {title} Breakdown\n\nHey [First Name],\n\nThis week I went deep on {title}.\n\nKey takeaways:\n- Point 1\n- Point 2\n- Point 3\n\nFull breakdown inside...\n\nUntil next week,\nAlex",
    "instagram_caption": "The truth about {title} nobody talks about\n\n- It's not about working harder\n- It's about working smarter\n- The compound effect is REAL\n\nSave this post!\n\n#ContentCreator #AIContent #DigitalMarketing",
}

def simulate_ai_processing(job_id: str):
    def process():
        job = db.get_job(job_id)
        if not job:
            return
        db.update_job(job_id, {"status": "processing"})
        formats = job["formats"]
        total = len(formats)
        for i, fmt in enumerate(formats):
            time.sleep(random.uniform(1.5, 3.0))
            title = job["title"]
            template = SAMPLE_CONTENT.get(fmt["format"], f"Generated {fmt['format']} content for: {title}")
            content = template.replace("{title}", title)
            formats[i] = {
                **fmt, "status": "completed", "content": content,
                "word_count": len(content.split()),
                "created_at": datetime.now().isoformat(),
            }
            progress = int(((i + 1) / total) * 100)
            db.update_job(job_id, {
                "formats": formats, "progress": progress,
                "status": "processing" if progress < 100 else "completed"
            })
        db.update_job(job_id, {"status": "completed", "progress": 100})
    threading.Thread(target=process, daemon=True).start()

@router.get("/")
def list_jobs(user_id: str = "user_demo"):
    return db.get_jobs(user_id)

@router.post("/")
def create_job(body: JobCreate, user_id: str = "user_demo"):
    job = db.create_job({
        "title": body.title, "content_type": body.content_type,
        "source_url": body.source_url, "source_text": body.source_text,
        "formats": body.formats, "user_id": user_id,
    })
    simulate_ai_processing(job["id"])
    return job

@router.get("/{job_id}")
def get_job(job_id: str):
    job = db.get_job(job_id)
    if not job:
        raise HTTPException(404, "Job not found")
    return job

@router.delete("/{job_id}")
def delete_job(job_id: str):
    from models.database import _jobs
    if job_id not in _jobs:
        raise HTTPException(404, "Job not found")
    _jobs.pop(job_id)
    return {"deleted": True}
