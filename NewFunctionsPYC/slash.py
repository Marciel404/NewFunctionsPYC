import discord

slashContext = discord.Interaction

def Slash_Command(name: str = None,
                description: str = None,
                guild_only: bool = False,
                nsfw: bool = False,
                guild_ids: list = None,
                name_localizations: dict = {},
                description_localizations: dict = {},
                **kwargs
                ) -> any:
    """For this to work the "auto_sync_commands" needs to be set to True"""

    if name != None: name = name.lower().replace(" ","_")
    
    return discord.slash_command(
        name = name, 
        description = description,
        guild_only = guild_only,
        nsfw = nsfw,
        name_localizations = name_localizations,
        description_localizations = description_localizations,
        guild_ids = guild_ids,
        **kwargs
    )