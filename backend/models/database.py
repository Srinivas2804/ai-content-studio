"""In-memory database simulation. In production replace with PostgreSQL + SQLAlchemy."""
from datetime import datetime, timedelta
import uuid

_users: dict = {}
_jobs: dict = {}


def _seed():
    uid = "user_demo"
    _users[uid] = {
        "id": uid, "name": "Alex Rivera", "email": "alex@contentstudio.ai",
        "password_hash": "hashed_demo", "plan": "pro",
        "created_at": datetime(2025, 11, 1).isoformat(),
    }
    formats_pool = [
        "twitter_thread", "linkedin_post", "blog_article", "newsletter",
        "instagram_caption", "youtube_shorts_script", "email_sequence",
        "seo_summary", "podcast_notes", "quote_cards", "tiktok_script", "facebook_post"
    ]
    sample_jobs = [
        ("How AI is Changing Content Marketing", "podcast", "completed", 100),
        ("The Future of Remote Work", "blog", "completed", 100),
        ("Building a Personal Brand in 2026", "video", "completed", 100),
        ("10 Growth Hacks for SaaS Founders", "article", "processing", 55),
        ("Mental Models for Better Decisions", "podcast", "queued", 0),
    ]
    for i, (title, ctype, status, progress) in enumerate(sample_jobs):
        jid = f"job_{i+1}"
        formats_used = formats_pool[:8] if status == "completed" else formats_pool[:5]
        created = (datetime.now() - timedelta(days=10 - i * 2)).isoformat()
        _jobs[jid] = {
            "id": jid, "title": title, "content_type": ctype,
            "status": status, "progress": progress, "user_id": uid,
            "formats": [
                {
                    "format": f,
                    "status": "completed" if status == "completed" else (
                        "processing" if j == 0 and status == "processing" else "queued"),
                    "content": f"Generated {f.replace('_', ' ')} content for: {title}" if status == "completed" else None,
                    "word_count": 200 + j * 50 if status == "completed" else None,
                    "created_at": created if status == "completed" else None,
                }
                for j, f in enumerate(formats_used)
            ],
            "created_at": created, "updated_at": created,
        }


_seed()


def get_user(user_id: str): return _users.get(user_id)
def get_user_by_email(email: str): return next((u for u in _users.values() if u["email"] == email), None)
def create_user(data: dict):
    uid = f"user_{uuid.uuid4().hex[:8]}"
    _users[uid] = {**data, "id": uid, "plan": "free", "created_at": datetime.now().isoformat()}
    return _users[uid]
def get_jobs(user_id: str): return [j for j in _jobs.values() if j["user_id"] == user_id]
def get_job(job_id: str): return _jobs.get(job_id)
def create_job(data: dict):
    jid = f"job_{uuid.uuid4().hex[:8]}"
    now = datetime.now().isoformat()
    _jobs[jid] = {
        **data, "id": jid, "status": "queued", "progress": 0,
        "created_at": now, "updated_at": now,
        "formats": [
            {"format": f, "status": "queued", "content": None, "word_count": None, "created_at": None}
            for f in data.get("formats", [])
        ]
    }
    return _jobs[jid]
def update_job(job_id: str, updates: dict):
    if job_id in _jobs:
        _jobs[job_id].update({**updates, "updated_at": datetime.now().isoformat()})
    return _jobs.get(job_id)
