import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords 
import nrclex
import praw 
nltk.download('vader_lexicon')
nltk.download('punkt')


def get_emotions(comment): 
    """
    Returns an emotion score given a string comment
    
    Args: 
        comment (string): reddit post comment in string form
        
    Returns: 
        emotion_score (dict): of associated scores with each value  
    
    """
 
    tokens = word_tokenize(comment)
    filtered_words = [c for c in tokens if c not in stopwords.words('english')] # remove stopwords 
    
    filtered_text = ' '.join(filtered_words)
    emotion = nrclex.NRCLex(filtered_text)
    emotion_score = emotion.raw_emotion_scores 
    emotion_score.pop('positive', None)
    emotion_score.pop('negative', None)
    
    return emotion_score 
        
        
def get_sentiment(comment): 
    """
    Returns a sentiment score for each string comment 
    
    Args: 
        comment (string): a string of subreddit comment 
    """
 
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(list[0])
    return scores 
    
    
    
        
        
        
    
    
    
    







