import disnake
from disnake.ext import commands
from Utils.Embeds import Embeds
from Utils.Lookup import Lookup
from Utils.CommandTools import CommandTools


class ServerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.footer = 'made by charis_k'


    @commands.slash_command(description="Provides info about a server")
    async def server(
        self,
        inter: disnake.ApplicationCommandInteraction,
        server: str = commands.Param(
            description="Server name, defaults to Aurora",
            default="aurora",
            choices=["aurora"]
        )
    ):
        try:
            serverLookup = await Lookup.lookup(server)
            allResidentsLookup = await Lookup.lookup(server, endpoint="residents",version=1)
            allTownsLookup = await Lookup.lookup(server, endpoint="towns",version=1)
            allNationsLookup = await Lookup.lookup(server, endpoint="nations",version=1)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )

            await inter.send(embed=embed, ephemeral=True)
            return

        try:
            weather = CommandTools.get_weather(serverLookup)

            embed = Embeds.embed_builder(
                title=f"`{server.capitalize()}`",
                footer=self.footer,
                author=inter.author
            )

            embed.add_field(
                name="Online Players",
                value=f"{serverLookup['players']['numOnlinePlayers']}/{serverLookup['players']['maxPlayers']}",
                inline=False
            )

            embed.add_field(name="Weather", value=weather, inline=True)
            embed.add_field(name="Time", value=f"{serverLookup['world']['time']}/24000", inline=True)
            embed.add_field(
                name="Day",
                value=int(round(serverLookup["world"]["fullTime"] / 24000, 0)),
                inline=True
            )

            embed.add_field(
                name="Stats",
                value=f"• `Residents` — {allResidentsLookup['numResidents']}\n• `Towns` — {allTownsLookup['numTowns']}\n• `Nations` — {allNationsLookup['numNations']}",
                inline=False
            )

            await inter.send(embed=embed, ephemeral=False)

        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter.author
            )
            await inter.edit_original_response(embed=embed)


def setup(bot):
    bot.add_cog(ServerCommand(bot))
