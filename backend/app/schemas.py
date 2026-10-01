from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# === USER ===
class UserCreate(BaseModel):
    name: str
    login: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    login: str
    photo_profile: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    login: Optional[str] = None
    password: Optional[str] = None
    photo_profile: Optional[str] = None

# === POST ===
class PostCreate(BaseModel):
    name: str
    description: str
    media: Optional[str] = None

class PostResponse(BaseModel):
    id: int
    name: str
    description: str
    media: Optional[str] = None
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True

class PostUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    media: Optional[str] = None

# === COMMENT ===
class CommentCreate(BaseModel):
    text: str
    media: Optional[str] = None

class CommentResponse(BaseModel):
    id: int
    text: str
    media: Optional[str] = None
    created_at: datetime
    user_id: int
    post_id: int

    class Config:
        from_attributes = True

class CommentUpdate(BaseModel):
    text: Optional[str] = None
    media: Optional[str] = None