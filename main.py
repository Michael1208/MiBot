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
