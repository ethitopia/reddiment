from db_config import get_db_connection

def insert_post(conn, post_data):
    """
    Inserts a post into the database.
    """
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""INSERT INTO posts (reddit_post_id, title, score, url, selftext_sentiment, selftext_emotion) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (reddit_post_id) DO NOTHING""", post_data)
            conn.commit()
            print("Post inserted successfully")
        except Exception as e:
            conn.rollback()
            print("An error occurred:", e)
        finally:
            cur.close()
            conn.close()
    else:
        print("Failed to get database connection")
        
        
def insert_comment(conn, comment_data):
    """
    Inserts a post into the database.
    """
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO comments (reddit_comment_id, post_id, body, score, comment_sentiment, comment_emotion) 
                        VALUES (%s, %s, %s, %s, %s, %s) 
                        ON CONFLICT (reddit_post_id) DO NOTHING
                        """, comment_data)
            conn.commit()
            print("Post inserted successfully")
        except Exception as e:
            conn.rollback()
            print("An error occurred:", e)
        finally:
            cur.close()
            conn.close()
    else:
        print("Failed to get database connection")
