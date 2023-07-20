# bot.py
import os
import discord
import os
import discord_slash

from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from discord_slash import SlashCommand, SlashContext

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="?", intents= discord.Intents.all())
#slash = discord_slash.SlashCommand(bot, sync_commands=True) 

class onOffConverter(commands.Converter):
        async def convert (self, ctx, argument):
                if argument.lower() =="on":
                        return True
                elif argument.lower()=="off":
                        return False
                else:
                        raise commands.BadArgument("Invalid input. Please enter 'on' or 'off'.") 

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

@bot.tree.command(name="mhiatus", description="Hiatus commands for Mods")
@app_commands.describe(action="Type 'On' or 'Off' to enable or disable hiatus.")
async def mhaitus(ctx: commands.Context, *, action: str):
        modID = ctx.user.id
        modRole = discord.utils.get(ctx.guild.roles, id=1131388396061855765)
        hiatusRole = discord.utils.get(ctx.guild.roles, id=1131388455759396914)
        if action.lower() == "on" and modRole in ctx.user.roles:
        # Perform the 'on' action
                await ctx.response.send_message(f"Hiatus is turned on for <@{modID}>", ephemeral = False)
                await ctx.user.add_roles(hiatusRole)
                await ctx.user.remove_roles(modRole)
        elif action.lower() == "on" and hiatusRole in ctx.user.roles:
                await ctx.response.send_message("Hiatus is already enabled, select 'off' to disable hiatus.", ephemeral = True)

        elif action.lower() == "off" and hiatusRole in ctx.user.roles:
        # Perform the 'off' action
                await ctx.response.send_message(f"Hiatus is turned off for <@{modID}>", ephemeral = False)
                await ctx.user.add_roles(modRole)
                await ctx.user.remove_roles(hiatusRole)
        elif action.lower() == "off" and modRole in ctx.user.roles:
                await ctx.response.send_message("Hiatus is already off, select 'on' to disable hiatus.", ephemeral = True)
                
        elif action.lower() == "off" or action.lower() == "on":
                await ctx.response.send_message("This command is for moderators only.", ephemeral = True)
                
        else:
                await ctx.response.send_message("Please enter 'On' or 'Off' for hiatus options.", ephemeral = True)

@mhaitus.error
async def mhaitus_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.response.send_message(error, ephemeral=True)

        
@bot.tree.command(name="hello", description="Hi")
async def hello(interaction: discord.Interaction):
        await interaction.response.send_message("sup")

@bot.tree.command(name="trade", description="This command is to set up a trade thread with another user.")
async def trade(ctx: commands.Context, target: discord.Member):
        initiator = ctx.user.id
        participant = target.id
        await ctx.response.send_message("Trade being set up...", ephemeral = True)
        channel = bot.get_channel(int(1131393762413793443))
        print("Channel created")
        thread = await channel.create_thread(name="active-trade")
        await thread.send(f"<@{initiator}> started a trade with <@{participant}>!")
        

bot.run(DISCORD_TOKEN)

