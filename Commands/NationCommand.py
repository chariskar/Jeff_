import random
import disnake
from disnake.ext import commands
from Utils.Lookup import Lookup
from Utils.Embeds import Embeds
from Utils.CommandTools import CommandTools



class NationCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.footer = 'made by charis_k'

    @commands.slash_command(description="Nation-related commands.")
    async def nation(self, inter: disnake.ApplicationCommandInteraction):
        await inter.send('The main nation commands there are commands like /nation search , /nation reslist, /nation allylist etc.')

    @nation.sub_command(description="Retrieve and display general information about a nation.")
    async def search(
            self,
            inter: disnake.ApplicationCommandInteraction,
            nation: str = commands.param(name='nation', default='Jefferson')
    ):
        await inter.response.defer()

        server = 'aurora'
        """Retrieve and display general information about a nation."""


        try:
            if nation.lower() == "random":
                allNationsLookup = await Lookup.lookup(server, endpoint="nations")
                nation = random.choice(allNationsLookup["allNations"])

            nationsLookup = await Lookup.lookup(server, endpoint="nations", name=nation)
            locationUrl = f"https://earthmc.net/map/{server}/?zoom=4&x={nationsLookup['spawn']['x']}&z={nationsLookup['spawn']['z']}"



            embed = Embeds.embed_builder(
                title=f"`{nationsLookup['strings']['nation']}`",
                description=nationsLookup["strings"]["board"],
                footer=self.footer,
                author=inter.author
            )

            embed.add_field(name="King", value=nationsLookup["strings"]["king"], inline=True)
            embed.add_field(name="Capital", value=nationsLookup["strings"]["capital"], inline=True)
            embed.add_field(
                name="Location",
                value=f"[{int(round(nationsLookup['spawn']['x'], 0))}, {int(round(nationsLookup['spawn']['z'], 0))}]({locationUrl})",
                inline=True
            )

            embed.add_field(
                name='Nation Bonus',
                value=int(CommandTools.claim_bonus(nationsLookup['stats']['numResidents'])),
                inline=True
            )

            embed.add_field(name="Residents", value=nationsLookup["stats"]["numResidents"], inline=True)
            embed.add_field(name="Towns", value=nationsLookup["stats"]["numTowns"], inline=True)
            embed.add_field(
                name="Town Blocks",
                value=f"{nationsLookup['stats']['numTownBlocks']} ({nationsLookup['stats']['numTownBlocks'] * 16 + (48 * nationsLookup['stats']['numTowns'])}G)",
                inline=True
            )

            embed.add_field(name="Balance", value=f"{nationsLookup['stats']['balance']}G", inline=True)
            embed.add_field(
                name="Founded",
                value=f"<t:{round(nationsLookup['timestamps']['registered'] / 1000)}:R>",
                inline=True
            )
            embed.add_field(
                name="Status",
                value=f"• `Open` — {nationsLookup['status']['isOpen']}\n• `Public` — {nationsLookup['status']['isPublic']}\n• `Neutral` — {nationsLookup['status']['isNeutral']}",
                inline=True
            )

            await inter.edit_original_response(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )

            await inter.edit_original_response(embed=embed)

    @nation.sub_command(description="View all the residents of a specified nation.")
    async def reslist(
            self,
            inter: disnake.ApplicationCommandInteraction,
            nation: str = commands.param(name='nation', default='Jefferson')
    ):
        await inter.response.defer()

        server: str = "aurora"

        """Retrieve and display the list of residents in a nation."""


        try:
            nationsLookup = await Lookup.lookup(server, endpoint="nations", name=nation)

            embed = Embeds.embed_builder(
                title=f"`{nationsLookup['strings']['nation']}'s Residents`",
                footer=self.footer,
                author=inter.author
            )

            residentsString = CommandTools.list_to_string(nationsLookup["residents"])

            embed.add_field(name="Residents", value=f"```{residentsString[:1018]}```", inline=True)

            await inter.edit_original_response(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer,

            )

            await inter.edit_original_response(embed=embed)

    @nation.sub_command(description="Retrieve and display the list of ranked residents in a nation.")
    async def ranklist(
            self,
            inter: disnake.ApplicationCommandInteraction,
            nation: str = commands.param(name='nation', default='Jefferson')
    ):
        await inter.response.defer()

        server: str = "aurora"

        """Retrieve and display the list of ranked residents in a nation."""


        try:
            nationsLookup = await Lookup.lookup(server, endpoint="nations", name=nation)

            embed = Embeds.embed_builder(
                title=f"`{nationsLookup['strings']['nation']}'s Ranked Residents`",
                footer=self.footer,
                author=inter.author
            )

            for rank in nationsLookup["ranks"]:
                if len(nationsLookup["ranks"][rank]) != 0:
                    rankString = CommandTools.list_to_string(nationsLookup["ranks"][rank])

                    embed.add_field(name=rank.capitalize(), value=f"`{rankString[:1022]}`", inline=True)

                else:
                    embed.add_field(name=rank.capitalize(), value="N/A", inline=True)

            await inter.edit_original_response(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )

            await inter.edit_original_response(embed=embed)


    @nation.sub_command(description="Retrieve and display the list of allies of a nation.")
    async def allylist(
            self,
            inter: disnake.ApplicationCommandInteraction,
            nation: str = commands.param(name='nation', default='Jefferson')
    ):
        await inter.response.defer()

        server: str = "aurora"

        """Retrieve and display the list of allies of a nation."""


        try:
            nationsLookup = await Lookup.lookup(server, endpoint="nations", name=nation)

            embed = Embeds.embed_builder(
                title=f"`{nationsLookup['strings']['nation']}'s Allies`",
                footer=self.footer,
                author=inter.author
            )

            if len(nationsLookup["allies"]) != 0:
                alliesString = CommandTools.list_to_string(nationsLookup["allies"])

                embed.add_field(name="Allies", value=f"```{alliesString[:1018]}```", inline=True)

            else:
                embed.add_field(
                    name="Allies",
                    value=f"{nationsLookup['strings']['nation']} has no allies :(",
                    inline=True
                )

            await inter.edit_original_response(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )

            await inter.edit_original_response(embed=embed)

    @nation.sub_command(description="Retrieve and display the list of enemies of a nation.")
    async def enemylist(
            self,
            inter: disnake.ApplicationCommandInteraction,
            nation: str = commands.param(name='nation', default='Jefferson')
    ):
        await inter.response.defer()

        server: str = "aurora"

        """Retrieve and display the list of enemies of a nation."""


        try:
            nationsLookup = await Lookup.lookup(server, endpoint="nations", name=nation)

            embed = Embeds.embed_builder(
                title=f"`{nationsLookup['strings']['nation']}'s Enemies`",
                footer=self.footer,
                author=inter.author
            )

            if len(nationsLookup["enemies"]) != 0:
                enemiesString = CommandTools.list_to_string(nationsLookup["enemies"])

                embed.add_field(name="Enemies", value=f"```{enemiesString[:1018]}```", inline=True)

            else:
                embed.add_field(
                    name="Enemies",
                    value=f"{nationsLookup['strings']['nation']} has no enemies :)",
                    inline=True
                )

            await inter.edit_original_response(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )

            await inter.edit_original_response(embed=embed)

    @nation.sub_command(description="Retrieve and display the list of towns in a nation.")
    async def townlist(
            self,
            inter: disnake.ApplicationCommandInteraction,
            nation: str = commands.param(name='nation', default='Jefferson')
    ):
        await inter.response.defer()

        server: str = "aurora"

        """Retrieve and display the list of towns in a nation."""


        try:
            nationsLookup = await Lookup.lookup(server, endpoint="nations", name=nation)

            embed = Embeds.embed_builder(
                title=f"`{nationsLookup['strings']['nation']}'s Towns`",
                footer=self.footer,
                author=inter.author
            )

            townsString = CommandTools.list_to_string(nationsLookup["towns"])

            embed.add_field(name="Towns", value=f"```{townsString[:1018]}```", inline=True)

            await inter.edit_original_response(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )

            await inter.edit_original_response(embed=embed)

    @nation.sub_command(description="Retrieve and display the list of nations that the specified nation hasn't allied yet.")
    async def unallied(
            self,
            inter: disnake.ApplicationCommandInteraction,
            nation: str = commands.param(name='nation', default='Jefferson')
    ):
        await inter.response.defer()

        server: str = "aurora"

        """Retrieve and display the list of nations that the specified nation hasn't allied yet."""


        try:
            nationsLookup = await Lookup.lookup(server, endpoint="nations", name=nation)
            allNationsLookup = await Lookup.lookup(server, endpoint="nations")

            embed = Embeds.embed_builder(
                title=f"`{nationsLookup['strings']['nation']}'s Unallied Nations`",
                footer=self.footer,
                author=inter.author,
            )

            allyList = nationsLookup["allies"]
            allNations = allNationsLookup["allNations"]
            allNations.remove(nationsLookup["strings"]["nation"])

            unalliedList = list(set(allNations).difference(set(allyList)))
            if len(unalliedList) != 0:
                # Split unalliedList into multiple fields if needed
                for i in range(0, len(unalliedList), 15):  # Display 15 unallied nations per field
                    unalliedString = " ".join(unalliedList[i:i + 15])
                    embed.add_field(name=f"Unallied (Continued)" if i > 0 else "Unallied",
                                    value=f"```{unalliedString}```", inline=True)

            else:
                embed.add_field(
                    name="Unallied",
                    value=f"{nationsLookup['strings']['nation']} has allied everyone :)",
                    inline=True
                )

            await inter.edit_original_response(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',

                footer=self.footer
            )

            await inter.edit_original_response(embed=embed)


def setup(bot):
    bot.add_cog(NationCommand(bot))
