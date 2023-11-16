import random
import disnake
from disnake.ext import commands
from Utils.Embeds import Embeds
from Utils.Lookup import Lookup
from Utils.CommandTools import CommandTools



class ResCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.footer = 'made by charis_k'

    @commands.slash_command()
    async def res(
        self,
        inter: disnake.ApplicationCommandInteraction,

    ):
        await inter.send('This is the main /resident command there are commands lke /res search , /res friendlist etc')

    @res.sub_command(description="Provides general info about a resident")
    async def search(
        self,
        inter: disnake.ApplicationCommandInteraction,
        username: str = commands.Param(description="Resident's username, type 'random' for a random choice"),
    ):
        server: str = "aurora"

        try:
            if username.lower() == "random":
                allResidentsLookup = Lookup.lookup(server, endpoint="residents")
                username = random.choice(allResidentsLookup["allResidents"])

            residentsLookup = await Lookup.lookup(server, endpoint="residents", name=username)
        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',

                footer=self.footer,
            )
            await inter.send(embed=embed, ephemeral=True)
            return

        try:
            fullNameList = [residentsLookup["strings"]["title"], residentsLookup["strings"]["username"], residentsLookup["strings"]["surname"]]
            fullNameList = [x for x in fullNameList if x != ""]
            fullName = " ".join(fullNameList)

            if residentsLookup["timestamps"]["lastOnline"] != 0:
                lastOnline = f"<t:{round(residentsLookup['timestamps']['lastOnline'] / 1000)}:R>"
            else:
                lastOnline = "NPC"

            town = residentsLookup["affiliation"].get("town")
            joinedTownAt = f"<t:{round(residentsLookup['timestamps']['joinedTownAt'] / 1000)}:R>" if town else "N/A"
            nation = residentsLookup["affiliation"].get("nation")


            embed = Embeds.embed_builder(
                title=f"`{fullName}`",
                author=inter.author,
                footer=self.footer,
                thumbnail=f"https://mc-heads.net/head/{residentsLookup['strings']['username']}",
            )

            embed.add_field(name="Affiliation", value=f"• `Town` — {town}\n• `Nation` — {nation}", inline=True)
            embed.add_field(name="Online", value=residentsLookup["status"]["isOnline"], inline=True)
            embed.add_field(name="Balance", value=f"{residentsLookup['stats']['balance']}G", inline=True)

            embed.add_field(name="Registered", value=f"<t:{round(residentsLookup['timestamps']['registered'] / 1000)}:R>", inline=True)
            embed.add_field(name="Last Online", value=lastOnline, inline=True)
            embed.add_field(name="Joined Town", value=joinedTownAt, inline=True)


            for rankType in residentsLookup["ranks"]:
                if len(residentsLookup["ranks"][rankType]) != 0:
                    rankString = CommandTools.list_to_string(residentsLookup["ranks"][rankType])
                    name = "Town Ranks" if rankType == "townRanks" else "Nation Ranks"
                    embed.add_field(name=name, value=rankString.title(), inline=False)

            await inter.send(embed=embed, ephemeral=False)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )
            await inter.send(embed=embed, ephemeral=True)


    @res.sub_command(description="View all the friends of a specified resident")
    async def friendlist(
        self,
        inter: disnake.ApplicationCommandInteraction,
        username: str = commands.Param(description="Resident's username"),
    ):
        server: str = "aurora"
        try:
            residentsLookup = await Lookup.lookup(server.lower(), endpoint="residents", name=username)
        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                type="userError",
                footer=self.footer,
            )
            await inter.send(embed=embed, ephemeral=True)
            return

        try:
            embed = Embeds.embed_builder(
                title=f"`{residentsLookup['strings']['username']}'s Friends",
                footer=self.footer,
                author=inter.author,
            )

            if residentsLookup["friends"]:
                friendsString = CommandTools.list_to_string(residentsLookup["friends"])
                embed.add_field(name="Friends", value=f"```{friendsString[:1018]}```", inline=True)
            else:
                embed.add_field(name="Friends", value=f"{residentsLookup['strings']['username']} has no friends :(", inline=True)

            await inter.send(embed=embed, ephemeral=False)

        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )
            await inter.send(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(ResCommand(bot))
