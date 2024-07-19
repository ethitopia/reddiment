import psycopg2
from psycopg2.extras import DictCursor

def get_db_connection():
    """
    This function creates and returns a connection to the PostgreSQL database.
    """
    try:
        # Set up your database connection parameters
        connection = psycopg2.connect(
            dbname='your_database_name',
            user='your_database_user',
            password='your_database_password',
            host='your_database_host',
            port='your_database_port'  # Default is usually 5432
        )
        print("Database connection established")
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        return None
