import praw 

reddit = praw.Reddit(
    client_id="jY-Juldz8QjmQjKLg2oNBg",
    client_secret="4ZJO8wfWGG4K6KzwLpWXBqYPYntmog",
    password="19611230",
    user_agent="test_script for subreddit scraping",
    username="Pitiful-Code6160"
)

subreddit = reddit.subreddit('subreddit_name')

top_posts = subreddit.top(limit=10)



