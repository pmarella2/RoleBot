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
        '''-------------------------------------------------------------------------------------------------------- \n | Greetings! I will be taking care of handing out tags today. \n \n | In order to receive your desired game tag please click on the appropriate reaction (emoji). \n \n | **Possible tags**: \n | Overwatch: <:OW:368151944805744650> \n | League of Legends: <:LOL:368152261685411840> \n | Hearthstone: <:HS:368151006200201237> \n | Heroes of the Storm: <:HOTS:368152708814864386> \n | Rocket League: <:RL:368153006396407808> \n | CS:GO: <:CSGO:385706005239169024> \n | Smite: <:SMITE:385707263026790403> \n -------------------------------------------------------------------------------------------------------- \n'''
        await self.bot.delete_message(ctx.message)
        msg = await self.bot.say('-------------------------------------------------------------------------------------------------------- \n | Greetings! I will be taking care of handing out tags today. \n \n | In order to receive your desired game tag please click on the appropriate reaction (emoji). \n \n | **Possible tags**: \n | Overwatch: <:OW:368151944805744650> \n | League of Legends: <:LOL:368152261685411840> \n | Hearthstone: <:HS:368151006200201237> \n | Heroes of the Storm: <:HOTS:368152708814864386> \n | Rocket League: <:RL:368153006396407808> \n | CS:GO: <:CSGO:385706005239169024> \n | Smite: <:SMITE:385707263026790403> \n -------------------------------------------------------------------------------------------------------- \n')
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='368151944805744650'))
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='368152261685411840'))
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='368151006200201237'))
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='368152708814864386'))
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='368153006396407808'))
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='385706005239169024'))
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='385707263026790403'))

        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction([discord.utils.get(self.bot.get_all_emojis(), id='368151944805744650'), discord.utils.get(self.bot.get_all_emojis(), id='368152261685411840'), discord.utils.get(self.bot.get_all_emojis(), id='368151006200201237'), discord.utils.get(self.bot.get_all_emojis(), id='368152708814864386'), discord.utils.get(self.bot.get_all_emojis(), id='368153006396407808'), discord.utils.get(self.bot.get_all_emojis(), id='385706005239169024'), discord.utils.get(self.bot.get_all_emojis(), id='385707263026790403')], message=msg)
            if res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='368151944805744650'):
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Overwatch'))
            elif res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='368152261685411840'):
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='League of Legends'))
            elif res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='368151006200201237'):
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Hearthstone'))
            elif res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='368152708814864386'):
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Heroes of the Storm'))
            elif res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='368153006396407808'):
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Rocket League'))
            elif res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='385706005239169024'):
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='CS:GO'))
            elif res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='385707263026790403'):
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Smite'))

def setup(bot):
    bot.add_cog(ranks(bot))
