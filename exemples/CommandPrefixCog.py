from discord.ext import commands
from NewFunctionsPYC import CommandPrefix, prefixContext


class CommandsPrefix(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @CommandPrefix(
        name = "Teste" # Now the name convert for lowCase and replace spaces for _
    )
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def NameSymbolic(self, ctx: prefixContext):
        """
        This decorator add PrefixCommands
        """

        await ctx.send("Hello World")
    
    @CommandPrefix() #If name equal None the name of function is attributed the name command
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def hello_World(self, ctx: commands.Context):
        """
        This decorator add PrefixCommands
        """

        await ctx.send("Hello World")


def setup(bot:commands.Bot):
    bot.add_cog(CommandsPrefix(bot))
