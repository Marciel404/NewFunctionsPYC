import discord
from discord.ext import commands
from NewFunctionsPYC import EmbedBuilder, CommandPrefix, prefixContext

class embeds(commands.Cog):

    def __init__(self, bot:commands.Bot):
        
        self.bot = bot

    @CommandPrefix() #If name equal None the name of function is attributed the name command
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def embed(self, ctx: prefixContext):

        e: EmbedBuilder = EmbedBuilder() #Start the embed

        e.set_title("test") #Define the title
        e.set_description("test2") #Define the description
        e.set_color(11542) #Define Color

        await ctx.send(embed = e.build()) #Build the embed and send message

        e.remove_description() #Remove the description
        e.set_title("Hello")
        e.set_colour(5544)

        await ctx.send(embed = e.build()) #Build the embed and send message

        e.set_footer(text="Tests")
        e.remove_title() #Remove the title
        e.remove_colour() #Remove the color

        await ctx.send(embed = e.build()) #Build the embed and send message

    @CommandPrefix(name = "embedif") 
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def NameSymbolic(self, ctx: prefixContext, mod: int): # condition with if or match case(python3.10+)

        e: EmbedBuilder = EmbedBuilder() #Start the embed

        match mod:

            case 1:

                e.set_title(f"This is title {mod}") #Define the title
                e.set_description(f"this is description {mod}") #Define the description
                e.set_color(11542) #Define the color
                e.set_author(name = "TEste") #Define the author
            
            case 2: 

                e.set_title(f"This is title {mod}") #Define the title
                e.set_description(f"this is description {mod}") #Define the description
                e.set_colour(5544)#Define the color
                e.add_field(name = "teste", value = "teste") #add field
                e.add_field(name = "teste2", value = "teste2") #add field

            case 3:

                e.set_footer(text="Tests") #Define the footer
                e.set_title(f"This is title {mod}") #Define the title
                e.set_description(f"this is description {mod}") #Define the description

        await ctx.send(embed = e.build()) #Build the embed and send message

def setup(bot:commands.Bot):
    bot.add_cog(embeds(bot))