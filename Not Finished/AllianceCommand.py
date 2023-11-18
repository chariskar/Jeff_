import disnake
from disnake.ext import commands
from Utils.Embeds import Embeds
from Utils.CommandTools import CommandTools
import aiohttp

class AllianceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = 'https://emctoolkit.vercel.app/api/aurora/'

    @commands.slash_command(description="Alliance-related commands.")
    async def alliance(self, inter: disnake.ApplicationCommandInteraction):
        pass


    @alliance.sub_command(description="Retrieve and display general information about an alliance.")
    async def info(
            self,
            inter: disnake.ApplicationCommandInteraction,
            alliance: str = commands.param('name')):
        """Retrieve and display general information about an alliance."""
        commandString = f"/alliance info {alliance}"

        try:
            url = str(self.url + alliance)
            async with aiohttp.ClientSession as session:
                async with session.get(url=url) as response:
                    allianceInfo = await response.json()


            embed = Embeds.embed_builder(
                title=f'Alliance info about {alliance}',
                footer='made by charis_k',
                author=inter.author
            )

            embed.add_field(name="Leader/s", value=allianceInfo["leaderName"], inline=True)
            embed.add_field(name="Members", value=allianceInfo['nations'], inline=False)
            embed.add_field(name="Towns", value=allianceInfo["towns"], inline=True)
            embed.add_field(name='Residents', value=allianceInfo['residents'],inline=True)
            embed.add_field(name='Online', value=allianceInfo['online'],inline=True)
            embed.add_field(name='Discord invite', value=allianceInfo['discordInvite'],inline=True)
            embed.add_field(name='Type', value=allianceInfo['type'],inline=True)

            await inter.edit_original_message(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer='made by charis_k'
            )

            await inter.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(AllianceCommand(bot))
