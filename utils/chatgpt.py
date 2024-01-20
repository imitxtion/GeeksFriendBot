from openai import AsyncOpenAI
from utils import secret_values

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