import discord
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']



client.run(token)
