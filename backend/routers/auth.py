from fastapi import APIRouter, HTTPException
from models.schemas import UserCreate, UserLogin
from models import database as db
import hashlib

router = APIRouter()

def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

@router.post("/register")
def register(body: UserCreate):
    if db.get_user_by_email(body.email):
        raise HTTPException(400, "Email already registered")
    user = db.create_user({
        "name": body.name,
        "email": body.email,
        "password_hash": hash_password(body.password),
    })
    return {"user_id": user["id"], "name": user["name"], "email": user["email"], "plan": user["plan"]}

@router.post("/login")
def login(body: UserLogin):
    user = db.get_user_by_email(body.email)
    if not user:
        raise HTTPException(401, "Invalid credentials")
    return {
        "user_id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "plan": user["plan"],
        "token": f"demo_token_{user['id']}"
    }

@router.get("/me/{user_id}")
def get_me(user_id: str):
    user = db.get_user(user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return {k: v for k, v in user.items() if k != "password_hash"}
