import asyncio
import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")

# Free but smart model
MODEL_URL = "https://router.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

user_cooldowns = {}
COOLDOWN = 30  # seconds


async def handle_ai_message(message):
    user_id = message.author.id
    now = asyncio.get_event_loop().time()

    # Cooldown check
    if user_id in user_cooldowns and now - user_cooldowns[user_id] < COOLDOWN:
        await message.channel.send("Slow down 😄 give me a moment.")
        return

    user_cooldowns[user_id] = now

    # Extract question
    question = (
        message.content.lower()
        .replace("dowi", "")
        .replace(",", "")
        .strip()
    )

    if not question:
        await message.channel.send("Yes? What do you want to know?")
        return

    payload = {
        "inputs": f"Answer clearly and concisely: {question}",
        "parameters": {
            "max_new_tokens": 200
        }
    }

try:
    response = requests.post(MODEL_URL, headers=headers, json=payload, timeout=30)

    try:
        data = response.json()
    except ValueError:
        print("HF NON-JSON RESPONSE:", response.text)
        await message.channel.send("The AI didn’t respond properly 😵 try again.")
        return

    if isinstance(data, list) and len(data) > 0:
        answer = data[0].get("generated_text")
        if answer:
            await message.channel.send(answer.strip())
            return

    if isinstance(data, dict) and "error" in data:
        print("HF MODEL ERROR:", data)
        await message.channel.send("🧠 I’m warming up… try again shortly!")
        return

    await message.channel.send("I couldn’t think of a good answer 🤔")
    print("HF RAW RESPONSE:", data)

except Exception as e:
    print("HF AI ERROR:", repr(e))
    await message.channel.send("My brain lagged a bit 😵 try again soon.")
