import NewFunctionsPYC, discord

client = NewFunctionsPYC.client("") #Declare the bot

client.load_cogs("commands")

client.__run__() # run The bot