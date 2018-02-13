# The Medicore Bot by RobustOne

import discord
from discord import Embed, Color
from discord.ext import commands
from discord.ext.commands import Bot
import subprocess
import asyncio
import os
import sys

from time import gmtime, strftime
import sys

import STATICS
from commands import cmd_roll, cmd_help, cmd_pun, cmd_npcspeak, cmd_spell, cmd_danceparty, cmd_addquote, cmd_quote, cmd_feats

#from commands.cmd_spell import Spell 

# Create Discord Client
client = discord.Client()

cmdmap = {
            "help": cmd_help,
            "roll": cmd_roll,
            "pun": cmd_pun,
            "npcspeak": cmd_npcspeak,
            "spell": cmd_spell,
            "party": cmd_danceparty,
            "addquote": cmd_addquote,
            "quote": cmd_quote,
            "feats": cmd_feats,
}

# When the bot is started
@client.event
async def on_ready():
    print("\n-----------------------------\n"
            "The Mediocre Bot v.{}\n"
            "Ready to go\n"
    "-----------------------------".format(STATICS.VERSION))


@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

    
@client.event
async def on_message(message):
    if message.content.startswith('!cmd'):
        await client.send_message(message.channel, 'Enter command')
        msg = await client.wait_for_message(author=message.author)
        proc = msg.content
        auth = msg.author

        cmd = cmdmap[proc]

        try:
            await cmd.ex(msg, client)
        except:
            await cmd.ex(msg, client)
            pass
        
        print(strftime("[%Y.%d.%m %H:%M:%S]", gmtime()) + ' [COMMAND] \"' + message.content + ' => '+ msg.content + "\" by " + message.author.name)

    elif message.content.startswith(STATICS.PREFIX) and not message.author == client.user:
        print(strftime("[%Y.%d.%m %H:%M:%S]", gmtime()) + ' [COMMAND] \"' + message.content + "\" by " + message.author.name)
        invoke = message.content.split(" ")[0].replace(STATICS.PREFIX, "",1)
        command_string = ""

        cmd = cmdmap[invoke]
      
        try:
            await cmd.ex(message, client)
        except:
            #await cmd.ex(message, client)
            pass
    
        

client.run(STATICS.TOKEN)