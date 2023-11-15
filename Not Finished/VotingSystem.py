import disnake
from disnake.ext import commands
import random
from Utils.Embeds import Embeds
from disnake import reaction


class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.footer = 'made by charis_k'


    @commands.slash_command()
    async def poll(self,
         inter: disnake.ApplicationCommandInteraction,
         question: str = commands.param(name='Question'),
         options: str = commands.param(name='Options')):
        try:
            await inter.response.defer()
            embed = Embeds.embed_builder(
                title=question,
                footer=self.footer,
                author=inter.author
            )

            options = options.split(',')
            if len(options) == 1 or len(options) == 0:
                # check if options is one or empty
                await inter.send('Error not enough options',ephemeral=True)
            else:
                if len(options) >5:
                    await inter.send('Too many options', ephemeral=True)
                else:
                    embed.add_field(name=options)
                    await inter.edit_original_response(embed)


        except Exception as e:
            embed = Embeds.error_embed(
                value=f'Error is {e}',
                footer=self.footer
            )

            await inter.send(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Vote(bot))
