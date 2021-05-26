import discord
import settings
from discord.ext import commands
from discord import FFmpegPCMAudio
import os
import random
from random_italian_person import RandomItalianPerson
import wikipedia

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Pong")
   
    #@commands.command()
    #async def prova(self, ctx, member: discord.Member):
        
        
       
        
    @commands.command()
    async def randomperson(self, ctx):
        person = RandomItalianPerson()
        print(person.describe())
        await  ctx.send(person.describe())
    
    @commands.command()
    async def wiki(self,ctx, arg):
        x = wikipedia.summary(arg)
        await ctx.send(x)

    @commands.command()
    async def lolstats(self, ctx, name, region):
        link = f"https://www.leagueofgraphs.com/summoner/{region.lower()}/{name}"
        await ctx.send(link)

    @commands.command()
    async def ciao(self, ctx):
        if(ctx.voice_client is not None and ctx.voice_client.is_playing()):
            await ctx.send(f"{ctx.message.author.mention}Wait for the audio to finish")
            return
        if(ctx.author.voice):
            channel = ctx.message.author.voice.channel
            if(ctx.voice_client is not None):
                await ctx.voice_client.move_to(channel)
            else:
                await channel.connect()
            
            #voice = await channel.connect()
            audios = ["ciao.mp3", "brcock.mp3"]
            #for filename in os.listdir('./audios'):
            #    if filename.endswith('.mp3'):
            #        audios.append(filename)
            r = random.randint(0, len(audios)-1)
            source = FFmpegPCMAudio(executable= r"C:/ffmpeg/ffmpeg.exe",source=f"./audios/{audios[r]}")
            player =  ctx.voice_client.play(source)
            
        else:
            await ctx.send(f"{ctx.author.mention} ciao!")

    @commands.command()
    async def purge(self, ctx, amount,):

       channel = ctx.channel
       await channel.purge(limit=int(amount))
    
    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        avatar = discord.Embed()
        avatar.set_image(url=member.avatar_url)
        await ctx.send(embed=avatar)
    
    @commands.command()
    async def random(self,ctx, min: int, max: int):
        print(type(min))
        r = random.randint(min,max)
        print(r)
        await ctx.send(f"Numero: {r}")
    
    @commands.command()
    async def randomsacchi(self, ctx):
        
        if(ctx.voice_client is not None and ctx.voice_client.is_playing()):
            await ctx.send(f"{ctx.message.author.mention} Wait for the audio to finish")
            return

        if(ctx.author.voice):
            channel = ctx.message.author.voice.channel

            if(ctx.voice_client is not None):
                await ctx.voice_client.move_to(channel)
            else:
                await channel.connect()

            
            
            audios = []
            for filename in os.listdir('./audios'):
                if filename.endswith('.mp3'):
                    audios.append(filename)
            
            print(audios)
            r = random.randint(0, len(audios)-1)
            source = FFmpegPCMAudio(executable= r"C:/ffmpeg/ffmpeg.exe",source=f"./audios/{audios[r]}")
            player =  ctx.voice_client.play(source)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title = "Bot commands", colour=discord.Colour(5).random())
        file = discord.File("./gifs/sacchi.gif")
        embed.set_thumbnail(url = "attachment://sacchi.gif")
        commands_dict = settings.get_setting("commands")
        key_list = list(commands_dict.keys())
        val_list = list(commands_dict.values())
        for n in range(len(key_list)):
            embed.add_field(name=key_list[n], value=val_list[n],inline=False)

        
        embed.set_image(url = "attachment://sacchi.gif")
        #embed.add_field(name="Help", value="valore")
        #embed.add_field(name=f"{embed.author}",value="sss")
        await ctx.send(file = file,embed=embed)    
    
    @commands.command()
    async def join(self,ctx):
        if(ctx.author.voice is None):
            await ctx.send(f"{ctx.author.mention} You are not connected to a voice chat")
            return
        channel = ctx.message.author.voice.channel
        #channel = ctx.message.author.voice.voice_channel
        await channel.connect()
        
    @commands.command()
    async def biosacchi(self, ctx):
        await ctx.send("https://www.0x41414141.it/")

    @commands.command()
    async def leave(self, ctx):
        if(ctx.voice_client):
            await ctx.guild.voice_client.disconnect()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        await ctx.send(f"{ctx.author.mention} Impara a scrivere i comandi")
        await ctx.send(str(error))

def setup(client):
    client.add_cog(Commands(client))