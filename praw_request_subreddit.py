import os
from venv import create
from dotenv import load_dotenv
from datetime import datetime, timedelta
import praw


def access_reddit():
    USER_AGENT = os.environ["APP_NAME"] + "/0.1 by /u/" + os.environ["USERNAME"]
    return praw.Reddit(
        client_id=os.environ["APP_ID"],
        client_secret=os.environ["APP_SECRET"],
        user_agent=USER_AGENT,
    )


def parse_subreddits(reddit, subreddits):
    subreddit = reddit.subreddit(subreddits)
    last_five_minutes_utc = datetime.utcnow() - timedelta(minutes=5)

    for submission in subreddit.new(limit=25):
        created_utc = datetime.utcfromtimestamp(submission.created_utc)
        was_created_in_last_five_minutes = last_five_minutes_utc <= created_utc

        if was_created_in_last_five_minutes:
            print("----------------------")
            print("subreddit: " + str(submission.subreddit))
            print("title: " + str(submission.title))
            print("author: " + str(submission.author))
            print("created:  " + str(created_utc))
        else:
            return


def main():
    load_dotenv()
    reddit = access_reddit()  # set a 23 hour interval here in parallel
    subreddits = "news+worldnews+politics"
    parse_subreddits(reddit, subreddits)


if __name__ == "__main__":
    main()
