import discord
from discord.ext import commands
import checks
import asyncio

class sort():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(name='sort', pass_context=True)
    async def choice(self, ctx):
        '''Testing hopefully this works!'''
        await self.bot.delete_message(ctx.message)

        msg = await self.bot.say('Testing hopefully this works!')
        await self.bot.add_reaction(msg, '\U0001f916')

        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction(['\U0001f916'], message=msg)
            if res.reaction.emoji == '\U0001f916':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='robot'))


def setup(bot):
    bot.add_cog(sort(bot))