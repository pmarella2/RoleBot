import discord
from discord.ext import commands
import checks
import asyncio
class ranks():
    def __init__(self, bot):
        self.bot = bot
    @checks.is_owner()
    @commands.command(name='ranks', pass_context=True)
    async def choice(self, ctx):
        '''PLACEHOLDER MSG'''
        await self.bot.delete_message(ctx.message)
        msg = await self.bot.say('PLACEHOLDER MSG')
        await self.bot.add_reaction(msg, '368151944805744650')
        await self.bot.add_reaction(msg, '368152261685411840')
        await self.bot.add_reaction(msg, '368151006200201237')
        await self.bot.add_reaction(msg, '368152708814864386')
        await self.bot.add_reaction(msg, '368153006396407808')
        await self.bot.add_reaction(msg, '385706005239169024')
        await self.bot.add_reaction(msg, '385707263026790403')
        await self.bot.add_reaction(msg, '385708022120316928')

        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction(['368151944805744650', '368152261685411840', '368151006200201237', '368152708814864386', '368153006396407808', '385706005239169024', '385707263026790403', '385708022120316928'], message=msg)
            if res.reaction.emoji == '368151944805744650':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Overwatch'))
            elif res.reaction.emoji == '368152261685411840':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='League of Legends'))
            elif res.reaction.emoji == '368151006200201237':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Hearthstone'))
            elif res.reaction.emoji == '368152708814864386':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Heroes of the Storm'))
            elif res.reaction.emoji == '368153006396407808':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Rocket League'))
            elif res.reaction.emoji == '385706005239169024':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='CS:GO'))
            elif res.reaction.emoji == '385707263026790403':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Smite'))
            elif res.reaction.emoji == '385708022120316928':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='PUBG'))

def setup(bot):
    bot.add_cog(ranks(bot))