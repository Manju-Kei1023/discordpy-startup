import discord
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print('bonjin neko bot is starting')
    print('Logging as Name:'+str(client.user.name)+'\nID:'+str(client.user.id))
    prefix = 'b!'
    args = []

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '草' in message.content:
        await message.channel.send('草')
        
        

client.run(token)
