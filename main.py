import praw 
import argparse
from process import get_emotions, get_sentiment
from database.db_operations import insert_post, insert_comment
from database.db_config import get_db_connection


def get_parser(): 
    parser = argparse.ArgumentParser(description="Using PRAW to access subreddit submissions")
    parser.add_argument('--id', required=True, help="Reddit Client id")
    parser.add_argument('--secret', required=True, help="Reddit Client secret")
    parser.add_argument('--password', required=True, help="Reddit Client password")
    #parser.add_argument('--agent', required=True, help="Reddit user agent") #clarify? 
    parser.add_argument('--username', required=True, help="Reddit Client username")
    parser.add_argument('--url', required=True, help="submission url")
    
    return parser
    

def access_sub(id, secret, password, agent, username, url): 
    """
    given id, secret, pass, user_agent, username, url, accesses the url's 
    subreddit submission.
    """
    reddit = praw.Reddit(
        client_id=id, #Y-Juldz8QjmQjKLg2oNBg
        client_secret=secret, #4ZJO8wfWGG4K6KzwLpWXBqYPYntmog
        password=password, #19611230
        user_agent=agent,
        username=username #'Pitiful-Code6160'
        )
    
    reddit.read_only = True
    submission = reddit.submission(url)
    all_comments = submission.comments.body.list()
    
    return (submission.title, submission.id, submission.url, submission.selftext), all_comments

    
if __name__ == "__main__": 
    parser = get_parser()
    args = parser.parse_args()
    agent = 'desktop:myRedditApp:v1.0.0 (by /u/Pitiful-Code6160)'
    
    (title, post_id, url, description), all_comments = access_sub(args.id, args.secret, args.password, agent, args.username, args.url)
    
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
        
    print("completed test run")

        
    
    
    