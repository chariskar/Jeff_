import disnake
from disnake.ext import commands
from Utils.Embeds import Embeds
from Utils.Lookup import Lookup
from Utils.CommandTools import CommandTools


class AllianceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Alliance-related commands.")
    async def alliance(self, inter: disnake.ApplicationCommandInteraction):
        pass


    @alliance.sub_command(description="Retrieve and display general information about an alliance.")
    async def info(self, inter: disnake.ApplicationCommandInteraction, alliance: str):
        """Retrieve and display general information about an alliance."""
        commandString = f"/alliance info {alliance}"

        try:
            allianceInfo = await Lookup.lookup(endpoint='alliance',name=alliance,server='aurora')


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
