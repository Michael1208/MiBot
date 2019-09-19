import discord 
import os
import asyncio
import time
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix='mb-')

@bot.event
async def on_ready():        
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="mb-help"))
    print("MiBot Premium has started!")

@bot.command(pass_context=True)
@commands.has_permissions(manage_guild=True)
async def warn(ctx,user:discord.Member,count,*,reason="No Reason Provided"):
    # get user current warnings
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
@commands.check(boost)  
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
