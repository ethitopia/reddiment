import praw 
import os 
from config import get_reddit_config 


def access_sub(url): 
    """
    Given a url, accesses the submitted subreddit submission.
    """
    
    config = get_reddit_config() 
    reddit = praw.Reddit(
        client_id=config['id'], #Y-Juldz8QjmQjKLg2oNBg
        client_secret=config['secret'], #4ZJO8wfWGG4K6KzwLpWXBqYPYntmog
        password=config['password'], #19611230
        user_agent=config['agent'],
        username=config['username'] #'Pitiful-Code6160'
        )
    
    reddit.read_only = True
    submission = reddit.submission(url=url)
    submission.comments.replace_more(limit=None)
    all_comments = [comment.body for comment in submission.comments.list()]
    
    return (submission.title, submission.id, submission.url, submission.selftext), all_comments


def get_reddit_config(): 
    """
    Retrieves Reddit configuration from environment variables 
    """
    
    return {'client_id': os.getenv('REDDIT_CLIENT_ID'),
        'client_secret': os.getenv('REDDIT_CLIENT_SECRET'),
        'password': os.getenv('REDDIT_PASSWORD'),
        'user_agent': 'desktop:myRedditApp:v1.0.0 (by /u/yourusername)',
        'username': os.getenv('REDDIT_USERNAME')
    }