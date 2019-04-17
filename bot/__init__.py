from discord.ext import commands
client = commands.Bot(command_prefix='?')


@client.event
async def on_ready():
    print('Ready!')


@client.command()
async def ping(ctx):
    await ctx.send('pong!')
