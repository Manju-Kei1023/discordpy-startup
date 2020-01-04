import discord
from discord.ext import commands
import os
import traceback

client = discord.Client()

bot = commands.Bot(command_prefix='b!')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)



@bot.command()
async def say(ctx, *args):
    await ctx.send('{}'.format(join(args)))

@client.event
async def on_message(message):

    if message.content.startsWith == '$hello':
        await message.channel.send('Hello!')


bot.run(token)
