import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


def get_db_connection():
    try:
        connection = psycopg2.connect(
            host='localhost',
            dbname='your_db_name',
            user=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD'),
            port=5432  
        )
        print("Database connection established")
        return connection
    except psycopg2.OperationalError as e:
        print("Operational error while connecting to the database:", e)
    except Exception as e:
        print("Error connecting to the database:", e)
    return None



