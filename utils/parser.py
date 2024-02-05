import asyncpraw

from utils import text, secret_values
 
async def get_news():
    reddit = asyncpraw.Reddit(
        client_id=secret_values.CLIENT_ID,
        client_secret=secret_values.CLIENT_SECRET,
        user_agent=secret_values.USER_AGENT
    )
    subreddit = await reddit.subreddit('animenews')
    result = text.anime_news
    counter = 1

    async for submission in subreddit.new(limit=10):
        result += f'\n<b>{counter}) {submission.title}</b>'
        result += f'\n<a href="{submission.url}">Read more</a>\n'
        counter += 1
    
    return result