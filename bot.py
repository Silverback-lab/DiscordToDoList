# bot.py
import os
import random
from email import message

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
todolist = list()

@bot.command(name='del')
async def del_todo(ctx): 
    msg:str = ctx.message.clean_content 
    msg = msg.replace("!del ", '')
    num:int = int(msg)
    del todolist[num]


@bot.command(name='add')
async def add_todo(ctx):
    msg:str = ctx.message.clean_content    
    msg = msg.replace("!add ", '')
    todolist.append(msg)     
    response:str = f"Your Item is added: "+ msg  
    await ctx.send(response)


@bot.command(name='list')
async def list_todo(ctx):
    response:str = ''
    c:int = 0
    for i in todolist:
        response = response + f"{c}: {i}\n"
        c = c + 1
    await ctx.send(response)


bot.run(TOKEN)