import discord
import settings
from discord.ext import commands

class Lol_commands(commands.Cog):
    def __init__(self,client):
        self.client = client



def setup(client):
    client.add_cog(Lol_commands(client))
