import discord
from discord.ext import command

slashContext = discord.Interaction

def Slash_Command(name: str = None,
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
    if name != None:
        name = name.lower().replace(" ","_")
    
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