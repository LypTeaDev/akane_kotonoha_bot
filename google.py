from google_images_download import google_images_download
from discord.ext import commands
from discord import File
import discord
import os
from os import path
import random

"""


"""

def get_filenames(dir):
    return os.listdir(dir)

def is_file_empty(dir):
    return not bool(list(os.listdir(dir)))


class Google(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def gsearch(self, ctx, *, args):
        google_search = args
        dir = 'downloads/' + google_search + "/"

        if not path.exists(dir):
            response = google_images_download.googleimagesdownload()
            arguments = {"keywords": google_search, "limit": 20}
            paths = response.download(arguments)

        filenames = get_filenames(dir)

        f = open(dir + random.choice(filenames), 'rb')
        await ctx.send(file=File(f, google_search + '.png'))

    @commands.command()
    async def blue(self, ctx, *, member: discord.Member = None):
        dir = 'downloads/blue things/'

        if (is_file_empty(dir)):
            response = google_images_download.googleimagesdownload()
            arguments = {"keywords": "blue things", "limit": 20}
            paths = response.download(arguments)

        filenames = get_filenames(dir)

        f = open(dir + random.choice(filenames), 'rb')
        await ctx.send(file=File(f, 'blue.png'))

    @commands.command()
    async def red(self, ctx, *, member: discord.Member = None):
        response = google_images_download.googleimagesdownload()
        arguments = {"keywords": "red", "limit": 20}
        paths = response.download(arguments)

        dir = 'downloads/red/'
        filenames = get_filenames(dir)

        f = open('downloads/red/' + random.choice(filenames), 'rb')
        await ctx.send(file=File(f, 'red.png'))

    @commands.command()
    async def gay(self, ctx, *, member: discord.Member = None):
        response = google_images_download.googleimagesdownload()
        arguments = {"keywords": "rainbow", "limit": 20}
        paths = response.download(arguments)

        dir = 'downloads/rainbow/'
        filenames = get_filenames(dir)

        f = open('downloads/rainbow/' + random.choice(filenames), 'rb')
        await ctx.send(file=File(f, 'rainbow.png'))

    @commands.command()
    async def previously_searched(self, ctx):
        filenames = get_filenames('downloads/')
        await ctx.send("Previously searched items: " + filenames)

    @commands.command()
    async def remove_all(self, ctx):
        os.rmdir('downloads/')
        await ctx.send("Deleted all items successfully!")
