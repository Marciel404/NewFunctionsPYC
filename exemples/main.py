import NewFunctionsPYC

client = NewFunctionsPYC.client("tokenBot")

client.load_cogs("commands")

client.__run__()