import discord
from discord.ext import commands
import checks
import asyncio
import random

class sort():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(name='sort', pass_context=True)
    async def choice(self, ctx):
        '''See the galaxy, join the fleet TODAY! We want YOU to enlist today by clicking on the \U00002705 and you will randomly be assigned as a Galactic Trooper <:empire:382281804016648203> or a Rebel Trooper <:rebel:382281557479653376>. Please only click on it once we do not like dual enlisted troopers (aka traitors!)'''
        await self.bot.delete_message(ctx.message)

        msg = await self.bot.say('See the galaxy, join the fleet TODAY! We want YOU to enlist today by clicking on the \U00002705 and you will randomly be assigned as a Galactic Trooper <:empire:382281804016648203> or a Rebel Trooper <:rebel:382281557479653376>. Please only click on it once we do not like dual enlisted troopers (aka traitors!)')
        await self.bot.add_reaction(msg, '\U00002705')

        await asyncio.sleep(0.1)
        role1 = 0
        role2 = 0
        rebelArray = [2,4,6,8,10]
        galacticArray = [1,3,5,7,9]
        while True:
            res = await self.bot.wait_for_reaction(['\U00002705'], message=msg)
            randomnum = random.randint(1,10)
            faircheck = role1 - role2
            if faircheck == -2:
                randomnum = 1
            elif faircheck == 2:
                randomnum = 2
            if res.reaction.emoji == '\U00002705' and randomnum in galacticArray:
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Galactic Trooper'))
                role1 += 1
            elif res.reaction.emoji == '\U00002705' and randomnum in rebelArray:
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Rebel Trooper'))
                role2 += 1

def setup(bot):
    bot.add_cog(sort(bot))
