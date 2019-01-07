from random import *;
from discord.ext import commands;
from discord import Member;

class Moderation_Commands:
    def __init__(self, bot):
        self.bot = bot;





def setup(bot):
    bot.add_cog(Moderation_Commands(bot));