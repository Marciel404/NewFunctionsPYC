import discord
import NewFunctionsPYC
from discord.ext import commands

client = NewFunctionsPYC.client("Token Here") #Declare the bot

@client.slash_command(name = "slash") #slashCommand
async def slash(Interaction: NewFunctionsPYC.slashContext | discord.Interaction):

    await Interaction.response.send_message("Hello World")

@client.command() #PrefixCommand
async def slash(Interaction: NewFunctionsPYC.prefixContext | commands.Context):

    await Interaction.send("Hello World")

client.__run__() # run The bot