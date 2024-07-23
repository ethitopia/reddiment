import praw 
import argparse
import parser
from .process import get_emotions, get_sentiment
from database.db_operations import insert_post, insert_comment
from database.db_config import get_db_connection


emotion_accumulation = {} 


def access_sub(id, secret, password, agent, username, url): 
    """
    given id, secret, pass, user_agent, username, url, accesses the url's 
    subreddit submission.
    """
    reddit = praw.Reddit(
        client_id=id, 
        client_secret=secret, 
        password=password, 
        user_agent=agent, 
        username=username
        )
    reddit.read_only = True
    submission = reddit.submission(url)
    title = submission.title
    id = submission.id
    description = submission.selftext 
    all_comments = submission.comments.body.list()
    
    return (title, id, url, description), all_comments

    
if __name__ == "__main__": 
    argparse.ArgumentParser(description="Using PRAW to access subreddit submissions")
    argparse.ArgumentParser.add_argument('--id', required=True, help="Reddit Client id")
    argparse.ArgumentParser.add_argument('--secret', required=True, help="Reddit Client secret")
    argparse.ArgumentParser.add_argument('--password', required=True, help="Reddit Client password")
    argparse.ArgumentParser.add_argument('--agent', required=True, help="Reddit user agent") #clarify? 
    argparse.ArgumentParser.add_argument('--username', required=True, help="Reddit Client username")
    argparse.ArgumentParser.add_argument('--url', required=True, help="submission url")
    args = parser.parse_args() 
    
    (title, post_id, url, description), all_comments = access_sub(args.id, args.secret, args.password, args.agent, args.username, args.url)
    
    selftext_sentiment = get_sentiment(description)
    selftext_emotion = get_emotions(description)
    reddit_sub = (title, post_id, url, description, selftext_sentiment, selftext_emotion
    )
    
    conn = get_db_connection() 
    
    insert_post(conn, reddit_sub)
    
    for comment in all_comments: 
        comment_body = comment.body if hasattr(comment, 'body') else ''
        comment_emotions = get_emotions(comment_body)
        comment_sentiment = get_sentiment(comment_body)
        sub_comment = (comment.id, comment.link_id, comment_body, comment.score, comment_sentiment, comment_emotions)
        insert_comment(conn, sub_comment)
        

        
    
    
    