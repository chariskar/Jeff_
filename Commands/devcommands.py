import datetime
import disnake
from disnake.ext import commands
import subprocess
from Utils.Lookup import Lookup
from Utils.Embeds import Embeds
from Utils.Bot_News import NewsCog
from Utils.CommandTools import CommandTools
import sys
import pytz


class devcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.footer = 'made by charis_k'
        self.timezone = pytz.timezone('Europe/Athens')
        self.time = datetime.datetime.now(self.timezone)
        self.owner_id = 927581845787402240
        self.channel_id = 1158381660107198614
        self.guild_id = 1131117400985706538

    @commands.slash_command(description='Restart the bot')
    async def restart(self,
                      inter: disnake.ApplicationCommandInteraction,
                      reason: str = commands.param(name='reason'),

                      ):
        try:
            await inter.response.defer()
            member = inter.author
            if member.id == self.owner_id:
                embed = Embeds.embed_builder('Restarting', author=inter.author, footer=self.footer)
                embed.add_field(name='reason', value=reason, inline=True)
                embed.add_field(name='Program was run at', value=self.time, inline=True)

                await inter.edit_original_response(embed=embed)

                python = sys.executable
                subprocess.run([python] + sys.argv)
            else:
                embed = Embeds.embed_builder(
                    f'{inter.author} you cant restart the bot you are not a dev',
                    author=inter.author,
                    footer=self.footer
                )
                embed.add_field(name='Program was run at', value=self.time, inline=True)
                await inter.edit_original_response(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter.author
            )
            await inter.edit_original_response(embed=embed)



    @commands.slash_command(description='Stop the bot')
    async def stop(
            self,
            inter: disnake.ApplicationCommandInteraction,
            reason: str = commands.param(name='reason')):
        try:
            await inter.response.defer()

            member = inter.author

            if member.id == self.owner_id:
                embed = Embeds.embed_builder(
                    'Stopping',
                    author=inter.author,
                    footer=self.footer
                )
                embed.add_field(name='reason', value=reason, inline=True)

                embed.add_field(name='Program was run at', value=self.time, inline=True)
                await inter.edit_original_response(embed=embed)
                print(f'The reason to close the bot was f{reason}')
                exit(code=1)
            else:
                embed = Embeds.embed_builder(
                    f'{inter.author} you cant stop the bot you are not a dev',
                    author=inter.author,
                    footer=self.footer
                )
                embed.add_field(name='Program was run at', value=self.time, inline=True)
                await inter.edit_original_response(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter.author
            )
            await inter.edit_original_response(embed=embed)

    @commands.slash_command(description='The bots ping')
    async def ping(
            self,
            inter: disnake.ApplicationCommandInteraction):
        try:
            await inter.response.defer()

            bot_latency = self.bot.latency * 1000
            api_latency = await CommandTools.get_discord_api_latency()
            embed = Embeds.embed_builder(
                'Pong!.',
                author=inter.author,
                footer=self.footer
            )
            embed.add_field(name='Bot latency is', value=f'{bot_latency:.2f} ms', inline=True)
            embed.add_field(name='Discord API latency is', value=f'{api_latency:.2f} ms', inline=True)
            embed.add_field(name=f'Program was run at', value=self.time, inline=True)

            await inter.edit_original_response(embed=embed)
        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter.author
            )
            await inter.edit_original_response(embed=embed)

    @commands.slash_command(description='clear the cache of the bot')
    async def cache_clear(
            self,
            inter: disnake.ApplicationCommandInteraction,
            reason: str = commands.param(name='reason', default=None)
    ):
        try:
            await inter.response.defer()

            member = inter.author
            if member.id == self.owner_id:
                embed = Embeds.embed_builder(
                    title='Clearing cache',
                    footer=self.footer,
                    author=inter.author)
                Lookup.clear_cache()

                print(f'Cache cleared {reason}')
                embed.add_field(name='reason', value=reason, inline=True)

                embed.add_field(name='Program was run at', value=self.time, inline=True)

                await inter.edit_original_response(embed=embed)
            else:
                await inter.send(f"{member.display_name}, you do not have the required role.")

        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter.author
            )
            await inter.edit_original_response(embed=embed)

    @commands.slash_command(description='log something to the console')
    async def long_to_console(
            self,
            inter: disnake.ApplicationCommandInteraction,
            reason: str = commands.param(name='reason', default=None)
    ):
        try:
            await inter.response.defer()

            member = inter.author
            if member.id == self.owner_id:
                print(f'Logged f{reason}')
                embed = Embeds.embed_builder(
                    f'{inter.author} Logged',
                    author=inter.author,
                    footer=self.footer
                )
                embed.add_field(name='reason', value=reason, inline=True)
                embed.add_field(name='Program was run at', value=self.time, inline=True)

                await inter.edit_original_response(embed=embed)

            else:
                embed = Embeds.embed_builder(
                    f'{inter.author} you cant log to the bots console',
                    author=inter.author,
                    footer=self.footer
                )
                embed.add_field(name='Program was run at', value=self.time, inline=True)
                await inter.edit_original_response(embed=embed)


        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter.author
            )
            await inter.edit_original_response(embed=embed)

    @commands.slash_command(description='see the latest news')
    async def send_last_message(self, inter: disnake.ApplicationCommandInteraction):
        try:
            await inter.response.defer()
            guild: disnake.Guild = self.bot.get_guild(self.guild_id)
            channel: disnake.TextChannel = guild.get_channel(self.channel_id)

            last_message = await NewsCog.on_message(channel.last_message)
            await inter.edit_original_response(
                f'{last_message}'
            )

        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter.author
            )
            await inter.edit_original_response(embed=embed)

def setup(bot):
    bot.add_cog(devcommand(bot))
