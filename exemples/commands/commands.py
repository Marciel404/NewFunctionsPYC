import discord
from discord.ext import commands
from NewFunctionsPYC import embedBuilder

class CogName(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name = "embed",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context):

        e: embedBuilder = embedBuilder()

        e.set_title("test")
        e.set_description("test2")

        await ctx.send(embed = e)

        e.remove_description()
        e.set_title("Hello")

        await ctx.send(embed = e)

        e.set_footer(text="Tests")
        e.remove_title()

        await ctx.send(embed = e)


def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))