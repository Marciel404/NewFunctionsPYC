import NewFunctionsPYC, discord

client = NewFunctionsPYC.client("Token Bot Here")

client.upsertComand("command_name_slash", "This is a Description")

@client.event
async def on_interaction(interaction: discord.Interaction):

    match interaction.to_dict()["type"]:
        case 1: return
        case 2: 
            match interaction.to_dict()['data']['name']:
                case "command_name_slash":
                    await interaction.response.send_message("Hello World")
        case 3: return
        case 4: return
        case 5: return

client.__run__()