# main script for wabi token bot
import praw
import os
import time
from configparser import ConfigParser

# get reddit app and account information 
config = ConfigParser()
config.read("praw.ini")

# log into reddit account
reddit = praw.Reddit(**config["reddit_wabi"])


def comment_reply_text(comment):
	about_wabi = '''#####About WaBi Token\nWalimai, the company behind WaBi, is a company that develops solutions to ensure product authenticity. It places secure anti-counterfeit labels on consumer products in China and internationally.\n\nWalimai’s operations are mainly in China, which suffers from counterfeit in products such as baby formula, cosmetics, and alcohol. In order to solve this problem and provide confidence for consumers, the company has developed RFID labels with anti-reuse design, as well as mobile Apps that integrate with the labels.\n\nWalimai label is applied to the product at the point of origin and is scanned throughout the supply chain. After consumers purchase the products, they can scan the items with Walimai app, which would then show whether the product is original and the product’s previous locations and timestamp along the supply chain.'''

	wabi_links = '''* Company Website: https://www.walimai.com/\n* Token Website: https://www.wacoin.io/\n* Whitepaper: http://resources.wacoin.io/WaBI_Whitepaper_ENG.pdf'''

	about_me = " | ".join(["  \nI am a bot",
						   "[Feedback](https://www.reddit.com/message/compose/?to={[reddit_wabi][host_account]}&subject=WaBi%20Token%20Information%20Bot)".format(config),
						   "[Github](https://github.com/)"])

	comment.reply(about_wabi + "\n\n" + wabi_links + "\n\n" + "---" + "\n\n" + about_me)


# upvote all reddit submisisons in WaBiToken subreddit or any submisison in the list of subreddits with 'wabi' or 'walimai' in the title
def upvote_submissions(subreddit, submissions_upvoted):
	print("checking {0} submissions".format(subreddit))
	if subreddit == 'WaBiToken':
		for submission in reddit.subreddit(sub).new(limit=25):
			if submission.id not in submissions_upvoted:
				submission.upvote()
				submissions_upvoted.append(submission.id)
				with open("submissions_upvoted.txt", "a") as file:
					file.write(submission.id + "\n")
	else:
		for submission in reddit.subreddit(subreddit).new(limit=25):
			if 'wabi' or 'walimai' in submission.title.lower() and submission.id not in submissions_upvoted:
				submission.upvote()
				submissions_upvoted.append(submission.id)
				with open("submissions_upvoted.txt", "a") as file:
					file.write(submission.id + "\n")

def comment_reply(subreddit, comments_replied_to):
	print("checking {0} comments".format(subreddit))
	for comment in reddit.subreddit(subreddit).comments(limit=25):
		if "!WaBi" in comment.body and comment.id not in comments_replied_to and comment.author != reddit.user.me():
			comment_reply_text(comment)
			comments_replied_to.append(comment.id)
			with open("comments_replied_to.txt", "a") as file:
				file.write(comment.id + "\n")
			print("replied to comment")

# retrieve text file of replied comment ids 
def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as file:
			comments_replied_to = file.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = list(filter(None, comments_replied_to))
	return comments_replied_to

# retrieve text file of upvoted submission ids 
def get_upvoted_submissions():
	if not os.path.isfile("submissions_upvoted.txt"):
		submissions_upvoted = []
	else:
		with open("submissions_upvoted.txt", "r") as file:
			submissions_upvoted = file.read()
			submissions_upvoted = submissions_upvoted.split("\n")
			submissions_upvoted = list(filter(None, submissions_upvoted))
	return submissions_upvoted

def run_bot(subreddits):
	comments_replied_to = get_saved_comments()
	submissions_upvoted = get_upvoted_submissions()

	for sub in subreddits:	
		upvote_submissions(sub, submissions_upvoted)
		comment_reply(sub, comments_replied_to)

	print("taking a catnap..")
	time.sleep(10)


def run():
	subreddits = ['WabiToken', 'CryptoCurrencies', 'CryptoMarkets', 'Binance', 'ethtrader', 'CryptoTechnology'] 
	while True:
		run_bot(subreddits)

if __name__ == "__main__":
	run()

