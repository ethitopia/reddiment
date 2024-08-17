import argparse
import logging 
from process import get_emotions, get_sentiment
from api.api import access_sub 
from database.db_operations import insert_post, insert_comment
from database.db_config import get_db_connection
from flask import Flask, request, jsonify, abort 


app = Flask(__name__)


@app.route('/fetch', methods=['POST'])
def fetch_data():
    """ 
    Fetches subreddit data and stores in postgres db. 
    """ 
    try:
        args = request.json
        title, post_id, url, description, all_comments = access_sub(args[url])
        
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
            insert_comment(conn, sub_comment)
            
        return jsonify({"message": "Data fetched and stored successfully"}), 200
    except Exception as e: 
        logging.error(f'Exception as {e}')
        abort(500, description="An error occurred while fetching data.") 
        
        
def process_comment_data(comment):
    """
    Ensures comment data is sufficient for reddiment. 
    """
    comment_body = comment.body if hasattr(comment, 'body') else ''
    return (comment.id, comment.link_id, comment_body, comment.score, get_sentiment(comment_body), get_emotions(comment_body))
    
if __name__ == "__main__": 
    app.run(debug=True)
    print("completed test run")

        
    
    
    