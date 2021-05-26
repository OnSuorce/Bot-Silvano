import discord
import settings
import json
import os
from itertools import cycle
from discord.ext import commands, tasks
from server_configs import server_configs
import time


intents = discord.Intents.default()
intents.members = True



status = cycle(settings.get_setting("status_pool"))
configs = server_configs

def get_prefix(client, message):
    prefixes = configs.get_prefixes()
    #prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(*prefixes[str(message.guild.id)])(client, message)
    #return  prefixes[str(message.guild.id)]
client = commands.Bot(command_prefix = get_prefix, help_command=None,intents=intents)

@tasks.loop(seconds = settings.get_setting("status_change_timer"))
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_guild_join(guild):
    if(str(guild.id) in configs.get_prefixes()):
        pass
    else:
        configs.add_guild(guild)
    
@client.event
async def on_member_join(member):
    guild = member.guild
    print(guild.id)
    roles_id = configs.get_autorole(guild.id)
    for id in roles_id:
        role = guild.get_role(int(id))
        print(role.name)
        await member.add_roles(role)

@tasks.loop(seconds=10)
async def troll():
    guild = await client.fetch_guild(829407559055704094)
    print(guild)
    channels = await guild.fetch_channels()
    print(channels)
    
    for channel in channels:
        if(channel.name == "Generale"):
            await channel.connect()
            time.sleep(3)
            await guild.voice_client.disconnect()


    #await guild.text_channels[0].send("ciao")
    
    

@client.event
async def on_ready():
    change_status.start()
    print("{0.user} attivo".format(client))
    #troll.start()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#configs.load()

try:
    client.run(settings.get_setting("token"))
except RuntimeError:
    print("ciao")
    client.close()