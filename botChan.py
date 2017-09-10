import discord
from discord.ext import commands
import random
import asyncio
import  json
import os

client = discord.Client()
description = '''These be my Commands'''
prefix = '?'
bot = commands.Bot(command_prefix=prefix, description=description)

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Games with my Heart'))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command
async def killSwitch():
    await bot.say('Understood')

    
@bot.command(pass_context=True)
async def test(ctx):
    """Under construction teehee"""
    rolez = ctx.message.author.roles
    role = ""
    await bot.say("Here are your roles!")
    for x in rolez:
        role += (str)x
    await bot.say(role)
    await bot.say("Your top roles is")
    await bot.say(ctx.message.author.top_role)
    
@bot.command()
async def add(left : float, right : float):
    """Adds two numbers together."""
    temp = await bot.say(str(left) + ' ' + str(right))
    await asyncio.sleep(2)
    await bot.edit_message(temp, 'Oh.. wait..')
    await asyncio.sleep(1)
    await bot.edit_message(temp, 'Fixing...')
    await asyncio.sleep(1)
    await bot.edit_message(temp, left + right)
    await asyncio.sleep(1)
    await bot.say('I AM A SMART BOY')
    print('Completed Addition')


@bot.command()
async def sub(left : float, right: float):
    """Subtracts two numbers."""
    temp = await bot.say(str(left) + ' ' + str(right))
    await asyncio.sleep(2)
    await bot.edit_message(temp, 'Oh.. wait..')
    await asyncio.sleep(1)
    await bot.edit_message(temp, 'Fixing...')
    await asyncio.sleep(1)
    await bot.say(temp, left - right)
    await bot.say('I AM A SMART BOY')
    print('Completed Subtraction')

@bot.command()
async def choose(*choices : str):
    """Chooses between multiple choices. """
    choices = str(choices).lower()
    print(choices)
    result = ''
    
    if('jabby' in choices):
       result = ('jabby')
    elif('jabari'.upper().lower() in choices):
       result = ('jabari ')
    else:
        result = str(random.choice(choices))

    await bot.say(result)
    print(result)

@bot.command()
async def flip():
    ''' Flips a coin '''
    coin = ['Heads','Tails']
    result = (random.choice(coin))
    await bot.say(result)
    print(result)

@bot.command()
async def feh(message):
    ''' Gives you the page for a FEH Hero '''
    await bot.say('https://fireemblem.gamepress.gg/hero/' + message)

@bot.command()
async def addQuote(msg : str): ##Things to implement next
    '''Add a Quote to be spat out later'''
    fo = open("Quotes.txt", "w")
    fo.write(msg)
    fo.close()

@bot.command()
async def callQuote(): ##Things to implement next
    '''Returns a random quote '''
    fo = open("Quotes.txt", "r")
    await bot.say(fo.read())
    print(fo.read())
    fo.close()

@bot.command()
async def allQuote(): #Things to implement next
    '''Returns all Quotes in file '''
    
@bot.event
async def on_message(message):
    msgContent = message.content.lower()
    if message.author == bot.user:
        return
    
    elif message.content.startswith('WHATS GOOOD '):
        await asyncio.sleep(2)
        await bot.send_message(message.channel, 'NO CLOUDIEBOT-CHAN! BAKA COW!')
        print('CloudieBot said something')
        
    elif 'nani' in msgContent:
        reaction = open('NANI.jpg', 'rb')
        await bot.send_file(message.channel, reaction)
        await bot.send_message(message.channel, 'NANI!?!?!')   
        reaction.close()
        print('Someone made a Nani meme')
    
    elif message.content.startswith('Hi'):
        gResponses = open("GreetingResponse.txt", "r")
        if(message.author.name == 'Jabby Sparks'):
            await bot.send_typing(message.channel)
            await asyncio.sleep(3)
            cMsg = gResponses.readline()
            await bot.send_message(message.channel, cMsg)
        else:
            rNumber = random.randint(1,2)
            print(rNumber)
            rResponse = gResponses.read().split('\n')
            await bot.send_typing(message.channel)
            await asyncio.sleep(3)
            await bot.send_message(message.channel, rResponse[rNumber] + ' {0.author.mention}'.format(message))

    elif message.content.startswith("I'm"):
        msg = message.content
        await bot.send_message(message.channel, "Hello" + msg[3:] + ", I'M DAD!")

    elif 'kevin' in msgContent:
        await bot.send_message(message.channel, ':O KEVIN-CHAN')
        await asyncio.sleep(2)
        await bot.send_message(message.channel, 'Where?!?!')
    await bot.process_commands(message)


bot.run('PRIVATE TOKEN')
