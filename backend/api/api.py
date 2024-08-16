import praw 
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
