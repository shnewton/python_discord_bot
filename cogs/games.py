from random import *;
from discord.ext import commands;

class Games:
    def __init__(self, bot):
        self.bot = bot;

    @commands.command(pass_context=True)
    async def roll(self, ctx):
        rand = randint(1, 6);
        user = ctx.message.author;
        await self.bot.say(format(user.mention) + " rolled a " + "**`" + format(rand) + "`**");

    @commands.command(pass_context=True)
    async def flip(self, ctx):
        rand = randint(0, 1);
        user = ctx.message.author;
        output = "";

        if rand == 1:
            output = "`HEADS`";
        else:
            output = "`TAILS`";

        await self.bot.say(format(user.mention) + " flipped and got " + "`"  + output + "`!");

def setup(bot):
    bot.add_cog(Games(bot));