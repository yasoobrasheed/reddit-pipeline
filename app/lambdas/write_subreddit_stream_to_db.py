import json
from create_session import create_session
from submissions import Submission
from datetime import datetime


def read_and_write_records(event):
    session = create_session()
    print(event["Records"])

    with session.begin():
        for record in event["Records"]:
            print("--- test consumption ---")
            payload = record["body"]
            print(str(payload))

            submission = Submission(
                subreddit=record["body"]["subreddit"],
                title=record["body"]["title"],
                author=record["body"]["author"],
                url=record["body"]["url"],
                submission_id=record["body"]["submission_id"],
                submission_created_at=record["body"]["submission_created_at"],
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
