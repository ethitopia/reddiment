import os
import praw
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import secrets

load_dotenv()

auth_router = APIRouter()

CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDIRECT_URI = "http://localhost:8000/callback"
USER_AGENT = "desktop:myRedditApp:v1.0.0 (by /u/yourusername)"

def get_reddit_instance():
    return praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        user_agent=USER_AGENT
    )

@auth_router.get("/login")
def login(response: Response):
    reddit = get_reddit_instance()
    state = secrets.token_urlsafe(16)
    auth_url = reddit.auth.url(scopes=["identity", "read"], state=state, duration="permanent")
    response.set_cookie(key="auth_state", value=state, httponly=True, secure=True)
    return RedirectResponse(auth_url)

@auth_router.get("/callback")
def reddit_callback(request: Request):
    state = request.cookies.get("auth_state")
    code = request.query_params.get('code')
    if not code or not state or request.query_params.get('state') != state:
        raise HTTPException(status_code=400, detail="State mismatch or code missing")

    try:
        reddit = get_reddit_instance()
        reddit.auth.authorize(code)
        username = reddit.user.me().name
        return {"message": f"Welcome {username}, you are now logged in!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
