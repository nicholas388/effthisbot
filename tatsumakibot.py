import praw
import time
import os


def authenticate():
	print("Authenticating...")
	reddit = praw.Reddit(
						 'TatsuBot',
						 user_agent="Tatsumaki comment responder v0.3")
	print("Authenticated as {}!".format(reddit.user.me()))
	return reddit


def run_bot(reddit, comments_replied_to, subreddit_name):
	print("Obtaining 25 comments...")
	for comment in reddit.subreddit(subreddit_name).comments(limit = None):
		lowercase_comment = comment.body.lower()
		if "sassy lost child" in lowercase_comment and comment.id not in comments_replied_to and comment.author != reddit.user.me():
			print('String with "sassy lost child" found.' + comment.id)
			comment.reply("I'm not a sassy lost child!")
			print("Replied to comment" + comment.id)
			comments_replied_to.append(comment.id)
			with open("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

		if "Tatsu" in lowercase_comment and comment.id not in comments_replied_to and comment.author != reddit.user.me():
			print('String with "Tatsu" found.' + comment.id)
			comment.reply("It's Tatsumaki, not Tatsu you octopus!")
			print("Replied to comment" + comment.id)
			comments_replied_to.append(comment.id)
			with open("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")
		
		if "brat" in lowercase_comment and comment.id not in comments_replied_to and comment.author != reddit.user.me():
			print('String with "brat" found.' + comment.id)
			comment.reply("Who do you think you are calling brat")
			print("Replied to comment" + comment.id)
			comments_replied_to.append(comment.id)
			with open("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")
		
		if "spoilt brat" in lowercase_comment and comment.id not in comments_replied_to and comment.author != reddit.user.me():
			print('String with "spoilt brat" found.' + comment.id)
			comment.reply("Unforgivable. Me, a brat? I'm older than you!")
			print("Replied to comment" + comment.id)
			comments_replied_to.append(comment.id)
			with open("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")
		
		if "best girl" in lowercase_comment and comment.id not in comments_replied_to and comment.author != reddit.user.me():
			print('String with "best girl" found.' + comment.id)
			comment.reply("Of course I am best girl! Not that I'd be into any of you...")
			print("Replied to comment" + comment.id)
			comments_replied_to.append(comment.id)
			with open("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")
				
				# subreddit = reddit.subreddit(subreddit_name)
				#
				# for submission in subreddit.get_new(limit=100):
				#     title = submission.title
				#     normal=title.lower()
				#     if "Tatsumaki" in normal:
				#         print("fuck")
				
				# for submission in subreddit.stream.submissions():
				#     lowercase_title = submission.title.lower()
				#     print(lowercase_title)
				
				
	#Sleep for 10 seconds
	print("Sleeping for 10 seconds")
	time.sleep(10)


def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = list(filter(None, comments_replied_to))
	return comments_replied_to


def main():
	reddit = authenticate()
	comments_replied_to = get_saved_comments()
	print(comments_replied_to)
	#active
	while True:
		run_bot(reddit, comments_replied_to, "MemeTuesday")



print("About to run bot")

if __name__ == "__main__":
	main()


# for submission in hot_one:
#     if not submission.stickied:
#         print("{}, {}, {}, {}".format(submission.title, submission.ups, submission.downs, submission.visited))

