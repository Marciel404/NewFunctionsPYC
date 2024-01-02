from discord.ext import commands
from NewFunctionsPYC import HybridCommand, hybridContext

class HybridCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):

        self.bot = bot

    @HybridCommand(
        name = "Teste" # Now the name convert for lowCase and replace spaces for _ (Required)
    )
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def NameSymbolic(self, ctx: hybridContext):
        """
        This decorator add SlashCommands and PrefixCommands
        """

        await ctx.reply("Hello World")

def setup(bot:commands.Bot):
    bot.add_cog(HybridCommands(bot))