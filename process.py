import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzers
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords 
from nrclex import NRClex 
import praw 

nltk.download('punkt')

def normalize(comments): 
    emot_freq = {} 
    comments = [com for com in comments if com not in stopwords.words('english')] # remove stopwords 
    for comment in comments: 
        tokens = word_tokenize(comment)
        emotion = NRCLex(' '.join(tokens))
        emotion_score = emotion.raw_emotion_scores 
        
        
    
    
    
    







