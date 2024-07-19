from db_config import get_db_connection

def insert_post(post_data):
    """
    Inserts a post into the database.
    """
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO posts (reddit_post_id, title, score, url) VALUES (%s, %s, %s, %s) ON CONFLICT (reddit_post_id) DO NOTHING", post_data)
            conn.commit()
            cur.close()
            print("Post inserted successfully")
        except Exception as e:
            print("An error occurred:", e)
        finally:
            conn.close()
    else:
        print("Failed to get database connection")
