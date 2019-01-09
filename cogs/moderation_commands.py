from discord.ext import commands;
#from discord import Member;
import constants;

class Moderation_Commands:
    def __init__(self, bot):
        self.bot = bot;

    @commands.command(pass_context=True)
    @commands.has_any_role(constants.ROLE_ADMIN, constants.ROLE_MOD)
    async def ban(self, ctx, member):
        await self.bot.guild.ban(member);



def setup(bot):
    bot.add_cog(Moderation_Commands(bot));