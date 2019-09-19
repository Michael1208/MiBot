import discord 
import os
import asyncio
import time
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import has_permissions

bot = commands.Bot(command_prefix='mb-')

@bot.event
async def on_ready():        
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="mb-help"))
    print("MiBot Premium has started!")

@bot.command(pass_context=True)
async def warn(ctx,user:discord.Member,count,*,reason=None):

if reason is None:
    reason = "No reason provided"

try:
      # add warning
   except:
      await ctx.send("Count is Invalid.")
      raise TypeError # crash out of cmd
    # send successful message
     # find server data file
    # if inexistent, then go and create it.
    # log the warn count based on a json obj {userid:warncount}
    
@bot.command()
async def avatar(ctx, member: discord.Member):
	embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
	embed.set_author(name=f"Avatar Of {member}")
	embed.set_image(url=member.avatar_url)
	await ctx.send(embed=embed)	
@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Premium Required Type n!info")
	
@bot.command()
async def ping(ctx):
    start = time.monotonic()
    embed = discord.Embed(title="MiBot Premium's Ping!", color=0x0084FD)
    embed.add_field(name="Ping Latency", value="{} ms".format(int(ctx.bot.latency*1000)))
    await ctx.send(embed=embed)
@ping.error
async def ping_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Premium Required Type n!info")

@bot.command() 
async def serverinfo(ctx):
    guild = ctx.message.guild
    online = len([m.status for m in guild.members if m.status == discord.Status.online or m.status == discord.Status.idle])
    embed = discord.Embed(name="{} Server information".format(guild.name), color=0x6AA84F)
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="Server Name", value=guild.name, inline=True)
    embed.add_field(name="Owner", value=guild.owner.mention)
    embed.add_field(name="Server ID", value=guild.id, inline=True)
    embed.add_field(name="Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="Members", value=len(guild.members), inline=True)
    embed.add_field(name="Online", value=f"**{online}/{len(guild.members)}**")
    embed.add_field(name="Guild Created At", value=guild.created_at.strftime("%d %b %Y %H:%M"))
    embed.add_field(name="Emojis", value=f"{len(guild.emojis)}/100")
    embed.add_field(name="Server Region", value=str(guild.region).title())
    embed.add_field(name="Total Channels", value=len(guild.channels))
    embed.add_field(name="AFK Channel", value=str(guild.afk_channel))
    embed.add_field(name="AFK Timeout", value=guild.afk_timeout)
    embed.add_field(name="Verification Level", value=guild.verification_level)
    await ctx.send(embed=embed)      
@serverinfo.error
async def serverinfo_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Premium Required Type n!info")   
	
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member=None, *, reason=None):
    if member is None:
        await ctx.send("Please mention a user to ban")
    else:
        await member.ban(reason=reason)
	
@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
	await ctx.channel.purge(limit=amount)
	
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member=None, *, reason=None):
    if member is None:
        await ctx.send("Please mention a user to kick")
    else:
        await member.kick(reason=reason)

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")

@bot.command()
@commands.has_permissions(mute_members=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Error Check Permissions / Server Needs Role Name Muted Spelt Excatly Like That ")
 
 
@bot.command()
@commands.has_permissions(mute_members=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Error Check Permissions / Server Needs Role Name Muted Spelt Excatly Like That")

@bot.command(aliases=['whois'])
async def userinfo(ctx, member: discord.Member):       
	
    roles = [role for role in member.roles]
                        
    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)	
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild Username:", value=member.display_name)	
    embed.add_field(name="Account Created At:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p EST"))
    embed.add_field(name="Joined Server At:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p EST"))	
    embed.add_field(name=f"Roles {len(roles)}" , value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top Role:", value=member.top_role.mention)
    embed.add_field(name="Bot?", value=member.bot)		
    await ctx.send(embed=embed)
@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Missing Arguments : Member Missing")
	
@bot.command()
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, member: discord.Member, *, nickname):
    await member.edit(nick=f"{nickname}")
    await ctx.send(f'Nickname Changed For {member.mention} ') 
    await ctx.message.delete()
		    					    
@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
	responses = ['It Is Certain',
	'Without A Doubt',
	'Yes Definitely',
	'You May Rely On It',
	'Most Likely',
	'Ask Again Later',
	'Nope',
	'Cannot Tell Right Now']

	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
	
@bot.command()
async def say(ctx, *, content):
    if content == "@everyone":
        await ctx.send("Please dont try to mention **@**everyone!")
        return
    elif content == "@here":
        await ctx.send("Please dont try to mention **@**here!")
        return
    else:
        await ctx.send(content)
        await ctx.message.delete()
