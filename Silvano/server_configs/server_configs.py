import json
import os

config_json = "./server_configs/servers.json"

with open(config_json, "r") as f:
        servers_json = json.load(f)


def load():
    with open(config_json, "r") as f:
        servers_json = json.load(f)


def get_json():
    return servers_json

template = {"id": "", "prefix": "!", "autorole": ""}

def add_guild( guild):
    tmp = template.copy()
    tmp["id"] = str(guild.id)
    tmp["prefix"] = "!"
    servers_json.append(tmp)
    dump_json()

def update_prefix(guild_id, prefix):
    #a = []
    for item in servers_json:
        #a.append(item)
        if(item["id"] == str(guild_id)):
            item["prefix"] = prefix
            ind = servers_json.index(item)
            servers_json[ind] = item
            dump_json()
            return item
def update_troll(guild_id, status):
    for item in servers_json:
        #a.append(item)
        
        if(item["id"] == str(guild_id)):
            #print(item["troll"])
            item["troll"] = status
    
    dump_json()

def update_autorole(guild_id, roles):
    roles_id = []
    for role in roles:
        roles_id.append(str(role.id))
    print(roles_id) 
    print(guild_id)
    for item in servers_json:
        #a.append(item)
        
        if(item["id"] == str(guild_id)):
            
            item["autorole"] = roles_id
    dump_json()
    
def get_autorole(guild_id):
    roles = []
    for item in servers_json:
       
        if(item["id"] == str(guild_id)):
            print(item)
            roles = item["autorole"]
    return roles

def get_enabled_trolls():
    guilds = []
    for guild in servers_json:
        if guild["troll"] == True:
            guilds.append(guild["id"])
    return guilds

def get_prefixes():
    prefixes = {}

    for guild in servers_json:
        
        prefixes[guild["id"]] = guild["prefix"]
    return prefixes

def dump_json():
    with open(config_json, "w") as f:
        json.dump(servers_json, f)
