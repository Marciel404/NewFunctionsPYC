from discord.ext.bridge import bridge_command, BridgeContext

hybridContext = BridgeContext

def HybridCommand(name: str,
                description: str = None,
                guild_only: bool = False,
                nsfw: bool = False,
                guild_ids: list = None,
                name_localizations: dict = {},
                description_localizations: dict = {},
                usage: str = None, 
                aliases: list = [],
                enable: bool = True,
                help: str = None,
                **kwargs) -> any:
    """For this to work the "auto_sync_commands" needs to be set to True"""
    
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