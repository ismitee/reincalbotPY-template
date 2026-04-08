import discord
from discord.ext import commands
import time

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Ping latency command."""
        start_time = time.time()
        message = await ctx.send('Pong!')
        end_time = time.time()
        latency = round((end_time - start_time) * 1000)
        await message.edit(content=f'Pong! Latency: {latency} ms')

    @commands.command(name='hello')
    async def hello(self, ctx):
        """Example command - feel free to add your own!"""
        await ctx.send(f'Hello {ctx.author.mention}! This is an example command.')

async def setup(bot):
    await bot.add_cog(General(bot))

