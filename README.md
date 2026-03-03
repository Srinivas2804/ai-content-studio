# ContentStudio — AI Content Repurposing Studio

A full-stack solo-founder business starter. Drop one piece of content, get 12 AI-generated formats instantly.

## Stack
| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 14, React 18, TypeScript, Tailwind CSS |
| Backend | Python 3.11+, FastAPI, Uvicorn, Pydantic |
| Charts | Recharts |

## Quick Start

### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
python main.py
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

### Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
# App: http://localhost:3000
```

## Pages
| Route | Description |
|-------|-------------|
| / | Landing page with pricing, features, waitlist CTA |
| /dashboard | Analytics + job management + create modal |
| /tracking | Real-time per-format progress tracker |

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/health | Health check |
| POST | /api/auth/register | Create account |
| POST | /api/auth/login | Login |
| GET | /api/jobs | List jobs |
| POST | /api/jobs | Create repurposing job |
| GET | /api/jobs/{id} | Job detail + results |
| DELETE | /api/jobs/{id} | Delete job |
| GET | /api/analytics/summary | Dashboard stats |

## 12 Output Formats
Twitter Thread, LinkedIn Post, Blog Article, Newsletter, Instagram Caption,
YouTube Shorts Script, Email Sequence, SEO Summary, Podcast Notes,
Quote Cards, TikTok Script, Facebook Post

## Demo Login
- Email: alex@contentstudio.ai
- Password: any password works in demo mode

## Production Upgrade Path
1. Replace in-memory DB with SQLAlchemy + PostgreSQL
2. Replace simulation with real OpenAI/Anthropic API calls
3. Add JWT auth (python-jose)
4. Add Celery + Redis for job queues
5. Add Stripe for subscriptions
