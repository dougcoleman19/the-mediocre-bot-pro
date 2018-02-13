import discord
from discord import Embed, Color
import os
import sys

import STATICS
import QUERIES

async def ex(message, client):
    quote, submitted_by, date = QUERIES.get_quote()

    footer_text = 'This quote was submitted by {0} on {1}. Thanks, Obama!'.format(submitted_by, date)

    embed = discord.Embed(title='The Mediocre Bot opens up the tomb of Mediocre Quotes to a random page and begins to read...', description=quote)
    embed.set_footer(text=footer_text)

    await client.send_message(message.channel, embed=embed)
