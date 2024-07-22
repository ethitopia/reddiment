import praw 
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

