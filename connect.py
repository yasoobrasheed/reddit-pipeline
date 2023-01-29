import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

engine = psycopg2.connect(
    user=os.environ["DB_USERNAME"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_ENDPOINT"],
    port=os.environ["DB_PORT"],
    dbname=os.environ["DB_NAME"],
)

cur = engine.cursor()

cur.execute("SELECT * FROM submissions")
