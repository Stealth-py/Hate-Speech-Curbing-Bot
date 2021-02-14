import discord
from discord.ext import commands
import sys
import os
pth = os.path.abspath(os.getcwd())
sys.path.append(pth + r"\\abuse_dir")
sys.path.append(pth + r"\\wordgames")
print(pth)
import mlbasedabusetofunny as abf
import jumbledwords as jw
import hangman as hm

token = '<your-token-here>'

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
    msg1 = "Hello! You can use the following commands to play various word games."
    msg2 = "1)`$jumble` to play Jumbled Words, where you'll be given one try to guess what the correct word is.\n 2)`$hangman`, to play HangMan, with 5 lives, where you need to either guess the correct letter in the word or guess the correct word."
    p1.add_field(name="Help", value=msg1, inline=False)
    p1.add_field(name = "Commands", value = msg2, inline=False)
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
    p1 = discord.Embed(title = "Game: HangMan", color = 0x6c0101)
    msg = f"Hey {ctx.message.author.mention}! Given below is a {len(word)} characters long word, and you need to guess the correct word.\n After guessing, you need to send the correct answer in this chatbox."
    qn = f"`{''.join(question)}`"
    p1.add_field(name = "Task Details", value = msg, inline = False)
    p1.add_field(name = "Question", value = qn, inline = False)
    await ctx.send(embed = p1)
    p2 = discord.Embed(title = "HangMan", color = 0x800080)
    x = ''.join(word)
    x = x.lower()
    msg = f"You have {lives} lives and your question is `{' '.join(question)}`.\n Respond with your choice below, either "
    p2.add_field(name = "Current Progress", value = msg, inline=False)
    editable = await ctx.send(embed = p2)
    while f or lives:
        p = discord.Embed(title = "HangMan", color = 0x800080)
        arg = await bot.wait_for('message', check = lambda message: message.author==ctx.author)
        guess = f"Your guess: `{arg.content}`."
        res = arg.content
        res = res.lower()
        if len(res)==len(x):
            if res == x:
                f = True
                break
            else:
                lives-=1
        else:
            if len(res)==1:
                if res in x:
                    for i in range(len(x)):
                        if x[i]==res:
                            question[i] = res
                else:
                    lives-=1
            else:
                lives-=1
        if ''.join(question)==x:
            f = True
            break
        qn = f"`{' '.join(question)}` and `{lives}` lives."
        p.add_field(name = "Current Progress", value = qn + "\n" + guess, inline=False)
        await editable.edit(embed = p)
        p = editable
        #print(editable)
    px = discord.Embed(title = "Result")
    print(f)
    if f:
        px.color = 0xdaa520
        msg = f"Congratulations {ctx.message.author.mention}! You got the correct answer!"
        px.add_field(name = "Won", value = msg, inline = False)
    else:
        px.color = 0xffffff
        msg = f"Sorry {ctx.message.author.mention}, you didn't win. Your lives ran out or your guess was not correct. The correct answer was {''.join(word)}."
        px.add_field(name = "Lost", value = msg, inline=False)
    await ctx.send(embed = px)


bot.run(token)
