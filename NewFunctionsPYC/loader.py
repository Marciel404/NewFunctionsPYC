from os import listdir
import discord
from discord.ext import commands, bridge
from discord import Intents, Game

defaultIntents: Intents = Intents(
        message_content = True,
        members = True,
        messages = True
)

class BotBuilder(bridge.Bot):

    def __init__(self,
            token: str,
            command_prefix: str = None,
            Intents: Intents = None,
            poweredby: bool = True,
            case_insensitive: bool = True,
            auto_sync_commands: bool = True,
            **options
        ):

        if token == None or token == "":
            raise print("Token is a argument required")
        if command_prefix == None:
            command_prefix = "!"
        if Intents == None:
            Intents = defaultIntents
        
        self.token: str = token
        self.poweredby: bool = poweredby

        super().__init__(
            command_prefix = command_prefix,  
            intents = Intents,
            auto_sync_commands = auto_sync_commands,
            case_insensitive = case_insensitive,
            **options
        )
    
    async def on_ready(self):
        if self.poweredby == True:
            await self.change_presence(activity=Game(name="PoweredBy PyCord and NewFunctionsPYC"))
            print("PoweredBy PyCord and NewFunctionsPYC")

    def upsertComand(
            self,
            name: str,
            description: str = None,
            guild_only: bool = False,
            nsfw: bool = False,
            guild_ids: list = None,
            name_localizations: dict = {},
            description_localizations: dict = {},
            **kwargs
        ) -> any:

        if name != None:
            name = name.lower().replace(" ","_")

        @self.slash_command(
            name=name,
            description=description,
            nsfw=nsfw,
            guild_only=guild_only,
            guild_ids=guild_ids,
            name_localizations=name_localizations,
            description_localizations=description_localizations,
            kwargs=kwargs
        )
        async def add(ctx):
            pass
    
    def load_cogs(self, folder: str):

        if folder.startswith("./") or folder.startswith("."):
            folder = folder.strip("./")
            
        for cogs in listdir(f"{folder}"):
            if cogs.endswith(".py") and not cogs.startswith("__"):
                self.load_extensions("{0}.{1}".format(folder.replace("/", "."),cogs[:-3]))

    def __run__(self):
        if self.token == None or self.token == "":
            raise print("Token is a argument required")
        try:
            self.run(self.token)
        except Exception as error:
            return print("Error: {}".format(error))

class client(BotBuilder):
    """Represents a discord bot.

    This class is a subclass of :class:`NewFunctionsPYC.BotBuilder` and as a result
    anything that you can do with a :class:`discord.Bot` you can do with
    this bot.
    """

class Bot(BotBuilder):
    """Represents a discord bot.

    This class is a subclass of :class:`NewFunctionsPYC.BotBuilder` and as a result
    anything that you can do with a :class:`discord.Bot` you can do with
    this bot.
    """

class bot(BotBuilder):
    """Represents a discord bot.

    This class is a subclass of :class:`NewFunctionsPYC.BotBuilder` and as a result
    anything that you can do with a :class:`discord.Bot` you can do with
    this bot.
    """

class Client(BotBuilder):
    """Represents a discord bot.

    This class is a subclass of :class:`NewFunctionsPYC.BotBuilder` and as a result
    anything that you can do with a :class:`discord.Bot` you can do with
    this bot.
    """