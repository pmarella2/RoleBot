import discord
from discord.ext import commands
import checks
import asyncio
class ranks2():
    def __init__(self, bot):
        self.bot = bot
    @checks.is_owner()
    @commands.command(name='ranks2', pass_context=True)
    async def choice(self, ctx):
        '''-------------------------------------------------------------------------------------------------------- \n | Greetings! I will be taking care of handing out tags today. \n \n | In order to receive your desired game tag please click on the appropriate reaction (emoji). \n \n | **Possible tags**: \n | Overwatch: <:OW:414502052991991823> \n | League of Legends: <:LoL:414502064811409418> \n | Super Smash Bros: <:SB:414502086261211156> \n | Rocket League: <:RL:414502074869350402> \n -------------------------------------------------------------------------------------------------------- \n'''
        await self.bot.delete_message(ctx.message)
        msg = await self.bot.say('-------------------------------------------------------------------------------------------------------- \n | Greetings! I will be taking care of handing out tags today. \n \n | In order to receive your desired game tag please click on the appropriate reaction (emoji). \n \n | **Possible tags**: \n | Overwatch: <:OW:414502052991991823> \n | League of Legends: <:LoL:414502064811409418> \n | Super Smash Bros: <:SB:414502086261211156> \n | Rocket League: <:RL:414502074869350402> \n -------------------------------------------------------------------------------------------------------- \n')
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='414502052991991823'))
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='414502064811409418'))
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='414502086261211156'))
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='414502074869350402'))

        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction([discord.utils.get(self.bot.get_all_emojis(), id='414502052991991823'), discord.utils.get(self.bot.get_all_emojis(), id='414502064811409418'), discord.utils.get(self.bot.get_all_emojis(), id='414502086261211156'), discord.utils.get(self.bot.get_all_emojis(), id='414502074869350402'), discord.utils.get(self.bot.get_all_emojis(), id='368153006396407808'), discord.utils.get(self.bot.get_all_emojis(), id='385706005239169024'), discord.utils.get(self.bot.get_all_emojis(), id='385707263026790403')], message=msg)
            if res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='414502052991991823'):
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Overwatch'))
            elif res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='414502064811409418'):
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='League of Legends'))
            elif res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='414502086261211156'):
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Super Smash Bros'))
            elif res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='414502074869350402'):
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Rocket League'))

def setup(bot):
    bot.add_cog(ranks2(bot))
