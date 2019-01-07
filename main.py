from discord.ext import commands;
import constants
import discord;
import token;


client = commands.Bot(command_prefix=constants.PREFIX);
client.load_extension("cogs.games");
client.load_extension("cogs.testing");
client.load_extension("cogs.chat_commands");

@client.event
async  def on_ready():
    print("Bot is ready!");

@client.event
async def on_member_join(member):
    msg = "Welcome to " + "***" + format(member.server.name) + "*** " + format(member.mention);
    role = discord.utils.get(member.server.roles, name="New");
    await client.add_roles(member, role);
    await client.send_message(client.get_channel(constants.LOBBY_CHANNEL), msg);

client.run(token.TOKEN);