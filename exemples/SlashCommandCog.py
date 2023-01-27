import discord
from discord.ext import commands
from NewFunctionsPYC import Slash_Command, slashContext

class SlashCommands(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @Slash_Command(
        name = "This is a name command", # Now the name convert for lowCase and replace spaces for _
        description = "This is a Description",
    )
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def NameSymbolic(self, Interaction: slashContext | discord.Interaction):
        """
        This decorator add SlashCommands
        """

        await Interaction.response.send_message("Hello World")
    
    @Slash_Command() #If name equal None the name of function is attributed the name command
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def hello_world(self, Interaction: slashContext | discord.Interaction):
        """
        This decorator add SlashCommands
        """

        await Interaction.response.send_message("Hello World")

def setup(bot:commands.Bot):
    bot.add_cog(SlashCommands(bot))