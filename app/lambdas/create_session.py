import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def create_reddit_stream_engine():
    load_dotenv()
    DB_CONN_STRING = f"postgresql://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_ENDPOINT']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}?sslmode=require"
    return create_engine(DB_CONN_STRING, echo=True)


def create_session():
    engine = create_reddit_stream_engine()
    return Session(engine)
