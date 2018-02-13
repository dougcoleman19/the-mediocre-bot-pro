import os
from os import path
from discord import Embed, Color

import text_files

description = 'Help'

CMDMAP = None
FORMAT_CODE = '```'
FORMAT_BOLD = '**'

async def ex(message, client):
    author = str(message.author)
    head, sep, msg = message.content.partition(' ')

    if msg == '':
        greeting = ('Greetings' + author + '!')
        helpDescription = ('\n\nHere is the list of helpful **commands** The Mediocre Bot can provide information on. Type !help <command> for more information.'
                        + '\n\n **roll** '
                        + '\n **pun** '
                        + '\n **quote** '
                        + '\n **addquote** '
                        + '\n\n For more information about a particular command, type !help <command>.')
        section_title = 'The Mediocre Bot - Help'
        fullMessage = greeting + helpDescription
    
    if msg == 'roll':
        with open("text_files/help_roll.txt") as f:
            description = f.read()
        f.closed
        section_title = 'roll'
    elif msg == 'pun':
        with open("text_files/help_pun.txt") as f:
            description = f.read()
        f.closed
        section_title = 'pun'
    elif msg == 'addquote':
        with open("text_files/help_addquote.txt") as f:
            description = f.read()
        f.closed
        section_title = 'addquote'
    elif msg == 'quote':
        with open("text_files/help_quote.txt") as f:
            description = f.read()
        f.closed
        section_title = 'quote'
    else:
        section_title = 'Oops!'
        description = 'I am sorry -- I do not recognize that command.'
    
    fullMessage = FORMAT_CODE + description + FORMAT_CODE

    await client.send_message(message.author, embed=Embed(
            color=Color.green(),
            title=section_title,
            description=fullMessage,
        ))

