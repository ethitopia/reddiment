
def create_sub(conn): 
    """
    Creates a database for each subreddit
    
    Args: 
        conn (psycopg2.connect): database connection 
    """
    cur = conn.cursor() 
    cur.execute('DROP TABLE IF EXISTS subreddit')
    cur.execute('''CREATE TABLE subreddit (
                id serial PRIMARY KEY, 
                name VARCHAR9(255) UNIQUE NOT NULL, 
                description TEXT
                )''')
    cur.close() 
    conn.close()  


def insert_post(conn, post_data):
    """
    Inserts a post into a predefined subreddit database 
    
    Args: 
        conn (psycopg2.connect): database connection 
        post_data (): scraped subreddit post data 
    """
    cur = conn.cursor()
    try:
        cur.execute("""INSERT INTO posts (reddit_post_id, title, url, selftext_sentiment, selftext_emotion) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (reddit_post_id) DO NOTHING""", post_data)
        conn.commit()
        print("Post inserted successfully")
    except Exception as e:
        conn.rollback()
        print("An error occurred:", e)
    finally:
        cur.close()
            
        
def insert_comment(conn, comment_data):
    """
    Inserts a comment into the database.
    
    Args: 
        conn (psycopg2.connect): database connection 
        comment_data (): scraped comment data 
    """
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO comments (reddit_comment_id, post_id, body, score, comment_sentiment, comment_emotion) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (reddit_post_id) DO NOTHING", comment_data)
        conn.commit()
        print("Post inserted successfully")
    except Exception as e:
        conn.rollback()
        print("An error occurred:", e)
    finally:
        cur.close() 
        

def insert_user(conn, username, refresh_token):
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (username, refresh_token) VALUES (%s, %s) ON CONFLICT (username) DO UPDATE SET refresh_token = EXCLUDED.refresh_token",
            (username, refresh_token),
        )
        conn.commit()

def get_user_refresh_token(conn, username):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT refresh_token FROM users WHERE username = %s",
            (username,),
        )
        result = cursor.fetchone()
        return result[0] if result else None
