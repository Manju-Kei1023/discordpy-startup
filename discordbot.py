import discord
from discord.ext import commands
import os
import traceback

client = discord.Client()

bot = commands.Bot(command_prefix='b!')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print('bonjin neko bot is start!')
    print('Logind as\n'+str(bot.user.name)+'\n'+str(bot.user.id))

@client.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    if '草' in message.content:
        message.send('草')

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "問題が発生しました", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    print(error_msg)



@bot.command()
async def say(ctx, *args):
    await ctx.send('{}'.format(' '.join(args)))

@bot.command()
async def cat(ctx):
    await ctx.send('にゃーん')
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def mydata(ctx):
    await ctx.send('Your ID Here:'+str(ctx.author.id))

bot.run(token)
