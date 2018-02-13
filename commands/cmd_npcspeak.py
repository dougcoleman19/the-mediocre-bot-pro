import discord
from discord import Embed, Color
import math


import QUERIES
import FUNCTIONS

import text_files

description = 'New'

async def ex(message, client):
    translatedPhrase = 'This is blank'

    # Name of the NPC
    await client.send_message(message.channel,'What is the name of the NPC you want to speak?')
    msg = await client.wait_for_message(author=message.author)
    npcName = msg.content

    # What the NPC Says
    question2 = 'What do you want {0} to say?'.format(npcName)
    await client.send_message(message.channel, question2)
    msg1 = await client.wait_for_message(author=message.author)
    npcSays = msg1.content
    wordCount = len(npcSays.split())
    wordCount = wordCount + 1

    # The language of the NPC
    question3 = "Finally, please select language {0} speaks: \n [1.] Elvish".format(npcName)
    await client.send_message(message.channel, question3)
    msg2 = await client.wait_for_message(author=message.author)
    languageChoice = msg2.content

    # Translate to language of the NPC
    if languageChoice == '1':
        translatedPhrase = FUNCTIONS.english_to_elvish(wordCount)

    title = 'The figure in front of you begins to speak.'

    embed = discord.Embed(title=title, description=translatedPhrase)

    await client.send_message(message.channel, embed=embed)
    

