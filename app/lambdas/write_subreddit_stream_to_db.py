import json
from create_session import create_session
from submissions import Submission
from datetime import datetime


def read_and_write_records(event):
    session = create_session()

    with session.begin():
        for record in event["Records"]:
            print("--- test consumption ---")
            payload = record["body"]
            print(str(payload))

            print(payload["subreddit"])
            print(payload.subreddit)

            submission = Submission(
                subreddit=payload["subreddit"],
                title=payload["title"],
                author=payload["author"],
                url=payload["url"],
                submission_id=payload["submission_id"],
                submission_created_at=payload["submission_created_at"],
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            session.add(submission)
            session.commit()


def lambda_handler(event, context):
    read_and_write_records(event)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": "Successfully logged subreddit stream queue messages"}
        ),
    }
