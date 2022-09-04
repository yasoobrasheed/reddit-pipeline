import os
from dotenv import load_dotenv
import requests
import requests.auth


def get_reddit_request_token():
    USER_AGENT = os.environ["APP_NAME"] + "/0.1 by /u/" + os.environ["USERNAME"]
    REDDIT_ACCESS_TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
    CLIENT_AUTH = requests.auth.HTTPBasicAuth(
        os.environ["APP_ID"], os.environ["APP_SECRET"]
    )
    POST_DATA = {
        "grant_type": "password",
        "username": os.environ["USERNAME"],
        "password": os.environ["PASSWORD"],
    }
    HEADERS = {"User-Agent": USER_AGENT}

    reddit_request_token = requests.post(
        REDDIT_ACCESS_TOKEN_URL,
        auth=CLIENT_AUTH,
        data=POST_DATA,
        headers=HEADERS,
    ).json()
    return reddit_request_token


def use_reddit_request_token(reddit_request_token, request_path):
    USER_AGENT = os.environ["APP_NAME"] + "/0.1 by /u/" + os.environ["USERNAME"]
    HEADERS = {
        "Authorization": "bearer " + reddit_request_token["access_token"],
        "User-Agent": USER_AGENT,
    }
    REDDIT_OAUTH_URL = "https://oauth.reddit.com/"
    response = requests.get(REDDIT_OAUTH_URL + request_path, headers=HEADERS)
    return response.json()


def main():
    load_dotenv()
    REDDIT_PROFILE_REQUEST_PATH = "api/v1/me"
    reddit_request_token = get_reddit_request_token()
    reddit_response = use_reddit_request_token(
        reddit_request_token, REDDIT_PROFILE_REQUEST_PATH
    )
    print(reddit_response)


if __name__ == "__main__":
    main()
