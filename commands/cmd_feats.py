import discord
from discord import Embed, Color
import os
import sys

import STATICS
import QUERIES

description = 'Feats'

async def ex(message, client):
    feat, skill, level, description, source = QUERIES.get_feats()

    embed = discord.Embed(title=feat)
    embed.add_field(name="Prerequisite", value=skill)
    embed.add_field(name="Level", value=level)
    embed.add_field(name="Description", value=description)
    embed.set_footer(text="Source: " + source)

    await client.send_message(message.channel, embed=embed)
