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
#    client.global_list = []

"""
@client.event
async def on_message(message):

    if message.author == message.guild.me:
        return

    if message.webhook_id:
        return

    global_tmp = [w for w in await message.channel.webhooks() if w in client.global_list]

    if message.content == "!global":
        if global_tmp:
            await message.channel.send("既に登録されています。")
            return

        new_w = await message.channel.create_webhook(name="global")
        client.global_list.append(new_w)
        await message.channel.send("グローバルチャットのチャンネルに登録しました。")
        return

    for webhook in client.global_list:
        if message.channel != webhook.channel:
            await webhook.send(content=message.content,username=message.author.name,avatar_url=message.author.avatar_url)
"""

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '草' in message.content:
        await message.channel.send('草')

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
