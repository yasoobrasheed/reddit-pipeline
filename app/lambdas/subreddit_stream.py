import os
import json
import praw
import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timedelta
from dotenv import load_dotenv


def send_message(queue, message_body, message_attributes={}):
    try:
        response = queue.send_message(
            MessageBody=message_body, MessageAttributes=message_attributes
        )
    except ClientError as error:
        print("Send message failed: %s", message_body)
        raise error
    else:
        return response


def parse_subreddits(reddit, subreddits):
    subreddit = reddit.subreddit(subreddits)
    last_five_minutes_utc = datetime.utcnow() - timedelta(minutes=5)

    SUBREDDIT_STREAM_FIFO_QUEUE_NAME = "subreddit-stream-queue.fifo"
    sqs = boto3.resource("sqs")
    queue = sqs.get_queue_by_name(QueueName=SUBREDDIT_STREAM_FIFO_QUEUE_NAME)

    for submission in subreddit.new(limit=100):
        created_utc = datetime.utcfromtimestamp(submission.created_utc)
        was_created_in_last_five_minutes = last_five_minutes_utc <= created_utc

        if was_created_in_last_five_minutes:
            message_body = {
                "subreddit": str(submission.subreddit),
                "title": str(submission.title),
                "author": str(submission.author),
                "url": str(submission.url),
                "submission_id": str(submission.id),
                "created": str(created_utc),
            }
            print(message_body)
            send_message(queue, message_body)
        else:
            return


def access_reddit():
    USER_AGENT = (
        os.environ["REDDIT_APP_NAME"] + "/0.1 by /u/" + os.environ["REDDIT_USERNAME"]
    )
    return praw.Reddit(
        client_id=os.environ["REDDIT_APP_ID"],
        client_secret=os.environ["REDDIT_APP_SECRET"],
        user_agent=USER_AGENT,
    )


def lambda_handler(event, context):
    load_dotenv()
    reddit = access_reddit()
    subreddits = [
        "news",
        "worldnews",
        "politics",
        "stocks",
        "stockmarket",
        "wallstreetbets",
        "cryptocurrency",
        "bitcoin",
    ]
    subreddits = "+".join(subreddits)
    parse_subreddits(reddit, subreddits)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Successfully streamed all new reddit posts in the past 5 minutes."
            }
        ),
    }
