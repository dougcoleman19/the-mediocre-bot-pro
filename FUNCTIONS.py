import discord
from discord import Embed, Color
import os
from os import path
import random

import text_files

async def check_channel(message,client):
    arena_channel = '405096848269770762'
    message_channel = str(message.channel.id)
    

    if message_channel == arena_channel:
        await client.send_message(message.channel, 'You are ready to play.')
    else:
       await client.send_message(message.channel, 'You cannot play the Arena here. Please go into the #arena channel.')
    
    return None

def english_to_elvish(wordCount):
    x = 0
    string = ''

    with open("text_files/text_elvish.txt", encoding="utf8") as f:
            description = f.read()

    # The text file has 480 words.

    words = description.split(' ')

    start = (random.randint(0,479-(int(wordCount))))

    while x <= int(wordCount):
        try:
            #test = words[start]
            if x == int(wordCount):
                string += words[start] + "."
            else:
                string += words[start] + " "
            start += 1
            x +=1
        except IndexError: 
            start = 0
        
    string = string.capitalize()

    return string

async def handle_menu(message, client, legalOption, option, optionSet, question):

    while legalOption == 0:
        await client.send_message(message.channel, question)
        msg = await client.wait_for_message(author=message.author)
        option = msg.content

        if option == '!spell':
            await client.send_message(message.channel, 'You started a second session. Ending previous session.')
            break

        try:
            option = (int(option))

            if option < 0:
                await client.send_message(message.channel, 'I do not recognize your selection.')
            else:
                legalOption = await is_option_legal(option, optionSet, message, client)
        except:
            await client.send_message(message.channel, 'Please enter a number.')
    
    return option


async def is_option_legal(option, optionSet, message, client):
    isOptionLegal = 0

    if option not in optionSet:
        await client.send_message(message.channel, 'I am sorry, I do not recognize your selection.')
    else:
        isOptionLegal = 1
    
    return isOptionLegal
