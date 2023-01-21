from os import listdir
from discord.ext.commands import Bot as BotBase
from discord import Intents, Game

defaultIntents: Intents = Intents.default()
defaultIntents.message_content = True

class client(BotBase):

    def __init__(self, token: str = None, command_prefix: str = None, Intents: Intents = None, poweredby: bool = True, **options):

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
            **options
        )
    
    async def on_ready(self):
        if self.poweredby == True:
            await self.change_presence(activity=Game(name="PoweredBy PyCord and BetterFunctions"))
            print("PoweredBy PyCord and BetterFunctions")
    
    def load_cogs(self, folder: str):

        if folder.startswith("./"):
            folder = folder.strip("./")
            
        for cogs in listdir(f"./{folder}"):
            if cogs.endswith(".py") and not cogs.startswith("__"):
                self.load_extensions("{0}.{1}".format(folder.replace("/", "."),cogs[:-3]))
    
    def __run__(self):
        if self.token == None or self.token == "":
            raise print("Token is a argument required")
        try:
            self.run(self.token)
        except Exception as error:
            return print(error)

class Client(client):
    """Represents a discord bot.

    This class is a subclass of :class:`betterFunctions.client` and as a result
    anything that you can do with a :class:`discord.Bot` you can do with
    this bot.
    """

class Bot(client):
    """Represents a discord bot.

    This class is a subclass of :class:`betterFunctions.client` and as a result
    anything that you can do with a :class:`discord.Bot` you can do with
    this bot.
    """

class bot(client):
    """Represents a discord bot.

    This class is a subclass of :class:`betterFunctions.client` and as a result
    anything that you can do with a :class:`discord.Bot` you can do with
    this bot.
    """