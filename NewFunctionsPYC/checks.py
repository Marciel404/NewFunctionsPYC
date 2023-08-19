import aiohttp
from discord.ext import commands

class NoGuild(commands.CommandError):

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or "This command cannot be used in private messages")

class NoVote(commands.CommandError):

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or "You didn't vote for top.gg to use this")

class NoRole(commands.CommandError):

    def __init__(self, missing_roles: str | None = None, *args) -> None:

        missing = [f"'{role}'" for role in missing_roles]

        if len(missing) > 2:
            fmt = f"{', '.join(missing[:-1])}, or {missing[-1]}"
        else:
            fmt = " or ".join(missing)

        message = f"You don't have the role: {fmt}"

        super().__init__(message, *args)

def has_roles(*roles):

    def check(ctx: commands.Context):

        if ctx.guild is None:
            raise NoGuild()

        roles2 = []
        for i in roles:
            if type(i) == int:
                roles2.append(i)
            elif type(i) == str:
                roles2.append(i.lower())

        v = 0
        while True:
            if v == ctx.author.roles.__len__() or ctx.author.roles.__len__() < 2:
                raise NoRole(roles2)
            elif ctx.author.roles[v].id in roles2 or ctx.author.roles[v].name.lower() in roles2:
                break
            else:
                v += 1
        return True

    return commands.check(check)

def checkVoteTopGG(topauth: str, arg: str | None = None):

    """
    A decorator for check if the user command has voted in top.gg

    .. versionadded:: 1.4

    Parameters
    ------------
    topauth: :class:`str`
        An argument for authenticate the connection in API top.gg and check vote
        the :func:`check` decorator.
    
    arg: :class:`str`
        An argument for use a message custom

    Raises
    -------
    TypeError
        A check passed has not voted

    Exemple
    -------

    @bot.command()\n
    @NewFunctionsPYC.checkVoteTopGG(topauth = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEwMTIxMjE2NDE5NDc1MTcwNjgiLCJib3QiOnRydWfef1494fwefwef20",
    arg = "You not voted in top.gg")\n
    async def voteTopGG(ctx):\n
        await ctx.send('You voted!')
    """

    async def check(ctx):

        async with aiohttp.ClientSession() as request:
            async with request.get(url=f"https://top.gg/api/bots/{ctx.me.id}/check?userId={ctx.author.id}", headers={"Authorization": topauth}) as RequestResponse:
                if RequestResponse.status == 200:
                    response = await RequestResponse.json()
                else:
                    raise NoVote("Error checking vote on top.gg")

        if response['voted'] == 0:
            raise NoVote(arg)

        return True

    return commands.check(check)
