import NewFunctionsPYC

client = NewFunctionsPYC.client("") #Declare the bot

client.load_cogs("commands") #load Folder cogs

client.__run__() # run The bot