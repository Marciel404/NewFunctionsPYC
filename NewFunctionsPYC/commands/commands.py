import discord
from discord.ext import commands
from discord.ext.bridge import bridge_command

def SlashCommand(name: str = None,
                description: str = None,
                guild_only: bool = False,
                nsfw: bool = False,
                options: list = None,
                guild_ids: list = None,
                name_localizations: dict = None,
                description_localizations: dict = None,
                **kwargs
                ) -> any:
        
    if options == None:
        options = []
    if name_localizations == None:
        name_localizations = {}
    if description_localizations == None:
        description_localizations = {}
    
    return discord.slash_command(
        name = name, 
        description = description,
        guild_only = guild_only,
        nsfw = nsfw,
        options = options,
        name_localizations = name_localizations,
        description_localizations = description_localizations,
        guild_ids = guild_ids,
        **kwargs
    )

def CommandPrefix(name: str = None, 
                usage: str = None, 
                description: str = None,
                aliases: list = None,
                enable: bool = True,
                help: str = None,
                **kwargs
                ):

    if usage == None:
        usage = "Not provided"
    if description == None:
        description = "Not provided"
    if help == None:
        help = "Not provided"
    if aliases == None:
        aliases = []

    return commands.command(
        name = name,
        usage = usage,
        description = description,
        aliases = aliases,
        help = help,
        enable = enable,
        **kwargs
    )

def HybridCommand(name: str = None,
                description: str = None,
                guild_only: bool = False,
                nsfw: bool = False,
                options: list = None,
                guild_ids: list = None,
                name_localizations: dict = None,
                description_localizations: dict = None,
                #Comand Prefix
                usage: str = None,
                aliases: list = None,
                enable: bool = True,
                help: str = None,
                **kwargs
                ):
    
    return bridge_command()