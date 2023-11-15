import random
import disnake
from disnake.ext import commands
from Utils.Embeds import Embeds
from Utils.Lookup import Lookup
from Utils.CommandTools import CommandTools


class TownCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.footer = 'made by charis_k'
    choices = ['/t join fort elko', '/t join Redwood_City', '/t join Lost_Coast']



    @commands.slash_command()
    async def town(self, inter: disnake.ApplicationCommandInteraction):
        pass



    @town.sub_command(description="Provides general info about a town")
    async def search(
        self,
        inter: disnake.ApplicationCommandInteraction,
        town: str = commands.Param(description="Town's name", default='')

    ):
        server: str = "aurora"
        try:
            if not town:
                num = random.randint(1, 3)
                try:
                    if num == 1:
                        townsLookup = await Lookup.lookup(server, endpoint="towns", name='Fort_Elko')
                    elif num == 2:
                        townsLookup = await Lookup.lookup(server, endpoint="towns", name='Lost_Coast')
                    elif num == 3:
                        townsLookup = await Lookup.lookup(server, endpoint="towns", name='Redwood_City')

                except Exception as e:
                    embed = Embeds.error_embed(
                        value=f'Error is {e}',
                        footer=self.footer
                    )
                    await inter.send(embed=embed)
                    return
            else:
                try:
                    townsLookup = await Lookup.lookup(server, endpoint="towns", name=town)
                except Exception as e:
                    embed = Embeds.error_embed(
                        value=f'Error is {e}',
                        footer=self.footer
                    )
                    await inter.send(embed=embed)
                    return
        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )
            await inter.send(embed=embed)
            return


        try:
            try:
                locationUrl = f"https://earthmc.net/map/{server}/?zoom=4&x={townsLookup['spawn']['x']}&z={townsLookup['spawn']['z']}"
                location = f"[{int(round(townsLookup['spawn']['x'], 0))}, {int(round(townsLookup['spawn']['z'], 0))}]({locationUrl})"
            except:
                locationUrl = f"https://earthmc.net/map/{server}/?zoom=4&x={townsLookup['home']['x'] * 16}&z={townsLookup['home']['z'] * 16}"
                location = f"[{townsLookup['home']['x'] * 16}, {townsLookup['home']['z'] * 16}]({locationUrl})"

            try:
                nation = townsLookup["affiliation"]["nation"]
                joinedNationAt = f"<t:{round(townsLookup['timestamps']['joinedNationAt'] / 1000)}:R>"
            except:
                nation = None
                joinedNationAt = "N/A"

            rnaoPermsList = CommandTools.rnao_perms(json=townsLookup)

            embed = Embeds.embed_builder(
                title=f"`{townsLookup['strings']['town']}`",
                description=townsLookup["strings"]["board"],
                footer=self.footer,
                author=inter.author
            )

            embed.add_field(name="Mayor", value=townsLookup["strings"]["mayor"], inline=True)
            embed.add_field(name="Nation", value=nation, inline=True)
            embed.add_field(name="Location", value=location, inline=True)

            embed.add_field(name="Residents", value=townsLookup["stats"]["numResidents"], inline=True)
            embed.add_field(
                name="Town Blocks",
                value=f"{townsLookup['stats']['numTownBlocks']}/{townsLookup['stats']['maxTownBlocks']} ({townsLookup['stats']['numTownBlocks'] * 16 + 48}G)",
                inline=True
            )

            # fetch the nation the town is in
            Nation = await Lookup.lookup(endpoint='nation', name=nation)
            embed.add_field(
                name=f'Nation bonus for {nation}',
                value=CommandTools.claim_bonus(int(Nation['stats']['numResidents']))
            )

            embed.add_field(name="Balance", value=f"{townsLookup['stats']['balance']}G", inline=True)

            embed.add_field(name="Founder", value=townsLookup["strings"]["founder"], inline=True)
            embed.add_field(
                name="Founded",
                value=f"<t:{round(townsLookup['timestamps']['registered'] / 1000)}:R>",
                inline=True
            )
            embed.add_field(name="Joined Nation", value=joinedNationAt, inline=True)

            embed.add_field(
                name="Perms",
                value=f"• `Build` — {rnaoPermsList[0]}\n• `Destroy` — {rnaoPermsList[1]}\n• `Switch` — {rnaoPermsList[2]}\n• `ItemUse` — {rnaoPermsList[3]}",
                inline=True
            )
            embed.add_field(
                name="Flags",
                value=f"• `PvP` — {townsLookup['perms']['flagPerms']['pvp']}\n• `Explosions` — {townsLookup['perms']['flagPerms']['explosion']}\n• `Firespread` — {townsLookup['perms']['flagPerms']['fire']}\n• `Mob Spawns` — {townsLookup['perms']['flagPerms']['mobs']}",
                inline=True
            )
            embed.add_field(
                name="Status",
                value=f"• `Capital` — {townsLookup['status']['isCapital']}\n• `Open` — {townsLookup['status']['isOpen']}\n• `Public` — {townsLookup['status']['isPublic']}\n• `Neutral` — {townsLookup['status']['isNeutral']}\n• `Overclaimed` — {townsLookup['status']['isOverClaimed']}\n• `Ruined` — {townsLookup['status']['isRuined']}",
                inline=True
            )

            await inter.send(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )
            await inter.send(embed=embed)

    @town.sub_command(description="View all the residents of a specified town")
    async def reslist(
        self,
        inter: disnake.ApplicationCommandInteraction,
        town: str = commands.Param(description="Town's name", default=random.choice(choices)),

    ):
        server: str = "aurora"

        commandString = f"/town reslist town: {town} server: {server}"
        try:
            townsLookup = await Lookup.lookup(server, endpoint="towns", name=town)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                type="userError",
                footer=commandString
            )
            await inter.response.send_message(embed=embed, ephemeral=True)
            return

        try:
            embed = Embeds.embed_builder(
                title=f"`{townsLookup['strings']['town']}'s Residents",
                footer=self.footer,
                author=inter.author
            )

            residentsString = CommandTools.list_to_string(townsLookup["residents"])

            embed.add_field(name="Residents", value=f"```{residentsString[:1018]}```", inline=True)

            await inter.response.send_message(embed=embed, ephemeral=False)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )
            await inter.response.send_message(embed=embed, ephemeral=True)

    @town.sub_command(description="View all the ranked residents of a specified town")
    async def ranklist(
        self,
        inter: disnake.ApplicationCommandInteraction,
        town: str = commands.Param(description="Town's name", default=random.choice(choices)),
    ):
        server: str = "aurora"

        commandString = f"/town ranklist town: {town} server: {server}"
        try:
            townsLookup = await Lookup.lookup(server, endpoint="towns", name=town)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                type="userError",
                footer=commandString
            )
            await inter.response.send_message(embed=embed, ephemeral=True)
            return

        try:
            embed = Embeds.embed_builder(
                title=f"`{townsLookup['strings']['town']}'s Ranked Residents",
                footer=commandString,
                author=inter.author
            )

            for rank in townsLookup["ranks"]:
                if len(townsLookup["ranks"][rank]) != 0:
                    rankString = CommandTools.list_to_string(townsLookup["ranks"][rank])

                    embed.add_field(name=rank.capitalize(), value=f"`{rankString[:1022]}`", inline=True)

                else:
                    embed.add_field(name=rank.capitalize(), value="N/A", inline=True)

            if len(townsLookup["trusted"]) != 0:
                trustedString = CommandTools.list_to_string(townsLookup["trusted"])

                embed.add_field(name="Trusted", value=f"`{trustedString[:1022]}`", inline=True)

            else:
                embed.add_field(name="Trusted", value="N/A", inline=True)

            await inter.response.send_message(embed=embed, ephemeral=False)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )
            await inter.response.send_message(embed=embed, ephemeral=True)

    @town.sub_command(description="View all the outlaws of a specified town")
    async def outlawlist(
        self,
        inter: disnake.ApplicationCommandInteraction,
        town: str = commands.Param(description="Town's name"),

    ):
        server: str = "aurora"

        try:
            if not town:
                num = random.randint(1, 3)
                try:
                    if num == 1:
                        townsLookup = await Lookup.lookup(server, endpoint="towns", name='Fort_Elko')
                    elif num == 2:
                        townsLookup = await Lookup.lookup(server, endpoint="towns", name='Lost_Coast')
                    elif num == 3:
                        townsLookup = await Lookup.lookup(server, endpoint="towns", name='Redwood_City')

                except Exception as e:
                    embed = Embeds.error_embed(
                        value=f'Error is {e}',
                        footer=self.footer
                    )
                    await inter.send(embed=embed)
                    return
            else:
                try:
                    townsLookup = await Lookup.lookup(server, endpoint="towns", name=town)
                except Exception as e:
                    embed = Embeds.error_embed(
                        value=f'Error is {e}',
                        footer=self.footer
                    )
                    await inter.send(embed=embed)
                    return
        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )
            await inter.send(embed=embed)
            return


        try:
            embed = Embeds.embed_builder(
                title=f"`{townsLookup['strings']['town']}'s Outlaws",
                footer=self.footer,
                author=inter.author
            )

            if len(townsLookup["outlaws"]) != 0:
                outlawsString = CommandTools.list_to_string(townsLookup["outlaws"])

                embed.add_field(name="Outlaws", value=f"```{outlawsString[:1018]}```", inline=True)

            else:
                embed.add_field(name="Outlaws", value=f"{townsLookup['strings']['town']} has no outlaws :)", inline=True)

            await inter.response.send_message(embed=embed, ephemeral=False)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )
            await inter.response.send_message(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(TownCommand(bot))
