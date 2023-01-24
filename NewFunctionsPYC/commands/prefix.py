import discord
from discord.ext import commands

prefixContext = commands.Context

def CommandPrefix(name: str = None, 
                usage: str = None, 
                description: str = None,
                aliases: list = None,
                enable: bool = True,
                help: str = None,
                **kwargs
                )-> any:

    if usage == None:
        usage = "Not provided"
    if description == None:
        description = "Not provided"
    if help == None:
        help = "Not provided"
    if aliases == None:
        aliases = []
    if name != None:
        name = name.lower().replace(" ","_")

    return commands.command(
        name = name,
        usage = usage,
        description = description,
        aliases = aliases,
        help = help,
        enable = enable,
        **kwargs
    )