import json


def read_and_log_from_queue(event):
    for record in event["Records"]:
        print("--- test consumption ---")
        payload = record["body"]
        print(str(payload))


def lambda_handler(event, context):
    read_and_log_from_queue(event)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": "Successfully logged subreddit stream queue messages"}
        ),
    }
