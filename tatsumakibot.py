import praw
import time
from praw.exceptions import APIException


def authenticate():
	print("Authenticating...")
	reddit = praw.Reddit(
						 'TatsuBot',
						 user_agent="Tatsumaki comment responder v0.3")
	print("Authenticated as {}!".format(reddit.user.me()))
	return reddit


def run_bot(reddit, subreddit_name):
	print("Obtaining 25 comments...")
	for comment in reddit.subreddit(subreddit_name).comments(limit = 25):
		lowercase_comment = comment.body.lower()
		try:
			if "sassy lost child" in lowercase_comment and comment.id not in cache and comment.author != reddit.user.me():
				print('String with "sassy lost child" found.' + comment.id)
				comment.reply("I'm not a sassy lost child!")
				print("Replied to comment" + comment.id)
				cache.append(comment.id)
	
			if "Tatsu" in lowercase_comment and comment.id not in cache and comment.author != reddit.user.me():
				comment.reply("It's Tatsumaki, not Tatsu you octopus!")
				print("Replied to comment" + comment.id)
				cache.append(comment.id)
			
			if "brat" in lowercase_comment and comment.id not in cache and comment.author != reddit.user.me():
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
				comment.reply("Of course I am best girl! Not that I'd be into any of you...")
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

