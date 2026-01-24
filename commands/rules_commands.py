from discord.ext import commands
import discord
from data.rules import RULES

class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # !rules command
    @commands.command(name="rules")
    async def rules_prefix(self, ctx):
        rules_text = "**Server Rules:**\n"
        for rule in RULES:
            rules_text += f"{rule}\n"
        await ctx.send(rules_text)

    # /rules slash command
    @discord.app_commands.command(name="rules", description="View the server rules")
    async def rules_slash(self, interaction: discord.Interaction):
        rules_text = "**Server Rules:**\n"
        for rule in RULES:
            rules_text += f"{rule}\n"
        await interaction.response.send_message(rules_text)

async def setup(bot):
    await bot.add_cog(Rules(bot))

