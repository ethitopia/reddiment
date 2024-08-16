import psycopg2
from psycopg2.extras import DictCursor


def get_db_connection():
    """
    This function creates and returns a connection to the PostgreSQL database.
    
    FIXME: DB_USERNAME and DB_PASSWORD stand in place for db login info.  
    """
    try:
        # for now, db is locahost 
        connection = psycopg2.connect(
            host='localhost',
            dbname='flask_db',
            user='DB_USERNAME',
            password='DB_PASSWORD', 
            port=5432  
        )
        print("Database connection established")
        return connection
    except psycopg2.OperationalError as e:
        print("Operational error while connecting to the database:", e)
    except Exception as e:
        print("Error connecting to the database:", e)
    return None



