from openai import AsyncOpenAI
from utils import secret_values
from utils import text

client = AsyncOpenAI(api_key=secret_values.OPENAI_API_KEY)

async def generate_answer(user_message):
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{user_message}",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

async def generate_hashtags(vid_theme):
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{text.tt_generate_tags_prompt.format(vid_theme=vid_theme)}",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content