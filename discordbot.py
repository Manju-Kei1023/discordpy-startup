import discord
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print('bonjin neko bot is starting')
    print('Logging as Name:'+client.user.name+'\nID:'+client.user.id)
    prefix = 'b!'

@client.event
async def on_message(message):
    if message.author == client.user:
        return

client.run(token)
