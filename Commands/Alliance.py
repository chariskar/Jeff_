from Utils.Lookup import Lookup
from Utils.Embeds import Embeds
from Utils.CommandTools import CommandTools
import disnake
from disnake.ext import commands

class Alliance(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.slash_command(description="Alliance-related commands.")
    async def alliance(self,inter: disnake.ApplicationCommandInteraction):
        pass

    async def search(
        self,
        inter: disnake.ApplicationCommandInteraction,
        name: str = commands.param(name='Alliance Name')
    ):
        try: 
            await inter.response.defer()
            
            lookup = await Lookup.lookup(endpoint='Alliance',name=name)
            if not lookup:
                return
            if lookup is str:
                return await inter.edit_original_response(f'{name} isnt an existing alliance')
            area = lookup['area']
            fullName = lookup['fullName']
            nations = lookup["nations"]
            Type = lookup["type"]
            discordInvite = lookup["discordInvite"]
            leaderName = lookup["leaderName"]
            towns = lookup["towns"]
            residents = lookup["residents"]
            rank = lookup["rank"]
            embed = Embeds.embed_builder(
                author=inter, 
                title=f'Info for {name}',
            )
            embed.add_field(
                name='Full Name',
                value=fullName,
                inline=True
            )   
            if len(nations) >= 7:
                embed.add_field(
                    name='Nations',
                    value=len(nations),
                    inline=True
                )
            else:
                embed.add_field(
                    name='Nations',
                    value=f'`{nations}`',
                    inline=True
                )
                     
            embed.add_field(
                name='Rank',
                value=rank,
                inline=True
            )  
            embed.add_field(
                name='Residents',
                value=residents,
                inline=True
            )   
            embed.add_field(
                name='Leader',
                value=leaderName,
                inline=True
            )

            embed.add_field(
                name='Area',
                value=area,
                inline=True
            )
            embed.add_field(
                name='Type',
                value=Type,
                inline=True
            )
            embed.add_field(
                name='Towns',
                value=towns,
                inline=True
            )
        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                author=inter
            )
            await inter.edit_original_response(embed=embed)
            