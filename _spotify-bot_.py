import praw

reddit = praw.Reddit(
    client_id="8EaCuEEXWwUyueceGB_ESw",
    client_secret="_wYcW8EpRgufiAvsvxQubfQoBVlNIA",
    user_agent="web:reddit/spotify:1.0",
)

subreddit = reddit.subreddit("askreddit")

for post in subreddit.hot(limit=10):
    print("")
    print(post.title)