import NewFunctionsPYC

client = NewFunctionsPYC.client("Token Bot Here") #Declare the bot

client.load_cogs("folderName") #If the folder is in the main location
client.load_cogs("folderName/subFolderName") #If the folder is inside another folder

client.__run__() # run The bot