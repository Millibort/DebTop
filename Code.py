import os
import discord
import datetime
import time

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

    presentDate = datetime.datetime.now()
    unix_timestamp = datetime.datetime.timestamp(presentDate)*1000

    try:
        with open('Messages/' + str(message.author.id) + '.txt', 'x') as f:
            f.write(str(message.guild.id))
            f.write("`")
            f.write(str(message.channel.id))
            f.write("`")
            f.write(str(unix_timestamp))
            f.write("`")
            f.write(str(message.content))
            f.write("|")
    except FileExistsError:
        with open('Messages/' + str(message.author.id) + '.txt', 'r') as f:
            old = f.read()
        with open('Messages/' + str(message.author.id) + '.txt', 'w') as f:
            f.write(old)
            f.write(str(message.guild.id))
            f.write("`")
            f.write(str(message.channel.id))
            f.write("`")
            f.write(str(unix_timestamp))
            f.write("`")
            f.write(str(message.content))
            f.write("|")

    if "<stat>" in message.content.lower():
        people = os.listdir("Messages")
        x = 0
        for i in range(len(people) - 1):
            with open('Messages/' + people[i] + '.txt', 'r') as f:
                text = f.read()
            text = text.split("|")
            x = x + len(text)
        await message.channel.send(str(x))

client.run(TOKEN)