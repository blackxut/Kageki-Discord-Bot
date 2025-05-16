# imports publics :
import discord
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

# 1. SETUP DU BOT

print("====================================")
print("Bot : Kageki / Version : 0.1")
print("====================================\n")


# On charge le fichier settings.env contenant nos variables d'environnement
load_dotenv(dotenv_path='settings.env')

# On va chercher la valeur DISCORD_TOKEN dans le fichier .env
DISCORD_TOKEN = getenv("TOKEN")
# Variable contenant l'ID de notre serveur
GUILD_ID = "guild-id"

# Créer un object Intents avec toutes les permissionss
intents = discord.Intents.all()
# Créer notre variable Client représentant le bot discord avec son préfixe et ses intentions
client = commands.Bot(command_prefix="!", intents=intents)
# Créer l'arbre de commande responsable de la gestion de toutes les commandes du bot discord
tree = client.tree

# 2. METHODES DU BOT

@client.event
async def on_ready():
    """
    Methode qui se lance lorsque le bot discord est en ligne 
    """
    print(f'\n[LOG] {client.user} est connecté à Discord')

    # PARAMETRE DU STATUT 
    # choix possibles : 
    #   online -> "en ligne" (par defaut) 
    #   idle -> "inactif" 
    #   dnd / do_not_disturb -> "ne pas deranger" 
    #   invisible -> "hors ligne"

    print("[LOG] Mise en place du statut discord")
    await client.change_presence(status=discord.Status.dnd)

    print("[LOG] Mise en place de l'arbre de commande")
    await client.tree.sync()

    print("[LOG] Setup terminé ! :D")
    print("\n============== HISTORIQUE ==============\n")

# Lancement du bot avec le token
client.run(DISCORD_TOKEN)