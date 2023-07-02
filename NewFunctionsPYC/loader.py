from os import listdir, getenv
from discord.ext import bridge
from discord import Intents, Game
from dotenv import load_dotenv

from NewFunctionsPYC.clientLogin import ClientAPI
from .commands.options import Choice

def getTokenDotEnv():
    load_dotenv()
    token = getenv("token") or getenv("TOKEN")

    if token is None:
        raise Error("MISSING TOKEN")
    return token

class Error(Exception):
    pass

defaultIntents: Intents = Intents(
    message_content = True,
    members = True,
    messages = True,
    guild_messages = True
)

class BotBuilder(bridge.Bot):

    def __init__(self,
            token: str = None,
            command_prefix: str = None,
            Intents: Intents = None,
            poweredby: bool = True,
            case_insensitive: bool = True,
            auto_sync_commands: bool = True,
            **options
        ):

        if command_prefix == None:
            command_prefix = "!"
        if Intents == None:
            Intents = defaultIntents
        
        self.token: str = token
        self.poweredby: bool = poweredby
        self.commandsREGISTER: list[dict[str,str]] = []

        super().__init__(
            command_prefix = command_prefix,  
            intents = Intents,
            auto_sync_commands = auto_sync_commands,
            case_insensitive = case_insensitive,
            **options
        )
    
    async def on_ready(self):

        if self.commandsREGISTER.__len__() > 0 and not self.auto_sync_commands:

            await ClientAPI.CreateApplicationCommand(
                token = self.token,
                commandsREGISTER = self.commandsREGISTER,
                botId = self.user.id
            )
            
        if self.poweredby == True:
            await self.change_presence(activity=Game(name="PoweredBy PyCord and NewFunctionsPYC"))
            print("PoweredBy PyCord and NewFunctionsPYC")

    def upsertSlashCommand(
            self,
            name: str,
            description: str = "Description not provided",
            nsfw: bool = False,
            options: list[Choice] = [],
            guild_ids: list = None,
            name_localizations: dict = {},
            description_localizations: dict = {},
            guild_only: bool = None,
            logRegister: bool = True
        ) -> any:

        """For this to work the "auto_sync_commands" needs to be set to False"""

        if guild_only is None:
            guild_only = True
        else:
            guild_only = False

        dictCommand = {
            "type": 1,
            "name": name,
            "description": description,
            "nsfw": nsfw,
            "options": options,
            "guild_ids":guild_ids,
            "name_localizations": name_localizations,
            "description_localizations": description_localizations,
            "dm_permission": guild_only,
            "logRegister": logRegister
        }

        self.commandsREGISTER.append(dictCommand)
    
    def upsertUserCommand(
            self,
            name: str,
            nsfw: bool = False,
            guild_ids: list = None,
            name_localizations: dict = {},
            guild_only: bool = None,
            logRegister: bool = True
        ) -> any:
        """For this to work the "auto_sync_commands" needs to be set to False"""

        if guild_only is None:
            guild_only = True
        else:
            guild_only = False

        dictCommand = {
            "type": 2,
            "name": name,
            "nsfw": nsfw,
            "guild_ids":guild_ids,
            "name_localizations": name_localizations,
            "dm_permission": guild_only,
            "logRegister": logRegister
        }

        self.commandsREGISTER.append(dictCommand)
    
    def upsertMessageCommand(
            self,
            name: str,
            nsfw: bool = False,
            guild_ids: list = None,
            name_localizations: dict = {},
            guild_only: bool = None,
            logRegister: bool = True
        ) -> any:
        """For this to work the "auto_sync_commands" needs to be set to False"""

        if guild_only is None:
            guild_only = True
        else:
            guild_only = False

        dictCommand = {
            "type": 3,
            "name": name,
            "nsfw": nsfw,
            "guild_ids":guild_ids,
            "name_localizations": name_localizations,
            "dm_permission": guild_only,
            "logRegister": logRegister
        }

        self.commandsREGISTER.append(dictCommand)

    def load_cogs(self, folder: str):

        if folder.startswith("./") or folder.startswith("."):
            folder = folder.strip("./")
            
        for cogs in listdir(f"{folder}"):
            if cogs.endswith(".py") and not cogs.startswith("__"):
                self.load_extensions("{0}.{1}".format(folder.replace("/", "."),cogs[:-3]))

    def __run__(self):
        if self.token == None or self.token == "":
            self.token = getTokenDotEnv()
        try:
            self.run(self.token)
        except Exception as error:
            raise Error(error)

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