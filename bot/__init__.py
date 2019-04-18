from discord.ext import commands
client = commands.Bot(command_prefix='?')
from database.models import CommandsModel


@client.event
async def on_ready():
    print('Ready!')

@client.command()
async def ping(ctx):
    await ctx.send('pong!')
