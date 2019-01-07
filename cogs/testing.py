import constants;
from discord.ext import commands;

class Testing:
    def __init__(self, bot):
        self.bot = bot;

    @commands.command()
    @commands.has_any_role(constants.ROLE_ADMIN, constants.ROLE_MOD, constants.ROLE_TRUSTED)
    async def ping(self):
        await self.bot.say("Pong!");

    @ping.error
    async def ping_error(self, ctx, error):
        if isinstance(error, commands.Context):
            await self.bot.say(constants.PERMISSION_DENIED);

def setup(bot):
    bot.add_cog(Testing(bot));