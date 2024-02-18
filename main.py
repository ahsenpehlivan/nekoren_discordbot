import discord
from discord.ext.commands import Bot
from functions import *

botum = Bot(command_prefix="777 ", intents=discord.Intents.all())
game = Game()


@botum.event
async def on_ready():
    print("çalışmaya hazır!")


@botum.event
async def on_member_join(member):
    print(f"{member} gelmiş, hoş gelmiş.. buyursun..")
    channel = discord.utils.get(member.guild.text_channels, name="hello-bitches")
    await channel.send(f"{member} gelmiş, hoş gelmiş..")

@botum.event
async def on_member_remove(member):
    print(f"{member} gitmiş, üzüldük.. umarım geri gelir.. gelmezse de canı sağ olsun")
    channel = discord.utils.get(member.guild.text_channels, name="hello-bitches")
    await channel.send(f"{member} gitmiş, üzüldük.. umarım geri gelir.. gelmezse de canı sağ olsun")


@botum.command(aliases=["oyun", "game"])
async def hgdeneme(ctx, *args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:
        await ctx.send("selam")


@botum.command()
async def ahsen(ctx):
    await ctx.send("pehlivan")


@botum.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


botum.run("MTIwODUwMzQwNDQzMTgwMjM3OA.G_n4fm.5akdJWpduLPnTpfZA0JKuJV0HWDa7D_JmICmoc")
