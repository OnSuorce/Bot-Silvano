import discord
import settings
import json
from server_configs import server_configs
from discord.ext import commands
from discord import FFmpegPCMAudio
import os
import random

class Config_commands(commands.Cog):

    configs = server_configs
    def __init__(self, client):
        self.client = client
        #self.configs = configs
    
    @commands.command()
    async def setprefix(self,ctx,arg): 
        a = self.configs.update_prefix(ctx.guild.id, arg)
        await ctx.send(f"Prefix changed to: {arg}")
    
    @commands.command()
    async def setautorole(self, ctx):
        role_mentions = ctx.message.role_mentions
        self.configs.update_autorole(ctx.guild.id, role_mentions)
        await ctx.send(self.configs.get_autorole(ctx.guild.id))
        
    @commands.command()
    async def settroll(self,ctx,arg):
        if(arg.lower() == "true"):
            self.configs.update_troll(ctx.guild.id, True)
        elif(arg.lower() == "false"):
            self.configs.update_troll(ctx.guild.id, False)
        else:
            await ctx.send("Argument should be false or true")

    @commands.command()
    async def prefix(self, ctx):
        prefixes = self.configs.get_prefixes()
        await ctx.send(f"This server's prefix is: {prefixes[str(ctx.guild.id)]}")

    
def setup(client):
    client.add_cog(Config_commands(client))