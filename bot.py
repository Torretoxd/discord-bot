import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from data.rules import RULES
from data.bloxd_faq import BLOXD_FAQ

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
    "commands.bloxd_tutorials",  # <-- NEW
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

# DM Help Center
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        content = message.content.lower()

        # Rules
        if "rules" in content or "server" in content:
            rules_text = "**Server Rules:**\n"
            for i, rule in enumerate(RULES, start=1):
                rules_text += f"{i}. {rule}\n"
            await message.channel.send(rules_text)
            return

        # Bloxd FAQ
        for q, a in BLOXD_FAQ.items():
            if q in content:
                await message.channel.send(a)
                return

        await message.channel.send(
            "I can help with **server rules** or **Bloxd.io questions**.\n"
            "Try asking something specific 🙂"
        )

    await bot.process_commands(message)

# Start bot
bot.run(TOKEN)
