import praw
import time
from praw.exceptions import APIException


def authenticate():
	print("Authenticating...")
	reddit = praw.Reddit(
						 'TatsuBot',
						 user_agent="Tatsumaki comment responder v1.1")
	print("Authenticated as {}!".format(reddit.user.me()))
	return reddit


def run_bot(reddit, subreddit_name):
	print("Obtaining 25 comments...")
	for comment in reddit.subreddit(subreddit_name).comments(limit = 25):
		lowercase_comment = comment.body.lower()
		try:
#fix not in lowercase_comment for 2, 3, 6
			if "sassy lost child" in lowercase_comment and comment.id not in cache and comment.author != reddit.user.me():
				print('String with "sassy lost child" found.' + comment.id)
				comment.reply("I'm not a sassy lost child!")
				print("Replied to comment" + comment.id)
				cache.append(comment.id)
	
			if "tatsu" in lowercase_comment and "tatsumaki" not in lowercase_comment and comment.id not in cache and comment.author != reddit.user.me():
				comment.reply("It's Tatsumaki, not Tatsu you octopus!")
				print("Replied to comment" + comment.id)
				cache.append(comment.id)
			
			if "brat" in lowercase_comment and "spoilt brat" not in lowercase_comment and comment.id not in cache and comment.author != reddit.user.me():
				print('String with "brat" found.' + comment.id)
				comment.reply("Who do you think you are calling brat")
				print("Replied to comment" + comment.id)
				cache.append(comment.id)
			
			if "spoilt brat" in lowercase_comment and comment.id not in cache and comment.author != reddit.user.me():
				print('String with "spoilt brat" found.' + comment.id)
				comment.reply("Unforgivable. Me, a brat? I'm older than you!")
				print("Replied to comment" + comment.id)
				cache.append(comment.id)
			
			if "best girl" in lowercase_comment and comment.id not in cache and comment.author != reddit.user.me():
				print('String with "best girl" found.' + comment.id)
				comment.reply("Of course I am best girl-no one compared to me!")
				print("Replied to comment" + comment.id)
				cache.append(comment.id)

			if "tats" in lowercase_comment and "tatsumaki" not in lowercase_comment and comment.id not in cache and comment.author != reddit.user.me():
				print('String with "tats" found.' + comment.id)
				comment.reply("It's Tornado of Terror to you, avocado head!")
				print("Replied to comment" + comment.id)
				cache.append(comment.id)

		except APIException as err:
			print("APIException", err)
			time.sleep(20)
			return False


def main():
	reddit = authenticate()
	while True:
		run_bot(reddit, "OnePunchMan")
#Sleep for 10 seconds
		print("Sleeping for 10 seconds")
		time.sleep(10)


print("About to run bot")


if __name__ == "__main__":
	cache = []
	main()

