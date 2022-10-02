import tweepy
import time
import requests
from dotenv import dotenv_values


# Load environment variables
config = dotenv_values(".env")
CONSUMER_KEY = config["CONSUMER_KEY"]
CONSUMER_KEY_SECRET = config["CONSUMER_KEY_SECRET"]
ACCESS_TOKEN = config["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = config["ACCESS_TOKEN_SECRET"]

# File to store last seen tweet ID
MENTIONS_FILE_NAME = "last_seen.txt"
HASHTAG_FILE_NAME = "hashtag_last_seen.txt"

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)


def main():
    """
    Main function
    """
    while True:
        reply_to_mentions()
        time.sleep(15)


def get_joke() -> str:
    """
    Gets a random joke from the API
    :param: None
    :return: str
    """
    try:
        response = requests.get(
            "https://icanhazdadjoke.com/", headers={"Accept": "application/json"}
        )
        data = response.json()
        return data["joke"]
    except requests.RequestException:
        return "All out of jokes!"


def get_last_seen(file: str) -> int:
    """
    Retrieves the last seen tweet from the file
    :param file: str
    :return: int
    """
    with open(file, "r") as f:
        last_seen = f.read().strip()
        return int(last_seen)


def update_last_seen(file: str, id: int) -> None:
    """
    Writes new last seen ID to file
    :param file: str
    :param id: int
    :return: None
    """
    with open(file, "w") as f:
        f.write(str(id))


def reply_to_mentions() -> None:
    """
    Replies to tweets that mention the bot
    :param: None
    :return: None
    """
    reply = (
        f"Thanks for the mention! Here's a joke for you.\n\n{get_joke()}\n\nWhat do you think? 🤖"
    )
    tweets = api.mentions_timeline(
        since_id=get_last_seen(MENTIONS_FILE_NAME), tweet_mode="extended"
    )

    if not tweets:
        print("No new tweets")
        return

    for tweet in reversed(tweets):
        if "#tellmeajoke" in tweet.text.lower():
            last_seen = tweet.id
            print(f"{tweet.id} | {tweet.user.name} said {tweet.text}")
            print("Replying to tweet!")
            api.update_status(
                status=reply,
                in_reply_to_status_id=tweet.id,
                auto_populate_reply_metadata=True,
            )
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            # Update last seen ID after replying to tweets
            update_last_seen(MENTIONS_FILE_NAME, last_seen)


if __name__ == "__main__":
    main()
