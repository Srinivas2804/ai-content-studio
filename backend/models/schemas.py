from pydantic import BaseModel, EmailStr
from typing import Optional, List
from enum import Enum
from datetime import datetime


class ContentType(str, Enum):
    podcast = "podcast"
    blog = "blog"
    video = "video"
    article = "article"


class JobStatus(str, Enum):
    queued = "queued"
    processing = "processing"
    completed = "completed"
    failed = "failed"


class OutputFormat(str, Enum):
    twitter_thread = "twitter_thread"
    linkedin_post = "linkedin_post"
    blog_article = "blog_article"
    newsletter = "newsletter"
    instagram_caption = "instagram_caption"
    youtube_shorts_script = "youtube_shorts_script"
    email_sequence = "email_sequence"
    seo_summary = "seo_summary"
    podcast_notes = "podcast_notes"
    quote_cards = "quote_cards"
    tiktok_script = "tiktok_script"
    facebook_post = "facebook_post"


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class JobCreate(BaseModel):
    title: str
    content_type: ContentType
    source_url: Optional[str] = None
    source_text: Optional[str] = None
    formats: List[OutputFormat]


class FormatResult(BaseModel):
    format: OutputFormat
    status: JobStatus
    content: Optional[str] = None
    word_count: Optional[int] = None
    created_at: Optional[datetime] = None


class Job(BaseModel):
    id: str
    title: str
    content_type: ContentType
    status: JobStatus
    formats: List[FormatResult]
    progress: int
    created_at: datetime
    updated_at: datetime
    user_id: str


class AnalyticsSummary(BaseModel):
    total_jobs: int
    completed_jobs: int
    total_formats_generated: int
    formats_this_month: int
    avg_completion_time_minutes: float
    top_format: str
    jobs_by_status: dict
    monthly_usage: List[dict]
