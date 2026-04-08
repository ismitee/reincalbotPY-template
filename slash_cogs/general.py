import discord
from discord.ext import commands
import time
from discord import app_commands

class SlashGeneral(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='ping', description='Check bot latency')
    async def slash_ping(self, interaction: discord.Interaction):
        """Slash ping command."""
        start_time = time.time()
        message = await interaction.response.send_message('Pong!')
        end_time = time.time()
        latency = round((end_time - start_time) * 1000)
        await interaction.edit_original_response(content=f'Pong! Latency: {latency} ms')

    @app_commands.command(name='hello', description='Say hello to a user')
    async def slash_hello(self, interaction: discord.Interaction):
        """Slash hello command."""
        await interaction.response.send_message(f'Hello {interaction.user.mention}! This is a slash command example.')

@app_commands.describe()  # Placeholder for future params

async def setup(bot):
    await bot.add_cog(SlashGeneral(bot))

