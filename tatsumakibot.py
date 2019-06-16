import praw
import time
from praw.exceptions import APIException
import re

def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit(
                         'TatsuBot',
                         user_agent="Tatsumaki comment responder v1.1")
    print("Authenticated as {}!".format(reddit.user.me()))
    return reddit


# The main functions of the bot
def run_bot(reddit, subreddit_name):
    print("Obtaining 25 comments...")
    for comment in reddit.subreddit(subreddit_name).comments(limit = 25):
        lowercase_comment = comment.body.lower()
        try:
# Checking comment for "sassy lost child"
            if re.search(r"\b" + "sassy lost child" + r"\b", lowercase_comment) and comment.id not in cache and comment.author != reddit.user.me():
                print('String with "sassy lost child" found.' + comment.id)
                comment.reply("I'm not a sassy lost child!")
                print("Replied to comment" + comment.id)
                cache.append(comment.id)
# Checking comment for "tatsu"
            if re.search(r"\b" + "tatsu" + r"\b", lowercase_comment) and comment.id not in cache and comment.author != reddit.user.me():
                comment.reply("It's Tatsumaki, not Tatsu you peasant!")
                print("Replied to comment" + comment.id)
                cache.append(comment.id)
# Checking comment for "brat"
            if re.search(r"\b" + "brat" + r"\b", lowercase_comment) and comment.id not in cache and comment.author != reddit.user.me():
                print('String with "brat" found.' + comment.id)
                comment.reply("[Who do you think you are calling brat](https://tenor.com/325Y.gif)")
                print("Replied to comment" + comment.id)
                cache.append(comment.id)
# Checking comment for "spoilt brat"
            if re.search(r"\b" + "spoilt brat" + r"\b", lowercase_comment) and comment.id not in cache and comment.author != reddit.user.me():
                print('String with "spoilt brat" found.' + comment.id)
                comment.reply("Unforgivable. Me, a brat? I'm older than you!")
                print("Replied to comment" + comment.id)
                cache.append(comment.id)
# Checking comment for "best girl"
            if re.search(r"\b" + "best girl" + r"\b", lowercase_comment) and comment.id not in cache and comment.author != reddit.user.me():
                print('String with "best girl" found.' + comment.id)
                comment.reply("Of course *I* am best girl-no one compared to me!")
                print("Replied to comment" + comment.id)
                cache.append(comment.id)
# Checking comment for "tats"
            if re.search(r"\b" + "tats" + r"\b", lowercase_comment) and comment.id not in cache and comment.author != reddit.user.me():
                print('String with "tats" found.' + comment.id)
                comment.reply("It's **Tornado of Terror** to you, avocado head!")
                print("Replied to comment" + comment.id)
                cache.append(comment.id)
# Response to "bad bot"
            if re.search(r"\b" + "bad bot" + r"\b", lowercase_comment) and comment.id not in cache:
                parent = comment.parent()
                if parent.author == reddit.user.me():
                    print('Response to "bad bot" initiated.')
                    comment.reply("[Hmph!](https://media.giphy.com/media/zzl3XA0WIdIWI/giphy.gif)")
                    print('Response to "bad bot" finished.')
                    cache.append(comment.id)
# Response to username call
            if re.search(r"\b" + "u/Not_a_brat_Tatsumaki" + r"\b", lowercase_comment) and comment.id not in cache:
                print("Responding to username call")
                comment.reply("[Who called? Can't you see I'm busy?](https://media.giphy.com/media/puFKQsuYMv8Zi/giphy.gif)")
                print("Responded to username call")
                cache.append(comment.id)
# Linking Github
            if "who created you" in lowercase_comment and comment.id not in cache:
                parent = comment.parent()
                if parent.author == reddit.user.me():
                    comment.reply("[I created myself](link)")
                    cache.append(comment.id)
# Checking for "You are doing that too much" error
        except APIException as err:
            print("APIException", err)
            time.sleep(20)
            return False


def main():
    reddit = authenticate()
    while True:
        run_bot(reddit, "MemeTuesday")
#Sleep for 10 seconds
        print("Sleeping for 10 seconds")
        time.sleep(10)


print("About to run bot")
if __name__ == "__main__":
    cache = []
    main()

