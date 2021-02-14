import discord
from discord import client
from discord.ext import commands
import sys
import os
pth = os.path.abspath(os.getcwd())
sys.path.append(pth + r"\\abuse_dir")
sys.path.append(pth + r"\\wordgames")
import nltkbasedabusetofunny as abf
import jumbledwords as jw
import hangman as hm

token = '<token>'

bot = commands.Bot(command_prefix="$", case_insensitive = True)
bot.remove_command("help")


@bot.event
async def on_guild_join(guild):
    p1 = discord.Embed(title = "Help Section", color = 0x6c0101)
    msg1 = "Hey! I am onlyFANS.py"
    p1.add_field(name="Introduction", value=msg1, inline=False)
    general = (lambda x: x.name == "general", guild.text_channels).find()
    if general and general.permissions_for(guild.me).send_messages:
        await general.send(embed = p1)


@bot.event
async def on_message(message):
    try:
        flag, processed_msg = abf.abusetofunny(message.content)
        if flag and message.author.id != bot.user.id:
            await message.delete()
            await message.channel.send(f"{message.author.mention}: {processed_msg}")
        print(message.content, " -> ", processed_msg, ": ", flag)
    except Exception as e:
        print(f"Exception {e} was raised")
    await bot.process_commands(message)


@bot.command()
async def help(ctx):
    p1 = discord.Embed(title = "Help Section", color = 0x6c0101)
    msg1 = "Hello! You can use the following commands to play various word games:/n 1)`$jumble` to play Jumbled Words, where you'll be given one try to guess what the correct word is."
    p1.add_field(name="Help", value=msg1, inline=False)
    await ctx.channel.send(embed = p1)


@bot.command()
async def jumble(ctx):
    p = discord.Embed(title = "Game: Jumbled Words", color = 0x6c0101)
    question, answer = jw.jumbledwords()
    msg = f"Hey {ctx.message.author.mention}!\nThe string given below is your question.\nYour task, is to unjumble the given string and send the correct answer in this chatbox."
    qn = f"`{question}`"
    p.add_field(name = "Task Details", value = msg, inline = False)
    p.add_field(name = "Question", value = qn, inline = False)
    await ctx.channel.send(embed = p)
    uresp = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    arg = uresp.content
    p1 = discord.Embed(title = "Result")
    if arg.lower()==answer.lower():
        p1.color = 0xdaa520
        msg = f"Congratulations {ctx.message.author.mention}! You got the correct answer!"
        p1.add_field(name = "Won", value = msg, inline = False)
    else:
        p1.color = 0xffffff
        msg = f"Sorry {ctx.message.author.mention}, you didn't win. Your guess was not correct. The correct answer was {answer}."
        p1.add_field(name = "Lost", value = msg, inline=False)
    await ctx.channel.send(embed = p1)


@bot.command()
async def hangman(ctx):
    lives = 5
    f = False
    word = list(hm.hangman())
    question = ["_"]*len(word)
    question = question[:-1]
    p1 = discord.Embed(title = "Game: HangMan", color = 0x6c0101)
    msg = f"Hey {ctx.message.author.mention}! Given below is a {len(word)} characters long word, and you need to guess the correct word.\n After guessing, you need to send the correct answer in this chatbox."
    qn = f"`{question}`"
    p1.add_field(name = "Task Details", value = msg, inline = False)
    p1.add_field(name = "Question", value = qn, inline = False)
    p2 = discord.Embed(title = "HangMan", color = )
    while f or lives:



bot.run(token)
