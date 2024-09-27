from .api.api import access_sub
from .sentiment.process import get_emotions, get_sentiment

def fetch_data(url, reddit_instance):
    """
    Fetches data given access_sub function in apy.py 
    
    Args: 
        url (string): subreddit url 
        reddit_instance (dict): instantiation of reddit instance
    """
    title, post_id, url, description, all_comments = access_sub(url, reddit_instance)
    selftext_sentiment = get_sentiment(description)
    selftext_emotion = get_emotions(description)
    return {
        "title": title,
        "post_id": post_id,
        "url": url,
        "description": description,
        "selftext_sentiment": selftext_sentiment,
        "selftext_emotion": selftext_emotion,
        "comments": all_comments
    }

def process_comment_data(comment):
    """
    Given reddit comment, processes data with sentiment and emotion analysis. 
    
    Args: 
        comment (string): reddit comment
    
    Returns
        reddit object 
    """
    comment_body = comment.body if hasattr(comment, 'body') else ''
    comment_sentiment = get_sentiment(comment_body)
    comment_emotions = get_emotions(comment_body)
    return {
        "id": comment.id,
        "link_id": comment.link_id,
        "body": comment_body,
        "score": comment.score,
        "sentiment": comment_sentiment,
        "emotions": comment_emotions
    }
