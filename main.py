# public imports
import discord
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
import mysql.connector
import random
import time

# private imports
from embedMessages import embed_info, embed_leaderboard, embed_accusation
from weatherAPI import getAqi
from sqlRequests import getLeaderboard

# 1. SETUP

print("====================================")
print("Bot : Kageki / Version : 0.1")
print("====================================\n")

# loeading env file 
load_dotenv(dotenv_path='.env')

# looking for the attributes inside the .env file
DISCORD_TOKEN = getenv("DISCORD_TOKEN")
DISCORD_AUTHOR = getenv("DISCORD_AUTHOR")
DISCORD_BOT = getenv("DISCORD_BOT")

httpCode = [100,101,102,103,200,201,202,203,204,205,206,207,
            208,214,226,300,301,302,303,304,305,307,308,400,
            401,402,403,404,405,406,407,408,409,410,411,412,
            413,414,415,416,417,418,419,420,421,422,423,424,
            425,426,427,428,429,431,444,450,451,495,496,497,
            498,499,500,501,502,503,504,506,507,508,509,510,
            511,521,522,523,525,530,599]

# create an object with all intents
intents = discord.Intents.all()
# create a variable storing the bot's prefix and permissions (intents)
client = commands.Bot(command_prefix="!", intents=intents)
# tree that store all slash commands
tree = client.tree

# 2. METHODES DU BOT

def log(name:str,interaction:discord.Interaction):
    """
    Method used for debugging purposes with basic logging
    """
    current = datetime.now()
    current_time = current.strftime("%H:%M:%S")
    # in private message
    if interaction.guild is None:
        print(f"[{current_time}]  Private message > {interaction.user.name} > {name}")
    # in a server
    else:
        print(f"[{current_time}]  {interaction.guild} > {interaction.user.name} > {name}")

@client.event
async def on_ready():
    """
    Function launched when the bot is started
    """
    print(f'\n[LOG] {client.user} is connected to Discord')

    # PARAMETRE DU STATUT 
    # choices : 
    #   online (default) 
    #   idle 
    #   dnd / do_not_disturb 
    #   invisible

    print("[LOG] Setting discord's status")
    await client.change_presence(activity=discord.Streaming(url="https://www.google.com/",name="𝑾𝒂𝒕𝒄𝒉𝒊𝒏𝒈 𝒕𝒉𝒆 𝒓𝒂𝒊𝒏 ☔"),status=discord.Status.dnd)

    print("[LOG] Loading tree commands")
    await client.tree.sync()

    print("[LOG] setup finished")
    print("\n============== HISTORIQUE ==============\n")

@client.event
async def on_message(message):
    """
    Function launched for every message sent
    """

    # ignore all messages from our bot
    if message.author == client.user:
        return
    
    print(f"[MESSAGE] {message.author} : {message.content}")
    return

@client.tree.command(name="rain",description="if you ask for the rain, you shall receive")
async def slash_command(interaction:discord.Interaction):
    
    log("/rain",interaction)
    file = 'assets/gif/rain.gif'
    with open(file, 'rb') as fp:
        return await interaction.response.send_message(file=discord.File(fp, file))

@client.tree.command(name="http-code",description="what HTTP code will you get ?")
async def slash_command(interaction:discord.Interaction):
    
    log("/http-code",interaction)
    return await interaction.response.send_message("https://http.cat/" + str(random.choice(httpCode)))

@client.tree.command(name="avatar",description="show the user's avatar")
async def slash_command(interaction:discord.Interaction,member:discord.Member):

    log("/avatar",interaction)
    return await interaction.response.send_message(member.display_avatar)

@client.tree.command(name="info",description="describe an user")
async def slash_command(interaction:discord.Interaction,member:discord.Member):
    
    log("/info",interaction)
    return await interaction.response.send_message(embed=embed_info(interaction,member))

@client.tree.command(name="air-quality",description="get the air's quality of a city")
async def slash_command(interaction:discord.Interaction,city:str):

    log("/air-quality",interaction)
    result = getAqi(city)
    if result[0] == -1:
        return await interaction.response.send_message(f":warning: Error : `{result[1]}`")
    else:
        return await interaction.response.send_message(f"The air quality of {city} is : `{result[1]}` ({result[0]})")

@client.tree.command(name="leaderboard",description="display the current leaderboard")
async def slash_command(interaction:discord.Interaction):
    log("/leaderboard",interaction)
    result = getLeaderboard()
    if result is None:
        await interaction.response.send_message("Something went wrong :thinking:")
    else:
        await interaction.response.send_message(embed=embed_leaderboard(result))

# starting the bot with his secret token
client.run(DISCORD_TOKEN)