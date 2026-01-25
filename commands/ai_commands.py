import discord
import asyncio
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Cooldowns per user
user_cooldowns = {}
COOLDOWN = 30  # seconds

async def handle_ai_message(message):
    user_id = message.author.id
    now = asyncio.get_event_loop().time()

    # Rate limit
    if user_id in user_cooldowns and now - user_cooldowns[user_id] < COOLDOWN:
        await message.channel.send(
            "Please wait a bit before asking another question 😉"
        )
        return

    user_cooldowns[user_id] = now

    # Remove trigger word
    question = message.content.lower().replace("dowi", "").replace(",", "").strip()
    if not question:
        await message.channel.send("Yes? What’s your question?")
        return

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Dowi, a helpful Bloxd.io assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=150,
            temperature=0.7
        )

        answer = response.choices[0].message.content
        await message.channel.send(answer)

    except Exception as e:
        print("AI ERROR:", repr(e))
        await message.channel.send(
            "⚠️ AI error occurred.\n"
            "The owner should check the Railway logs."
        )