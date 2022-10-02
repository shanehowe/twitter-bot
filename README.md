
# The Bad Joke Twitter Bot

A twitter bot created using the twitter API and the Python libbrary tweepy.
The bot replies the any tweet it is mentioned it with a joke. The bot also tweets an hourly joke!.
Username: @BadJokeBot1
Mention the bot in a tweet containing #tellmeajoke and it will reply with a joke!

## Example Tweet Reply

```tweet
Thanks for the mention! Here's a joke for you.

Where did you learn to make ice cream? Sunday school.

What do you think? 🤖
```
Funny... right? 



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

 Simple but effective.
## Deployment

The Bot has been deployed. It is running on repl.it. Be sure to check it out!



## Possible Future Additions

If the bot really caught traction and gained some followers/activity. 
I was thinking of building out a Joke API. Allow users the submit their own jokes through a form which
would be reviewed by me and if they are appropriate, the joke would be added to the API for the bot to use.

It does sound like a lot of work but I think I would gain a lot of experiece in doing so. For
now I am happy with where it is at.
