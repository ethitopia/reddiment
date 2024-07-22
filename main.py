import praw 
import argparse
import parser
from database.db_operations import insert_post

reddit = praw.Reddit(
    client_id="jY-Juldz8QjmQjKLg2oNBg",
    client_secret="4ZJO8wfWGG4K6KzwLpWXBqYPYntmog",
    password="19611230",
    user_agent="test_script for subreddit scraping",
    username="Pitiful-Code6160"
)

reddit.read_only = True

subreddit = reddit.subreddit('Cornell')

top_posts = subreddit.top(limit=10)

for post in top_posts: 
    post_data = (post.id, post.title, post.score, post.url)
    insert_post = post_data 

def main(): 
    argparse.ArgumentParser(description="Using PRAW to access subreddit submissions")
    argparse.ArgumentParser.add_argument('--id', required=True, help="Reddit Client id")
    argparse.ArgumentParser.add_argument('--secret', required=True, help="Reddit Client secret")
    argparse.ArgumentParser.add_argument('--password', required=True, help="Reddit Client password")
    argparse.ArgumentParser.add_argument('--agent', required=True, help="Reddit user agent") #clarify? 
    argparse.ArgumentParser.add_argument('--username', required=True, help="Reddit Client username")
    argparse.ArgumentParser.add_argument('--url', required=True, help="submission url")
    
    args = parser.parse_args() 
    
    reddit = praw.Reddit(
        client_id=args.id,
        client_secret=args.secret,
        password=args.password,
        user_agent=args.agent,
        username=args.username
        )
    
    url = args.url
    
    
    