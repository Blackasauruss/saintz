import discord, os
from discord.ext import commands



bot = commands.Bot(command_prefix=".", self_bot = True)

COGS_FOLDER = "cogs2"

y = "✅"
x = "❌"
@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

    # loads all cogs o rusm 
    for filename in os.listdir(COGS_FOLDER):
        if filename.endswith(".py"):
            cog_name = filename[:-3]  # remove py
            try:
                await bot.load_extension(f"cogs2.{cog_name}")
                print(f"loaded cog: {cog_name}")
            except Exception as e:
                print(f"failed to load cog {cog_name}: {e}")

sick = ""
bot.run(sick)
