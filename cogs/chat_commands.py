from discord.ext import commands;
import constants;

class Chat_Commands:
    def __init__(self, bot):
        self.bot = bot;

    @commands.command(pass_context=True)
    @commands.has_any_role(constants.ROLE_ADMIN, constants.ROLE_MOD, constants.ROLE_TRUSTED)
    async def echo(self, ctx, *args):
        user = ctx.message.author;
        output = "";
        for word in args:
            output += word + " ";
        await self.bot.say(output);

    @echo.error
    async def echo_error(self, ctx, error):
        if isinstance(error, commands.Context):
            await self.bot.say(constants.PERMISSION_DENIED);


def setup(bot):
    bot.add_cog(Chat_Commands(bot));