import asyncio
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='p!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has logged in!')
    print(f'Loaded cogs: {len(bot.cogs)}')
    
    synced = await bot.tree.sync()
    print(f'Synced {len(synced)} slash command(s)')
    
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.custom,
            name="custom",
            state="TorangPunya - use p!help or /help"
        )
    )

# Load cogs
async def load_cogs():
    for folder in ['./cogs', './slash_cogs']:
        for filename in os.listdir(folder):
            if filename.endswith('.py'):
                if folder == './slash_cogs':
                    extension = f'slash_cogs.{filename[:-3]}'
                else:
                    extension = f'cogs.{filename[:-3]}'
                try:
                    await bot.load_extension(extension)
                    print(f'Loaded extension {extension}')
                except Exception as e:
                    print(f'Failed to load extension {extension}: {e}')

async def main():
    async with bot:
        await load_cogs()
        token = os.getenv('BOT_TOKEN')
        if not token:
            raise ValueError('BOT_TOKEN not found in .env file!')
        await bot.start(token)

if __name__ == '__main__':
    asyncio.run(main())

