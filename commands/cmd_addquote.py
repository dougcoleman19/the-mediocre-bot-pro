import discord
from discord import Embed, Color
import os
import sys
import datetime

import STATICS
import QUERIES

async def ex(message, client):
    author = str(message.author)
    quote = message.content[10:]

    date = datetime.datetime.now().strftime("%d-%m-%Y")

    QUERIES.add_quote(quote, author, date)

    await client.send_message(message.channel, "Thank you for your submission!")
