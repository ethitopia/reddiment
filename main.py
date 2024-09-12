import logging 
from .sentiment.process import get_emotions, get_sentiment
from .api.api import access_sub 
from .database.db_operations import insert_post, insert_comment
from .database.db_config import get_db_connection
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn


app = FastAPI()


class redditClient(BaseModel): 
    url : str 
    
    
@app.get("/")
async def fetch_data(request : redditClient):
    """ 
    Fetches subreddit data and stores in postgres db. 
    """ 
    try:
        title, post_id, url, description, all_comments = access_sub(request.url)
        
        selftext_sentiment = get_sentiment(description)
        selftext_emotion = get_emotions(description)
        
        conn = get_db_connection()
        reddit_sub = (title, post_id, url, description, selftext_sentiment, selftext_emotion)
        insert_post(conn, reddit_sub)
        
        for comment in all_comments:
            comment_body = comment.body if hasattr(comment, 'body') else ''
            comment_emotions = get_emotions(comment_body)
            comment_sentiment = get_sentiment(comment_body)
            sub_comment = (comment.id, comment.link_id, comment_body, comment.score, comment_sentiment, comment_emotions)
            insert_comment(conn, sub_comment) #inserts comment into comment db 
            
        return {"message": "Data fetched and stored successfully"}
    except Exception as e: 
        logging.error(f'Exception as {e}')
        raise HTTPException(500, description="An error occurred while fetching data.") 
        
        
def process_comment_data(comment):
    """
    Ensures comment data is sufficient for reddiment. 
    """
    comment_body = comment.body if hasattr(comment, 'body') else ''
    return (comment.id, comment.link_id, comment_body, comment.score, get_sentiment(comment_body), get_emotions(comment_body))
    
    
if __name__ == "__main__": 
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)

        
    
    
    