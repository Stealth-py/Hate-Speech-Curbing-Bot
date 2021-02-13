import discord
from discord.ext import commands
import sys
import os
pth = os.path.abspath(os.getcwd())
sys.path.append(pth + r"\\abuse_dir")
import abusetofunny as abf

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
    flag, processed_msg = abf.changeabuse(message.content)
    if flag and message.author.id != bot.user.id:
        await message.channel.purge(limit = 1)
        await message.channel.send(processed_msg)
    print(message.content, " -> ", processed_msg, ": ", flag)


@bot.command()
async def help(ctx):
    p1 = discord.Embed(title = "Help Section", color = 0x6c0101)
    msg1 = ""
    p1.add_field(name="Help", value=msg1, inline=False)
    await ctx.channel.send(embed = p1)
bot.run(token)
