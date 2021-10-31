import discord
from discord.ext import commands
from funcs import *


client = commands.Bot(command_prefix="a!")

@client.command()
async def info(ctx, name):
  await ctx.send(player_info(name))

@client.command()
async def br(ctx):
  await ctx.send(br_rotation())

@client.command()
async def arena(ctx):
  await ctx.send(arena_rotation())

@client.command()
async def server(ctx):
  await ctx.send(server_status())



@client.event 
async def on_ready():
  print("We have logged in as {0.user}".format(client))

client.run(my_secret)