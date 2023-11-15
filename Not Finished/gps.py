from EarthMC import GPS
from disnake.ext import commands
from Utils import *
from typing import TypedDict


class gps(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.footer = 'made by charis_k'

    async def Gps(
            self,
            inter: disnake.ApplicationCommandInteraction,
            safest: bool = commands.param(name='safest',default=True),
            x: int = commands.param(name='x'),
            z: int = commands.param(name='z')

    ):
        try:
            if safest:

                loc = str(x) + str(z)
                loc = int(loc)

                GPS.find_safest_route(loc=loc)

            elif not safest:
                pass
        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )
            await inter.edit_original_response(embed=embed)

