import discord
from discord import Embed, Color
import random

import STATICS

description = 'Roll'

CMDMAP = None

async def ex(message, client):

    head, sep, msg = message.content.partition(' ')

    diceSides = -1
    diceNumber = -1
    diceModifier = -1
    numOfDice = -1

    diceVal = 0

    results = ''

    acceptibleSides = ['2', '3', '4', '6', '8', '10', '12', '20', '100']

    if msg == '':
        await client.send_message(message.channel, 'You chose to roll a 1d20 with no modifiers.')
        msg = '1d20(0)'


    dLoc = msg.rfind('d')
    opLoc = msg.rfind('(')
    cpLoc = msg.rfind(')')

    if opLoc != -1 and cpLoc < 0:
        cpLoc = len(msg) + 1

    if dLoc == 0:
        numOfDice = 1

    if opLoc < 0 and cpLoc < 0:
        diceModifier = 0
    
    if numOfDice < 0: 
        numOfDice = msg[0:dLoc]
    
    if int(numOfDice) > 10:
        await client.send_message(message.channel, 'I\'m sorry, you are only allowed to roll up to 10 dice of 1 type')
        return                                                           
    
    if diceSides < 0 and opLoc < 0:
        diceSides = msg[dLoc+1:]
    else:
        diceSides = msg[dLoc+1:opLoc]
    
    if diceSides not in acceptibleSides:
        await client.send_message(message.channel, 'The number of sides is not acceptable. The number of sides available are: 2, 3, 4, 6, 8, 10, 12, 20, 100.')
        return

    if diceModifier < 0:
            diceModifier = msg[opLoc+1:cpLoc]

    for i in range(0, int(numOfDice)):
        diceSides1 = int(diceSides)
        diceVal = (random.randint(1,int(diceSides1)))
        finalVal = int(diceVal) + int(diceModifier)
        results += ('You rolled a {0} sided dice and got {1}. With a modifier of {2}, you got a {3}.\n'.format(diceSides, diceVal, diceModifier, finalVal))
        
    await client.send_message(message.channel, embed=discord.Embed(
                                                                        color=discord.Color.orange(),
                                                                        description=(results),
                                                                    )
        )
