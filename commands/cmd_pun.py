import discord
from discord import Embed, Color
import os
import sys

import STATICS
import QUERIES

description = 'Puns'

async def ex(message, client):
    msg, isImg = QUERIES.get_pun()

    if isImg == 0: 
        embed = discord.Embed(title="The Mediocre Bot walks to the stage as the loveable Pun Bot 3000 and steps to the mic...", description=msg)
        embed.set_footer(text='Thank you! I\'ll be here all night! Or at least until I get shut off! Be sure to tip your waitress!')
        await client.send_message(message.channel, embed=embed)
    else:
        imgLoc = 'http://www.webdocdesigns.com/puns/' + msg
        embed = discord.Embed(title='The Mediocre Bot searches the archives for a great pun...')
        embed.set_image(url=imgLoc)
        embed.set_footer(text='You are welcome.')
        await client.send_message(message.channel, embed=embed)