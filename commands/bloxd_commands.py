from discord.ext import commands

class BloxdCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bloxdfaq")
    async def bloxd_faq(self, ctx):
        await ctx.send(
            "**Bloxd.io FAQ**\n"
            "🔹 Play at https://bloxd.io\n"
            "🔹 Earn coins by playing matches\n"
            "🔹 Practice to improve your skills"
        )

async def setup(bot):
    await bot.add_cog(BloxdCommands(bot))