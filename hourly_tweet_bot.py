import tweepy
import time
from dotenv import dotenv_values
from bot import get_joke


# Load environment variables
config = dotenv_values(".env")
CONSUMER_KEY = config["CONSUMER_KEY"]
CONSUMER_KEY_SECRET = config["CONSUMER_KEY_SECRET"]
ACCESS_TOKEN = config["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = config["ACCESS_TOKEN_SECRET"]

TIME = 60 * 60 #One hour

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)


def main():
    while True:
        print("Tweeting a joke...")
        tweet_joke()
        print("Sleeping for an hour...")
        time.sleep(TIME)


def tweet_joke() -> None:
    """
    Tweets a joke
    :param: None
    :return: None
    """
    joke = get_joke()
    api.update_status(status=f"Heres one for you...\n\n {joke} \n\n #joke #dad #dadjokes")


if __name__ == "__main__":
    main()