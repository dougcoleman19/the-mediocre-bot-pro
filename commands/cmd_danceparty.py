import discord
from discord import Embed, Color
import os
import sys

description = 'DanceParty'

async def ex(message, client):

    embed=discord.Embed(title='PARTY TIME!')
    embed.set_image(url='http://www.webdocdesigns.com/funstuff/partyporg.gif')

    await client.send_message(message.channel,embed=embed)