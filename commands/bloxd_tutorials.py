from discord.ext import commands
import discord

# Tutorial texts
TUTORIALS = {
    "bedwars": "🛏 **Bedwars Tutorial**\n**• Goal :** Protect your bed while destroying enemy beds so they can no longer respawn.\n**• How it works :** Each team starts on an island with a bed. As long as your bed is alive, you can respawn. Once it’s broken, death is permanent.\n**• Tips :** Collect iron, diamonds, and moonstone quickly. Upgrade your team’s generator, armor, and tools. Defend your bed with blocks, communicate with teammates, and attack enemy beds when they are distracted.\n**• Gameplan :** Get around 50–60 blocks maximum and immediately bridge or rush your nearest enemy to eliminate them early. After the first rush, upgrade your armor and sword, then grab more blocks. Go to mid to collect moonstone and diamonds, then rush the next closest enemy team. Always stay alert so enemies can’t knock you off bridges or attack from behind. After eliminating the second team, upgrade your team’s protection and damage. From there, keep rushing other teams quickly and try to control mid so no one else can gear up.",

    "skywars": "☁️ **Skywars Tutorial**\n**• Goal :** Be the last player standing on floating islands.\n**• How it works :** Players spawn on separate islands with loot chests. The map has a central island with better gear.\n**• Tips :** Loot your island fast, equip armor and weapons immediately, and use blocks to bridge carefully. Watch your surroundings to avoid being knocked off, use projectiles to knock enemies into the void, and go to mid for stronger loot if it’s safe.\n**• Gameplan :** Loot the chest on top of your island immediately, then rush the nearest player as fast as possible. After eliminating them, head straight to mid and eliminate enemies along the way. Always try to attack by surprise so opponents don’t have time to lower your health by alot. Aim to be the first player at mid to secure the best loot. Once mid is fully looted, move island to island in a strategic way, watching your surroundings, and eliminate the remaining enemies.",

    "survival": "🌳 **Survival Tutorial**\n**• Goal :** Survive as long as possible by gathering resources, crafting items, and exploring the world.\n**• How it works :** You start with nothing and must rely on the environment. Mobs spawn at night and can attack you.\n**• Tips :** Punch trees to get wood, craft basic tools, and build a shelter before night. Gather food to avoid starvation, mine for better resources, and craft armor to survive tougher enemies. \n**• Gameplan :** When you join, get an x-ray texture pack if allowed (can also be done without). Run far away from spawn to avoid early danger, then collect wood to craft basic tools. Mine stone and upgrade your tools, then start mining efficiently by finding caves and ores to get iron armor. Set up a hidden base under bedrock or high in the air (ground bases are possible but less safe). Gather food like steak, wheat, and pork to stay prepared. Once geared, return to spawn to outplay weaker players or use spike boot + glider strategy to eliminate enemies. From there, keep progressing by upgrading armor, tools, and food to stay ahead.",

    "one block": "🟦 **One Block Tutorial**\n**• Goal :** Survive and expand your island by mining a single regenerating block.\n**• How it works :** The block regenerates into different materials, mobs, and chests as you progress through phases.\n**• Tips :** Mine carefully so you don’t fall into the void. Save useful blocks, craft tools early, and manage mobs safely. Expand your island gradually and prepare for harder phases.\n**• Gameplan :** Start by carefully mining the block while making sure you don’t fall into the void. Use early blocks to expand your island and craft basic tools. Save useful materials and open chests when needed. As phases progress, prepare for hostile mobs by crafting weapons and armor. Build a small but safe base and storage area. Continue mining to unlock better resources, upgrade your tools and armor, and expand your island and base to stay safe and organized while building your own empire.",

    "99 nights in a forest": "🌲 **99 Nights in a Forest Tutorial**\n**• Goal :** Survive all 99 nights while facing increasingly difficult enemy waves.\n**• How it works :** Enemies become stronger each night, forcing you to improve your gear and defenses. Finding kids helps you skip days and progress faster.\n**• Tips :** Gather wood, stone, and food during the day. Build a secure base and add spikes around the campfire, craft weapons and armor, and keep healing items ready. Upgrade defenses often to survive later nights.\n**• Gameplan :** Start by gathering basic resources like wood, stone, and food during the day. Build a safe base early, preferably fortified or hard to reach. Prepare weapons and armor before nightfall to survive enemy waves. While exploring, search for the 5 lost kids hidden around the map each kid found will skip some days, making progression faster. Balance fighting enemies and exploring carefully. Upgrade gear, defenses, and healing items as nights get harder, and stay prepared for constant combat.",

    "ranked duels": "⚔️ **Ranked Duels Tutorial**\n**• Goal :** Win 1v1 fights to gain ELO and climb the leaderboard.\n**• How it works:** Players fight with equal or preset kits, and winning increases your ELO while losing decreases it.\n**• Tips:** Master PvP mechanics like strafing and combos. Learn your kit, manage cooldowns, and stay calm under pressure. Consistent wins help you climb the ranks faster.\n**• Gameplan :** Learn your kit before fighting and know when to attack or play defensive. Focus on movement, timing, and landing consistent hits rather than rushing blindly. Try to control the fight by keeping pressure on your opponent while avoiding unnecessary damage. Stay calm, watch your opponent’s patterns, and punish mistakes. Consistent wins will help you gain ELO faster."

}

class BloxdTutorials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Prefix commands (!bedwars, !skywars, etc.)
    @commands.command(name="bedwars")
    async def bedwars_prefix(self, ctx):
        await ctx.send(TUTORIALS["bedwars"])

    @commands.command(name="skywars")
    async def skywars_prefix(self, ctx):
        await ctx.send(TUTORIALS["skywars"])

    @commands.command(name="survival")
    async def survival_prefix(self, ctx):
        await ctx.send(TUTORIALS["survival"])

    @commands.command(name="oneblock")
    async def oneblock_prefix(self, ctx):
        await ctx.send(TUTORIALS["one block"])

    @commands.command(name="99nights")
    async def nights_prefix(self, ctx):
        await ctx.send(TUTORIALS["99 nights in a forest"])

    @commands.command(name="rankedduels")
    async def rankedduels_prefix(self, ctx):
        await ctx.send(TUTORIALS["ranked duels"])

    # Slash commands
    @discord.app_commands.command(name="bedwars", description="Bedwars tutorial")
    async def bedwars_slash(self, interaction: discord.Interaction):
        await interaction.response.send_message(TUTORIALS["bedwars"])

    @discord.app_commands.command(name="skywars", description="Skywars tutorial")
    async def skywars_slash(self, interaction: discord.Interaction):
        await interaction.response.send_message(TUTORIALS["skywars"])

    @discord.app_commands.command(name="survival", description="Survival tutorial")
    async def survival_slash(self, interaction: discord.Interaction):
        await interaction.response.send_message(TUTORIALS["survival"])

    @discord.app_commands.command(name="oneblock", description="One Block tutorial")
    async def oneblock_slash(self, interaction: discord.Interaction):
        await interaction.response.send_message(TUTORIALS["one block"])

    @discord.app_commands.command(name="99nights", description="99 Nights in a Forest tutorial")
    async def nights_slash(self, interaction: discord.Interaction):
        await interaction.response.send_message(TUTORIALS["99 nights in a forest"])

    @discord.app_commands.command(name="rankedduels", description="Ranked Duels tutorial")
    async def rankedduels_slash(self, interaction: discord.Interaction):
        await interaction.response.send_message(TUTORIALS["ranked duels"])


async def setup(bot):
    await bot.add_cog(BloxdTutorials(bot))
