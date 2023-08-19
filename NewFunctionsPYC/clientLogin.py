import asyncio
import aiohttp

class ClientAPI:

    urlBase = "https://discord.com/api/v10/"
    urlRegisterCommand = "applications/{}/commands"
    urlRegisterCommandGuilds = "applications/{}/guilds/{}/commands"

    @classmethod
    async def CreateApplicationCommand(cls, **kwargs):

        async with aiohttp.ClientSession() as request:

            for i in kwargs.get("commandsREGISTER"):
                logR = i["logRegister"]
                i.pop("logRegister")

                if i["guild_ids"] is None:
                    url = f"{cls.urlBase}/{cls.urlRegisterCommand.format(kwargs.get('botId'))}"
                else:
                    url = f"{cls.urlBase}/{cls.urlRegisterCommandGuilds.format(kwargs.get('botId'), i['guild_id'])}"
                
                async with request.post(url=url,json=i,headers={"Authorization": f"Bot {kwargs.get('token')}"}) as e:
                    if logR:
                        if e.status == 201:
                            if e.reason == "Created":
                                print(f"{i['name']} registered sucefully")
                        elif e.status == 200:
                            print(f"{i['name']} is already registered")
                        else:
                            print(f"Error registering {i['name']}")
                    await asyncio.sleep(5)
    