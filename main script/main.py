import discord
from discord.ext import commands
import sys
sys.path.insert(1, r'C:\Users\gener\OneDrive\Documents\GitHub\onlyFANS-Byld-WIT-Hackathon-21-\abuset_dir')
import abusetofunny as abf

token = 'ODEwMTM1NTAwMTgyNTE5ODA4.YCfPeg.4K0AGug6N8muvTr7V6Pv_Pydd2U'

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
    #flag, processed_msg = abf.abuse_set(message)
    if "hello" in message.content:
        processed_msg = "bruh"
        await message.edit(content=processed_msg)

@bot.command()
async def help(ctx):
    p1 = discord.Embed(title = "Help Section", color = 0x6c0101)
    msg1 = ""
    p1.add_field(name="Help", value=msg1, inline=False)
    await ctx.channel.send(embed = p1)
bot.run(token)
