# bot.py
import os
import discord
import os

from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from discord_slash import SlashCommand, SlashContext

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
                print("synced")
        except Exception as e:
                print(e)


class onOff(commands.Converter):
        async def convert (self, ctx, argument):
                if argument.lower() =="on":
                        return True
                elif argument.lower()=="off":
                        return False
                else:
                        raise commands.BadArgument("Invalid input. Please enter 'on' or 'off'.")              
                        



@slash.slash(name="mhiatus", description="Hiatus commands for Mods")
async def mhaitus(ctx: SlashContext, option: YesOrNoConverter):
        modID = interaction.user.id
        onHiatusRoleID = discord.utils.get(ctx.guild.roles, id=ENTERID)
        modRoleID = discord.utils.get(ctx.guild.roles, id=ENTERID)
        
        if option and modRoleID in user.roles:
                await interaction.response.send_Message(f"Mod <@{modID}> is going on Hiatus.")
        elif option and onHiatusRoleID in user.roles:
                await interaction.response.send_Message(f"Error: You already are on Hiatus. Try using the parameter off instead.")
        

        if not option and modRoleID in user.roles:
                await interaction.response.send_Message(f"Mod <@{modID}> is going off Hiatus.")
        elif not option and onHiatusRoleID in user.roles:
                await interaction.response.send_Message(f"Error: You already are off Hiatus. Try using the parameter on instead.")



@bot.tree.command(name="hello", description="Hi")
async def hello(interaction: discord.Interaction):
        await interaction.response.send_message("sup")

@bot.tree.command(name="trade", description="This command is to set up a trade thread with another user.")
@bot.tree.describe(
tradeUser="The User you want to trade with."


)

async def trade(
        interaction:discord.Interaction,
        tradeUser:discord.Member,               
                ):
        

        await interaction.response.send_message("Trade being set up...", ephemeral = True)
        channel = bot.get_channel(int(912552302764765206))
        print("Channel created")
        thread = await channel.create_thread(name="testthread")
        
        await thread.send("This is an example message")
        await thread.send(f"User <@{interaction.user.id}> set up a trade with <@{interaction.user.id}>!")
        

bot.run(DISCORD_TOKEN)

