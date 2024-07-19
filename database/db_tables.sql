CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    reddit_post_id TEXT UNIQUE,
    title TEXT,
    score INT,
    url TEXT
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    reddit_comment_id TEXT UNIQUE,
    post_id INT,
    body TEXT,
    score INT,
    FOREIGN KEY (post_id) REFERENCES posts(id)
);
