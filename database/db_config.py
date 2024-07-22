import psycopg2
from psycopg2.extras import DictCursor

def get_db_connection():
    """
    This function creates and returns a connection to the PostgreSQL database.
    """
    try:
        # Set up your database connection parameters
        connection = psycopg2.connect(
            dbname='db_name',
            user='db_user',
            password='db_pass',
            host='db_host',
            port='5432' 
        )
        print("Database connection established")
        return connection
    except psycopg2.OperationalError as e:
        print("Operational error while connecting to the database:", e)
    except Exception as e:
        print("Error connecting to the database:", e)
    return None
