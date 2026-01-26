import asyncio
import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")

# Free but smart model
MODEL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

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
        response = requests.post(
            MODEL_URL,
            headers=headers,
            json=payload,
            timeout=30
        )
        data = response.json()

        # Normal successful response
        if isinstance(data, list) and len(data) > 0:
            answer = data[0].get("generated_text")
            if answer:
                await message.channel.send(answer.strip())
                return

        # Model loading or HF error
        if isinstance(data, dict) and "error" in data:
            await message.channel.send(
                "🧠 I’m waking up… try again in a few seconds!"
            )
            print("HF MODEL ERROR:", data)
            return

        # Fallback
        await message.channel.send("I couldn’t think of a good answer 🤔")
        print("HF RAW RESPONSE:", data)

    except Exception as e:
        print("HF AI ERROR:", repr(e))
        await message.channel.send(
            "My brain lagged a bit 😵 try again soon."
        )
