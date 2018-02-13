import discord
from discord import Embed, Color
import os
import sys

import STATICS, QUERIES, FUNCTIONS

description = 'Spells'

#class Spell:

    #def __init__(self,message, client):
        #self.firstTry = 0

async def ex(message, client):
        #if self.firstTry == 0:
            #self.firstTry = 1
    x = 0
    y = 0
    option1 = -1
    option1Set = [ 1, ]
    schoolOptionSet = [ 1, 2, 3, 4, 5, 6, 7, 8, ]
    spellLevelOptionSet = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]
    schoolOption = 1
    spellOptions = ''
    legalOption = 0
    schools = ['Abjuration','Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation']
    head, sep, msg = message.content.partition(' ')
    spellList = []
    answer = 0

    question1 = 'Select Category you would like to choose from \n 1. Schools'
    question2 = 'Select Category you would like to choose from \n 1. Abjuration\n2. Conjuration\n3. Divination\n4. Enchantment\n5. Evocation\n6. Illusion\n7. Necromancy\n8. Transmutation'
    question3 = 'What level? (0-9)'

    if msg == '':
        
        answer = await FUNCTIONS.handle_menu(message, client, legalOption, option1, option1Set, question1)

        legalOption = 0

        if answer == 1:
            answer = 0

            answer = await FUNCTIONS.handle_menu(message, client, legalOption, option1, schoolOptionSet, question2)
            
            schoolOption = answer - 1
            schoolChoice = schools[schoolOption]

            answer = 0

            answer =  await FUNCTIONS.handle_menu(message, client, legalOption, option1, spellLevelOptionSet, question3)

            spellLevel = answer

            spellList = QUERIES.get_spell_list_by_school_level(schoolChoice, spellLevel)

        #spellList = QUERIES.get_spell_list()

        for spell in spellList:
            spellID = spellList[x][y]
            y = y + 1
            spellName = spellList[x][y]
            y = 0
            x = x + 1
            spellOptions += (str(spellID) + '. ' + str(spellName) + '\n')

        await client.send_message(message.channel, spellOptions)
        msg = await client.wait_for_message(author=message.author)

        spellSelected = msg.content

        spellInfo = QUERIES.get_spell_by_id(spellSelected)

        spellInfoDesc = len(spellInfo[0][7])

        if spellInfo[0][9] == '0':
                pageInfo = ''
        else:
            pageInfo = ' Page ' + spellInfo[0][9]
        
        embed = discord.Embed(title=spellInfo[0][0])
        embed.add_field(name="School", value=spellInfo[0][1])
        embed.add_field(name="Level", value=spellInfo[0][2])
        embed.add_field(name="Casting Time", value=spellInfo[0][3])
        embed.add_field(name="Range", value=spellInfo[0][4])
        embed.add_field(name="Components", value=spellInfo[0][5])
        embed.add_field(name="Duration", value=spellInfo[0][6])

        if spellInfoDesc > 750:
            firstSection = spellInfo[0][7][:749]
            restOfTheSection = spellInfo[0][7][750:]
            embed.add_field(name="Description", value=firstSection)
            await client.send_message(message.channel, embed=embed)

            if len(restOfTheSection) > 1000:
                secondSection = restOfTheSection[:999]
                restOfTheSection = restOfTheSection[1000:]
                embed2 = discord.Embed(title=spellInfo[0][0]+' cont\'d')
                embed2.add_field(name="Description", value=secondSection)
                await client.send_message(message.channel, embed=embed2)

                embed3 = discord.Embed(title=spellInfo[0][0]+' cont\'d')
                embed3.add_field(name="Description", value=restOfTheSection)
                embed3.set_footer(text='Source: ' + spellInfo[0][8] + pageInfo)
                await client.send_message(message.channel, embed=embed3)
            else:
                embed2 = discord.Embed(title=spellInfo[0][0]+' cont\'d')
                embed2.add_field(name="Description", value=restOfTheSection)

                embed2.set_footer(text='Source: ' + spellInfo[0][8] + pageInfo)
                await client.send_message(message.channel, embed2)
        else:
            embed.add_field(name="Description", value=spellInfo[0][7])
            embed.set_footer(text='Source: ' + spellInfo[0][8] + pageInfo)
            await client.send_message(message.channel, embed=embed)
            #else:
                #await client.send_message(message.channel, 'You done messed up, A-aron!')
            

                #embed.add_field(name="Classes", value=spellInfo[0][10])

        