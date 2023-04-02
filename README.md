
# The Bad Joke Twitter Bot

A twitter bot created using the twitter API and the Python libbrary tweepy.
The bot replies the any tweet it is mentioned it with a joke. The bot also tweets an hourly joke!.

Username: @BadJokeBot1  
Mention the bot in a tweet containing #tellmeajoke and it will reply with a joke

## Example Tweet Reply

```tweet
Thanks for the mention! Here's a joke for you.

Where did you learn to make ice cream? Sunday school.

What do you think? 🤖
```
Funny...



## How it works
 
 To make it work, I had to tweet the bot myself just so I could grab the ID
 assoiciated with my tweet. I then used this to my advantage by only looking
 at tweets that have been created after my tweet. Once the bot finds a new tweet we grab
 the id from that tweet and store the ID in a file for future refrences. The bot rests for 15 seconds and the process for finding new tweets repeats.


 * Snippet of the file functions

 ```python
 def get_last_seen(file: str) -> int:
    """
    Retrieves the last seen tweet from the file
    :param file: str
    :return: int
    """
    with open(file, "r") as f:
        last_seen = f.read().strip()
        return int(last_seen)
 ```

 ```python 
 def update_last_seen(file: str, id: int) -> None:
    """
    Writes new last seen ID to file
    :param file: str
    :param id: int
    :return: None
    """
    with open(file, "w") as f:
        f.write(str(id))
 ```

