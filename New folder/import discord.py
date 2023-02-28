import discord
import random

with open('TOKEN.txt', 'r') as f:
    TOKEN = f.read()

things = [
        'OH YEA!!',
        'absolutely!',
        'Yes!',
        'Wow!',
        "You're so smart!"
    ]

client = discord.Client()

client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = '<Help>'))
    print(f'{client.user.name} is ready')

@client.event
async def on_message(message):
    if message.author.id == 558081044872429569:
        await message.channel.send(random.choice(things))

client.run(TOKEN)