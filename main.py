import praw 
import argparse
import parser
from database.db_operations import insert_post


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
    description = submission.selftext 
    all_comments = submission.comments.body.list()
    
    return description, all_comments
    
if __name__ == "__main__": 
    argparse.ArgumentParser(description="Using PRAW to access subreddit submissions")
    argparse.ArgumentParser.add_argument('--id', required=True, help="Reddit Client id")
    argparse.ArgumentParser.add_argument('--secret', required=True, help="Reddit Client secret")
    argparse.ArgumentParser.add_argument('--password', required=True, help="Reddit Client password")
    argparse.ArgumentParser.add_argument('--agent', required=True, help="Reddit user agent") #clarify? 
    argparse.ArgumentParser.add_argument('--username', required=True, help="Reddit Client username")
    argparse.ArgumentParser.add_argument('--url', required=True, help="submission url")
    
    args = parser.parse_args() 
    
    access_sub(args.id, args.secret, args.password, args.agent, args.username, args.url)
    
    