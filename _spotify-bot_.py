import praw

reddit = praw.Reddit(
    client_id="8EaCuEEXWwUyueceGB_ESw",
    client_secret="_wYcW8EpRgufiAvsvxQubfQoBVlNIA",
    user_agent="web:reddit/spotify:1.0",
)
#Creates a read-only Reddit instance that passes auth info
#Adding Username and Password, would create an Authorized instance

subreddit = reddit.subreddit("askreddit")
#Obtains an instance of a subreddit (use r/all for multiple subs)

for submission in subreddit.hot(limit=10):
    print("***********")
    print(submission.title)
#For loop that sorts by Hot and prints the first ten titles

    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()

            if " song " in comment_lower:
                print(comment.body)
                print("-------------")
#For loop that iterates over the comments, makes it lower case