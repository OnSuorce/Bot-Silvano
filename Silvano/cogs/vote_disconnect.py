import discord
from discord.ext import commands

class Vote_disconnect(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.polls = []
    
    @commands.command()
    async def votedisconnect(self, ctx, member: discord.Member):
        if(ctx.message.author.voice is None):
            await ctx.send("You are not in a voice channel")
            return
        

        author_channel = ctx.message.author.voice.channel
        
        guild = member.guild
        if(member.voice is None):
            await ctx.send("He is not in a voice channel")
            return
        member_channel = member.voice.channel   
        if(author_channel != member_channel):
            await ctx.send("You are not in the same voice channel")
            return

        else:
            embed = discord.Embed(title = "Vote disconnect",colour=discord.Colour(5).random())
            embed.add_field(name="Members who can vote:", value="-------",inline=False)
            
            ind = guild.voice_channels.index(author_channel)
            members = guild.voice_channels[ind].members
            members.remove(member)
            if(len(members)<2):
                await ctx.send("You must be in more than 2 members connected")
                return
            for i in members:
                if i.bot:
                    members.remove(i)
            
            for mem in members:
                embed.add_field(name=mem.name, value="-")
            
            votes_required = int((len(members)/2)+1)
            embed.add_field(name="Votes required: ", value=votes_required, inline=False)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction("✅")
            await msg.add_reaction("❌")
            self.polls.append(Poll(msg,members,embed,votes_required,member))


    @commands.Cog.listener()
    async def on_reaction_add(self,reaction, user):
        for poll in self.polls:
            if user in poll.members and reaction.message == poll.msg:
                poll.members.remove(user)
                print(user.name)
                print(poll.votes_required)
                if(reaction.emoji == "✅"):

                    if(poll.votes_required-1>0):
                        print(poll.votes_required)
                    #poll.embed.set_field_at(0, name="ss", value="aa")
                    #await poll.msg.edit(embed=poll.embed)
                        poll.votes_required = poll.votes_required-1
                    else:
                        await poll.voted.move_to(None)
                        self.polls.remove(poll)
                    

        return

class Poll():
    def __init__(self,msg,members,embed, votes_required, voted):
        self.msg = msg
        self.members = members
        self.embed = embed
        self.votes_required = votes_required
        self.voted = voted

def setup(client):
    client.add_cog(Vote_disconnect(client))
