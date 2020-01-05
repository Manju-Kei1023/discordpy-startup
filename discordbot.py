import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='b!' ,help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    print('bonjin neko bot is start!')
    print('Logind as\n'+str(bot.user.name)+'\n'+str(bot.user.id))
    bot.global_list = []

@bot.listen()
async def on_message(message):
    if message.author.bot:
        return

    if '草' in message.content:
        await message.channel.send('草')
    if message.content.endswith('マ？'):
        await message.channel.send('マ')


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
@bot.command()
async def help(ctx, cmd):
    if cmd == '':
        ctx.send('全ての項目を表示')
@bot.listen()
async def on_message(message):

    if message.author == message.guild.me:
        return

    if message.content == "!global":
        if message.channel not in bot.global_list:
            bot.global_list.append(message.channel)
            await message.channel.send("グローバルチャットのチャンネルに登録しました。")
        else:
            await message.channel.send("既に登録されています。")
        return

    embed = discord.Embed(title=f"サーバー: {message.guild.name}",description=message.clean_content )
    embed.set_author(name=message.author.name,icon_url=message.author.avatar_url)

    for ch in bot.global_list:
        if message.channel != ch: 
            await ch.send(embed=embed)
    
bot.run(token)
