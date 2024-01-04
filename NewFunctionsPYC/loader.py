from os import listdir, getenv, path
from discord.commands import ApplicationContext
from discord.ext import bridge
from discord import Intents, Game
from discord.ext.commands.context import Context
from dotenv import load_dotenv

def getTokenDotEnv():
    load_dotenv()
    token = getenv("token") or getenv("TOKEN")

    if token is None:
        raise Error("MISSING TOKEN")

    return token

class Error(Exception):
    pass

class BotBuilder(bridge.Bot):

    def __init__(self,
            token: str = None,
            command_prefix: str = "!",
            Intents: Intents = Intents.default(),
            poweredby: bool = True,
            case_insensitive: bool = True,
            auto_sync_commands: bool = True,
            **options
        ):

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

    def HybridCommand(self, **kwargs):
        return super().bridge_command(**kwargs)

    async def on_application_command_error(self, context: ApplicationContext, exception: Exception) -> None:
        await context.respond(content=f"Error: {exception}")
    
    async def on_command_error(self, context: Context, exception: Exception) -> None:
        await context.reply(content=f"Error: {exception}")

    async def on_ready(self):
            
        if self.poweredby == True:
            await self.change_presence(activity=Game(name="PoweredBy PyCord and NewFunctionsPYC"))
            print("PoweredBy PyCord and NewFunctionsPYC")

    def load_cogs(self, pathName: str):

        for file in listdir(pathName):

            if path.isdir(file) and not file.startswith("__"):

                self.loadcogs(pathName)

            elif file.endswith(".py") and not file.startswith("__"):

                self.load_extension('{}.{}'.format(pathName, file[:-3]))

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