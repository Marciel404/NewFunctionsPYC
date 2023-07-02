import aiohttp

class ClientAPI:

    urlBase = "https://discord.com/api/v10/"
    urlRegisterCommand = "applications/{}/commands"
    urlRegisterCommandGuilds = "applications/{}/guilds/{}/commands"
    
    async def post(self, action, **kwargs):

        async with aiohttp.ClientSession() as request:

            if action == "regSlashCommands":

                for i in kwargs.get("commandsREGISTER"):
                    logR = i["logRegister"]
                    i.pop("logRegister")

                    if i["guild_ids"] is None:
                        url = f"{self.urlBase}/{self.urlRegisterCommand.format(kwargs.get('botId'))}"
                    else:
                        url = f"{self.urlBase}/{self.urlRegisterCommandGuilds.format(kwargs.get('botId'), i['guild_id'])}"
                    
                    async with request.post(url=url,json=i,headers={"Authorization": f"Bot {kwargs.get('token')}"}) as e:
                        if logR:
                            if e.status == 201:
                                print(f"{i['name']} registered sucefully")
                            else:
                                print(f"Error registering {i['name']}")