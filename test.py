from urllib.request import Request
import urllib.request


url = 'https://cdn.discordapp.com/attachments/600867936621690898/733119594306469918/profilepic.png'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

imagefile = open('test.jpg','wb')
imagefile.write(urllib.request.urlopen(req).read())
imagefile.close()


import discord
import logging
import urllib.request
import Beau


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content.startswith('!rawr'):
            channel = message.channel
            await channel.send('x3 nuzzles pounces on you uwu u so warm :3')

        if message.content.startswith('!imagetest'):
            image = 'https://media.discordapp.net/attachments/600867936621690898/733117004508299304/profilepic.png'
            urllib.request.urlretrieve(image, "test.jpg")

            channel = message.channel
            await channel.send(message.attachments[0].url)


if __name__ == '__main__':
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    client = MyClient()
    client.run('NDk5Nzg2NzUzNjY2OTczNjk2.Xw-XjQ.tgOog_kXVTWMPVs6OVOUuKoOxu0')
