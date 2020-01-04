import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='b!' ,help_command=None ,Activity='凡人ねこBot')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    print('bonjin neko bot is start!')
    print('Logind as\n'+str(bot.user.name)+'\n'+str(bot.user.id))

@bot.listen()
async def on_message(message):
    if message.author.bot:
        return

    if '草' in message.content:
        await message.channel.send('草')



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
