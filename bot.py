import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from data.rules import RULES
from data.bloxd_faq import BLOXD_FAQ
from data.smart_answers import SMART_ANSWERS

# Load token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Bot
bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

# Extensions (cogs)
initial_extensions = [
    "commands.help_commands",
    "commands.bloxd_commands",
    "commands.rules_commands",
    "commands.bloxd_tutorials",
]

@bot.event
async def on_ready():
    for ext in initial_extensions:
        await bot.load_extension(ext)

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(e)

    print(f"{bot.user} is online and ready!")

# Welcome DM
@bot.event
async def on_member_join(member):
    try:
        await member.send(
            f"Welcome {member.name}!\n"
            "Use !help or /help to get started.\n"
            "You can also DM me questions about the server or Bloxd.io!"
        )
    except discord.Forbidden:
        pass

# Message handler
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    # --- Smart Answer System (works in DMs + servers) ---
    best_match = None
    best_length = 0

    for entry in SMART_ANSWERS:
        for keyword in entry["keywords"]:
            if keyword in content and len(keyword) > best_length:
                best_match = entry["answer"]
                best_length = len(keyword)

    if best_match:
        await message.channel.send(best_match)
        return




    # --- DM Auto-responder ---
    if isinstance(message.channel, discord.DMChannel):

        # Rules
        if "rules" in content or "server" in content:
            rules_text = "**Server Rules:**\n"
            for rule in RULES:
                rules_text += f"{rule}\n"
            await message.channel.send(rules_text)
            return

        # Bloxd FAQ
        for q, a in BLOXD_FAQ.items():
            if q in content:
                await message.channel.send(a)
                return

        # Fallback
        await message.channel.send(
            "I can help with **server rules**, **Bloxd.io**, or **BedWars**.\n"
            "Try asking something specific 🙂"
        )
        return

    # Let normal commands work
    await bot.process_commands(message)

# Start bot
bot.run(TOKEN)