import discord
from discord.ext import commands
import json
import asyncio
import sys
import checks
import os
try:
	from urllib.request import urlretrieve
except Exception as e:
	pass

import json
import unicodedata

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open('config.json') as json_data_file:
    cfg = json.load(json_data_file)

startup_plugins = cfg["startup_plugins"]

description = '''Currently avilable commands for the plugins and basics. Commands marked "No Category" are built in:'''
bot = commands.Bot(command_prefix=cfg["Prefix"], description=description, pm_help=None)

@bot.event
async def on_ready():
	# bot.remove_command("help")
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('Invite link: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=268446784'.format(bot.user.id))
	print('------')
	await bot.change_presence(game=discord.Game(name='Prefix: {0[0]} | Ready to help'.format(bot.command_prefix), type=1))


@bot.event
async def on_message(message):
	if message.author.bot:
		return
	if message.channel.is_private:
            # print('Private Message: @{} by {}:      {}'.format(str(message.timestamp)[:16], message.author, message.content))
            return
	await bot.process_commands(message)

########OWNER CMDS###########
@bot.command()
@checks.is_owner()
async def plug(extension_name : str):
    """Loads a Plugin."""
    try:
        bot.load_extension("plugins." + extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
@checks.is_owner()
async def unplug(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension("plugins." + extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.command()
@checks.is_owner()
async def reload(extension_name : str):
	"""Reloads an extension."""
	bot.unload_extension("plugins." + extension_name)
	bot.load_extension("plugins." + extension_name)
	await bot.say("{} reloaded.".format(extension_name))

@bot.command(pass_context=True)
@checks.is_owner()
async def cnick(ctx, *, nick : str):
	"""Change the nickname of the bot"""
	await bot.change_nickname(ctx.message.server.me, nick)
	await bot.say('Done.')

@bot.command(pass_context=True)
@checks.is_owner()
async def cname(ctx, *, nn : str):
	"""Change the name of the bot"""
	await bot.edit_profile(username = nn)
	await bot.say('Done.')

@bot.command(pass_context=True)
@checks.is_owner()
async def cavatar(ctx, link : str):
	"""Change the avatar of the bot"""
	urlretrieve(link, 'pp.jpg')
	with open("pp.jpg", "rb") as imageFile:
		file = imageFile.read()
		bytelike = bytearray(file)
		await bot.edit_profile(avatar = bytelike)
	await bot.say('Done.')


@purge.error
async def p_error(error, ctx):
	if isinstance(error, commands.BadArgument):
		await bot.say("That\'s not a number...")
	if isinstance(error, commands.CheckFailure):
		await bot.say("Insufficent permissions")




########OWNER CMDS###########


if __name__ == "__main__":
    for extension in startup_plugins:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(cfg["Token"])
