import discord
import asyncio
import os

from discord.ext import tasks, commands 


client = commands.Bot(command_prefix = '!')

#List that holds every task
list = []

#
#
# Tells me that the Bot is working and on
#
#

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="!command"))
    print('Bot Started!')

#
#
# This command prints out the list of commands to run the bot.
#
#

@client.command()
async def command(ctx):
    embed = discord.Embed(title="ToDo List Commands", color=0x6441a4)
    embed.add_field(name="!add (task)  EX: !t add cs project", value="Adds a task to the list", inline=False)
    embed.add_field(name="!remove (number)  EX: !t remove 1", value="Removes a task from the list", inline=False)
    embed.add_field(name="!complete (number )  EX: !t complete 1", value="Says that you completed this task in the list",inline=False)
    embed.add_field(name="!todo (task)  EX: !t print", value="Prints the ToDo List", inline=False)
    embed.set_footer(text= "Made by: @RabbiT")
    await ctx.channel.send(embed=embed)
    return

#
#
# This add command adds the task list variable as a tuple (task, completed or not)
#
#

@client.command()
async def add(ctx, *args):
    try:
        msg = ""
        for s in args:
            msg += s + " "
            
        task = (msg, False)
        list.append(task)
        await ctx.channel.send("Added Task")
    except:
        await ctx.channel.send("Not Able to Add")
    return
    
#
#
# This remove command removes the task list variable
#
#

@client.command()
async def remove(ctx, arg):
    try:
        num = int(arg) - 1
        list.pop(num)
        await ctx.channel.send("Removed :(")
    except: 
        await ctx.channel.send("Not Able to Remove")
    return

#
#
# This complete command completes the task list variable by updating the tuple
#
#

@client.command()
async def complete(ctx, arg):
    try:
        num = int(arg) - 1
        (task, complete)= list[num]
        list[num] = (task, True)
        await ctx.channel.send("Completed :). You're doing great!")
    except:
        await ctx.channel.send("Not Able to Completed")
    
    return

#
#
# This todo command prints out the list variable
#
#

@client.command()
async def todo (ctx):
    embed = discord.Embed(title="ToDo List Commands", color=0x6441a4)
    for x in list:
        (task, completed) = x 
        if completed == True:
            embed.add_field(name=":ballot_box_with_check: ~~"+task+"~~", value="_", inline=False)
        else:
            embed.add_field(name=":x: " + task, value="_", inline=False)
    
    embed.set_footer(text= "Made by: @RabbiT")
    await ctx.channel.send(embed=embed)
    return

client.run()