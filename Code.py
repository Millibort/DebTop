import os
import discord

with open('TOKEN.txt', 'r') as f:
    TOKEN = f.read()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = 'Linux!'))
    print(f'{client.user.name} is ready')

@client.event
async def on_message(message):
    print(message.author.name + ' said: ' + message.content)
client.run(TOKEN)