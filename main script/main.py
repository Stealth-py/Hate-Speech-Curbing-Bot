import discord
from discord.ext import commands

token = 'ODEwMTM1NTAwMTgyNTE5ODA4.YCfPeg.JgZ7PD7BL0yrQQ3KTctEvoi56xY'

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


@bot.command()
async def help(ctx):
    p1 = discord.Embed(title = "Help Section", color = 0x6c0101)
    msg1 = ""
    p1.add_field(name="Introduction", value=msg1, inline=False)
    await ctx.channel.send(embed = p1)

bot.run(token)