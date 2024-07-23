CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    reddit_post_id TEXT UNIQUE,
    title TEXT,
    selftext TEXT,
    score INT,
    url TEXT,
    title_sentiment REAL,
    title_emotion TEXT,
    selftext_sentiment REAL,
    selftext_emotion TEXT
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    reddit_comment_id TEXT UNIQUE,
    post_id INT,
    body TEXT,
    score INT,
    comment_sentiment REAL, 
    comment_emotion TEXT,
    FOREIGN KEY (post_id) REFERENCES posts(id)
);
