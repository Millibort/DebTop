import os
import datetime
import random
import discord
import json
import requests
Run = True


with open('TOKEN.txt', 'r') as f:
    TOKEN = f.read()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents = intents)

def oneof(singlething, bunchofthings):
    num = 0
    while num < len(bunchofthings):
        if bunchofthings[num] == singlething:
            return(True)
        num = num + 1
    return(False)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = '<Help>'))
    print(f'{client.user.name} is ready')

#@client.event
#async def on_message_delete(message):
#    await message.channel.send(message.content)

@client.event
async def on_message(message):
    global Run

    print(message.content)

    if message.content.lower() == "<stop>":
        Run = False
    
    if message.author.id == 558081044872429569:
        if message.content == "KiLl":
            os.system("sudo shutdown -n now")
        if message.content.lower() == "<run>":
            Run = True

    if Run == True:
        if message.content.lower() == "<help>":
            embed=discord.Embed(title="Commands:", color=0xFF5733)
            embed.add_field(name="General:", value="<Help>: Tells you what different commands do! \n<AddS>: Lets people use SFW commands in this channel!", inline=False)
            embed.add_field(name="SFW:", value="<Link>: Sends a link to invite the bot to another server \n<AddNs>: Lets people use NSFW commands in this channel!", inline=False)
            embed.add_field(name="NSFW:", value="<?> : searches r34 for a pic based off of whatever tags you put in, used as \n '<?> tag1 tag2 tag3...etc'.\n<!> : add to your blacklist auto added to all <?> searches, used as \n '<!> tag1 tag2 tag3...etc'.", inline=False)
            embed.set_footer(text="This bot is still a work in progress!")
            await message.channel.send(embed=embed)

        elif message.content == '<AddS>':
                try:
                    with open('./SChannels/' + str(message.channel.id) + '.txt', 'x') as f:
                        print('adding S channel')
                        f.write('made at ')
                        f.write(str(datetime.datetime.now()))
                        f.write(' by ')
                        f.write(str(message.author))
                    await message.channel.send("Channel is now S!")
                except FileExistsError:
                    print('Channel already is S!')
                    await message.channel.send('Error: channel already is S!')
                    return

        elif message.author == client.user:
            return

        NchannelsDir = os.listdir('NsChannels')
        SchannelsDir = os.listdir('SChannels')
        mesChannel = str(message.channel.id) + '.txt'

        if oneof(mesChannel,NchannelsDir) == True:

            if "<!> " in message.content:
                tags = message.content.lower().split(" ")
                tag = ''
                i = 1
                while ( i < len(tags)):
                    tag = tag + " -" + tags[i]
                    i = i + 1
                try:
                    with open("./" + str(message.author.id), "r") as f:
                        pre = f.read()
                except FileNotFoundError:
                    pre = ''
                print(pre)
                print(tag)
                with open("./" + str(message.author.id), "w") as f:
                        f.write(pre + tag)

            elif "<?> " in message.content:
                tags = message.content.lower().split(" ")
                try:
                    with open("./" + str(message.author.id), "r") as f:
                        tags = tags + f.read().split(" ")
                except FileNotFoundError:
                    pass
                tag = ''
                tag = tag + tags[1]
                i = 2
                while ( i < len(tags)):
                    tag = tag + " "
                    tag = tag + tags[i]
                    i = i + 1
                print(tag)
                r = requests.get('https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100&json=1&tags=' + tag)
                data = json.loads(r.text)
                data = data[random.randint(0, len(data) - 1)]
                await message.channel.send(data['file_url'])
                await message.channel.send(data['tags'])
                #await message.channel.send(data)

            elif message.content.lower() == "<femboy>":
                with open('imagelist.txt', 'r') as f:
                    images = f.read()
                images = images.split(" ")
                image = images[random.randint(0,len(images)-1)]
                await message.channel.send("https://millibort2.github.io/images/" + image)

            elif message.author.id == 558081044872429569 or message.author.id == 492823631504736266:
                if message.content == "<spam>":
                    print("L+bozo")
                    with open('imagelist.txt', 'r') as f:
                        images = f.read()
                    images = images.split(" ")
                    for i in range(len(images)):
                        await message.channel.send("https://millibort2.github.io/images/" + images[i])
        
        if oneof(mesChannel,SchannelsDir) == True:
            if message.content.lower() == '<cat>':
                files = os.listdir('C:/Users/elias/OneDrive/Desktop/code/Wow Bot/cats/')
                img = random.randint(0,len(files)-1)
                img = files[img]
                pre = 'C:/Users/elias/OneDrive/Desktop/code/Wow Bot/cats/'
                await message.channel.send(file=discord.File(pre + img))

            if message.content == '<Femboy>':
                await message.channel.send("This channel isn't NS!")
            

            elif message.content == "<Link>":
                await message.channel.send("https://discord.com/api/oauth2/authorize?client_id=946292520449622076&permissions=8&scope=bot")

            elif message.author.id == 558081044872429569:
                if '<AddNs>' in message.content:
                    try:
                        with open('./NsChannels/' + str(message.channel.id) + '.txt', 'x') as f:
                            print('adding Ns channel')
                            f.write('made at ')
                            f.write(str(datetime.datetime.now()))
                            f.write(' by ')
                            f.write(str(message.author))
                        await message.channel.send("Channel is now NS! Naughty ;)")
                    except FileExistsError:
                        print('Channel already is Ns!')
                        await message.channel.send('Error: channel already is Ns!')
                        return

client.run(TOKEN)


""" if message.content == '<Femboy>':
        files = os.listdir('./Images/')
        img = random.randint(0,len(files)-1)
        img = files[img]
        pre = './Images/'
        if '.' not in img:
            pre = pre + img + '/'
            files = os.listdir('./Images/' + img)
            img = random.randint(0,len(files)-1)
            img = files[img]
            num = 0
            while num < len(files):
                await message.channel.send(file=discord.File(pre + files[num]))
                await message.author.send(file=discord.File(pre + files[num]))
                num = num + 1
            return
        await message.channel.send(file=discord.File(pre + img)) """