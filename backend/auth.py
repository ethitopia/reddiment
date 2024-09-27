import os
import praw
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import secrets
from database.db_config import get_db_connection
from database.db_operations import get_user_refresh_token, insert_user
from session import create_session_token


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
    auth_url = reddit.auth.url(scopes=["identity", "read", "history"], state=state, duration="permanent")
    response.set_cookie(key="auth_state", value=state, httponly=True, secure=True)
    return RedirectResponse(auth_url)


@auth_router.get("/callback")
def reddit_callback(request: Request, response: Response):
    state = request.cookies.get("auth_state")
    code = request.query_params.get('code')
    returned_state = request.query_params.get('state')
    if not code or not state or returned_state != state:
        raise HTTPException(status_code=400, detail="State mismatch or code missing")

    try:
        reddit = get_reddit_instance()
        refresh_token = reddit.auth.authorize(code)
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            refresh_token=refresh_token,
            user_agent=USER_AGENT
        )
        username = reddit.user.me().name

        # Store the refresh token associated with the username
        conn = get_db_connection()
        insert_user(conn, username, refresh_token)

        # Create a session token and set it as a cookie
        session_token = create_session_token(username)
        response.set_cookie(key="session_token", value=session_token, httponly=True, secure=True)

        return {"message": f"Welcome {username}, you are now logged in!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_user_refresh_token(username):
    conn = get_db_connection()
    return get_user_refresh_token(conn, username)