# bot.py
import os
import discord
import os

from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
#from discord_slash import SlashCommand

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="?", intents= discord.Intents.all())

@bot.event
async def on_message(message):
        if message.content == "ping":
                await message.channel.send("pong!")
@bot.event
async def on_ready():
        print("bot is up")
        try:
                synced = await bot.tree.sync()
                print("synced cock")
        except Exception as e:
                print(e)
        

@bot.tree.command(name="hello", description="Hi")
async def hello(interaction: discord.Interaction):
        await interaction.response.send_message("sup")

@bot.tree.command(name="trade", description="This command is to set up a trade thread with another user.")
async def trade(interaction:discord.Interaction):
        await interaction.response.send_message("Trade being set up...", ephemeral = True)
        channel = bot.get_channel(int(912552302764765206))
        print("Channel created")
        thread = await channel.create_thread(name="testthread")
        await thread.send("This is an example message")
        await thread.send(f"Hi <@{319182510548451329}>!")

bot.run(DISCORD_TOKEN)

