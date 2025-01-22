import uuid
from fastapi import HTTPException

# In-memory storage for session tokens (use Redis/DB in production)
session_tokens = {}

def create_token(username: str) -> str:
    """Generate a new session token and store it."""
    token = str(uuid.uuid4())
    session_tokens[token] = username
    return token

def get_username_from_token(token: str) -> str:
    """Retrieve the username associated with a session token."""
    username = session_tokens.get(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return username

def delete_token(token: str):
    """Remove a session token."""
    return session_tokens.pop(token, None)
