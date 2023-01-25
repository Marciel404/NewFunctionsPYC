import discord
from discord.ext.bridge import bridge_command, BridgeContext

hybridContext = BridgeContext

def HybridCommand(name: str,
                description: str = None,
                guild_only: bool = False,
                nsfw: bool = False,
                options: list = None,
                guild_ids: list = None,
                name_localizations: dict = None,
                description_localizations: dict = None,
                usage: str = None, 
                aliases: list = None,
                enable: bool = True,
                help: str = None,
                **kwargs) -> any:
    
    if options == None:
        options = []
    if name_localizations == None:
        name_localizations = {}
    if description_localizations == None:
        description_localizations = {}
    if name != None:
        name = name.lower().replace(" ","_")
    if description == None:
        description = "No description provided"
    if usage == None:
        usage = "Not provided"
    if description == None:
        description = "Not provided"
    if help == None:
        help = "Not provided"
    if aliases == None:
        aliases = []

    return bridge_command(
        name = name,
        description = description,
        name_localizations = name_localizations,
        description_localizations = description_localizations,
        guild_only = guild_only,
        nsfw = nsfw,
        guild_ids = guild_ids,
        usage = usage, 
        aliases = aliases,
        enable = enable,
        help = help,
        kwargs=kwargs
    )