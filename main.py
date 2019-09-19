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
    embed = discord.Embed(title="Neon Premium's Ping!", color=0x0084FD)
    embed.add_field(name="Ping Latency", value="{} ms".format(int(ctx.bot.latency*1000)))
    await ctx.send(embed=embed)
@ping.error
async def ping_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Premium Required Type n!info")
