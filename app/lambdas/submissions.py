from sqlalchemy import Column, String, Integer, Unicode, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True)
    subreddit = Column(String, nullable=False)
    title = Column(Unicode, nullable=False)
    author = Column(String, nullable=False)
    url = Column(String, nullable=False)
    submission_id = Column(String, nullable=False)
    submission_created_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())
