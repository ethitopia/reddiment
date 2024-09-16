import praw
from dotenv import load_dotenv
import os


def access_sub(url):
    """
    Given a URL, accesses the submitted subreddit submission and returns the post and its comments.
    """
    config = get_reddit_config()
    reddit = praw.Reddit(
        client_id=config['client_id'],
        client_secret=config['client_secret'],
        password=config['password'],
        user_agent=config['user_agent'],
        username=config['username']
    )

    reddit.read_only = True
    submission = reddit.submission(url=url)
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()  # Return full comment objects

    return submission.title, submission.id, submission.url, submission.selftext, all_comments


def get_reddit_config():
    """
    Retrieves Reddit configuration from environment variables.
    """
    return {
        'client_id': os.getenv('REDDIT_CLIENT_ID'),
        'client_secret': os.getenv('REDDIT_CLIENT_SECRET'),
        'password': os.getenv('REDDIT_PASSWORD'),
        'user_agent': 'desktop:myRedditApp:v1.0.0 (by /u/yourusername)',
        'username': os.getenv('REDDIT_USERNAME')
    }
    
    
