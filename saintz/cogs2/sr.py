
import discord
from discord.ext import commands
import random
import requests

class sr(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="react",
        aliases  = ['r'],
        help = "changes your personal reaction",
        usage = "<emoji>"
    )
    async def react(self, ctx, react : str ):
        try: 
            self.react = react
            print (react)
            await ctx.message.add_reaction("👍")
        except Exception as e:
            await ctx.message.add_reaction("❌")
            print(e)

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:

            await msg.add_reaction(self.react)


async def setup(bot):
    await bot.add_cog(sr(bot))