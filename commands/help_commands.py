from discord.ext import commands

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command(name="help")
async def help_command(self, ctx):
    await ctx.send(
        "**Help Center**\n"
        "• `!help` – Show this message\n"
        "• `!rules` – Server rules\n"
        "• `!bloxdfaq` – Bloxd.io general help\n"
        "• `!bedwars` – Bedwars tutorial\n"
        "• `!skywars` – Skywars tutorial\n"
        "• `!survival` – Survival tutorial\n"
        "• `!oneblock` – One Block tutorial\n"
        "• `!99nights` – 99 Nights in a Forest tutorial\n"
        "• `!rankedduels` – Ranked Duels tutorial\n"
        "You can also DM me questions!"
    )

    @commands.command(name="serverfaq")
    async def server_faq(self, ctx):
        await ctx.send(
            "**Server FAQ**\n"
            "1️⃣ Be respectful\n"
            "2️⃣ No spamming\n"
            "3️⃣ Have fun!"
        )

async def setup(bot):
    await bot.add_cog(HelpCommands(bot))
