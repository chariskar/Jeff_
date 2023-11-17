import disnake
from disnake.ext import commands
from Utils.Embeds import Embeds


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.footer = 'made by charis_k'


    @commands.slash_command(description='stars are appreciated <3')
    async def github(self, inter: disnake.ApplicationCommandInteraction):
        try:
            await inter.response.defer()
            await inter.edit_original_response('https://github.com/chariskar/Jeff_/tree/python')

        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer
            )
            await inter.response.send_message(embed=embed)


    @commands.slash_command(description='Help command')
    async def help(self, inter: disnake.ApplicationCommandInteraction):
        try:
            embed = Embeds.embed_builder(
                title='Commands',
                footer=self.footer,
                author=inter.author
            )
            embed.add_field(
                name='Nation',
                value='see /nation for more info'
            )
            embed.add_field(
                name='Resident',
                value='see /res for more info'
            )
            embed.add_field(
                name='Town',
                value='see /town for more info'
            )
            embed.add_field(
                name='Server',
                value='only one command for now'
            )
            embed.add_field(
                name='Devcommands /ping',
                value='see the bots ping the only available to everyone dev command'

            )
            embed.add_field(
                name='Weather',
                value='only one command for now'
            )
            await inter.response.send_message(embed=embed)
        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer
            )
            await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
