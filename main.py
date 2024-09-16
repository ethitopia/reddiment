import logging
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import uvicorn
import praw
from .auth import auth_router, get_user_refresh_token, get_reddit_instance
from .sentiment.process import get_emotions, get_sentiment
from .api.api import access_sub
from .database.db_operations import insert_post, insert_comment
from .database.db_config import get_db_connection


load_dotenv()
app = FastAPI()
app.include_router(auth_router)


class RedditClient(BaseModel):
    url: str


@app.post("/fetch-data/")
async def fetch_data(request: RedditClient):
    """
    Step 3: Fetch subreddit data and store it in the Postgres DB.
    Requires user authentication via OAuth2.
    """
    try:
        username = "username_from_session"  # Replace with actual session management

        refresh_token = get_user_refresh_token(username)
        if not refresh_token:
            raise HTTPException(status_code=401, detail="User not authenticated")

        reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            refresh_token=refresh_token,
            user_agent=os.getenv('USER_AGENT')
        )

        title, post_id, url, description, all_comments = access_sub(request.url)
        
        selftext_sentiment = get_sentiment(description)
        selftext_emotion = get_emotions(description)

        conn = get_db_connection()
        reddit_sub = (title, post_id, url, description, selftext_sentiment, selftext_emotion)
        insert_post(conn, reddit_sub)

        for comment in all_comments:
            comment_data = process_comment_data(comment)
            insert_comment(conn, comment_data)

        return {"message": "Data fetched and stored successfully"}

    except Exception as e:
        logging.error(f"Exception: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching data.")



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
