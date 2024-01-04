from NewFunctionsPYC import Bot, Collection
from discord import Interaction, option


client = Bot()
collectionGuildsLangs = Collection()


@client.event
async def on_ready():

    print(f"Entrei como {client.user.name}")

    for i in client.guilds:
        collectionGuildsLangs.set(f"{i.id}", "pt-BR")


@client.slash_command(name="teste_keys_collection", description="A command to teste function keys")
async def teste_keys_collection(interaction: Interaction):
    await interaction.response.send_message(f"{collectionGuildsLangs.keys()}")


@client.slash_command(name="teste_get_collection", description="A command to teste function get")
@option(name="item", description="Item you want to check out of the collection")
async def teste_get_collection(interaction: Interaction, item: str):
    await interaction.response.send_message(f"{collectionGuildsLangs.get(item)}")


@client.slash_command(name="teste_delete_collection", description="A command to teste function delete")
@option(name="item", description="Item you want to delete out of the collection")
async def teste_delete_collection(interaction: Interaction, item: str):
    collectionGuildsLangs.delete(item)
    await interaction.response.send_message("sucess")

@client.slash_command(name="teste_purge_collection", description="A command to teste function purge")
async def teste_purge_collection(interaction: Interaction):
    collectionGuildsLangs.purge()
    await interaction.response.send_message("sucess")


client.__run__()
