import datetime
import disnake
from disnake.ext import commands
import subprocess
from Utils.Lookup import Lookup
from Utils.Embeds import Embeds
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
                embed = Embeds.embed_builder(title='Restarting', author=inter, footer=self.footer)
                embed.add_field(name='reason', value=reason, inline=True)
                embed.add_field(name='Program was run at', value=self.time, inline=True)

                await inter.edit_original_response(embed=embed)

                python = sys.executable
                subprocess.run([python] + sys.argv)
            else:
                embed = Embeds.embed_builder(
                    title=f'{inter.author} you cant restart the bot you are not a dev',
                    author=inter,
                    footer=self.footer
                )
                embed.add_field(name='Program was run at', value=self.time, inline=True)
                await inter.edit_original_response(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter
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
                    title='Stopping',
                    author=inter,
                    footer=self.footer
                )
                embed.add_field(name='reason', value=reason, inline=True)

                embed.add_field(name='Program was run at', value=self.time, inline=True)
                await inter.edit_original_response(embed=embed)
                print(f'The reason to close the bot was f{reason}')
                exit(code=1)
            else:
                embed = Embeds.embed_builder(
                    title=f'{inter.author} you cant stop the bot you are not a dev',
                    author=inter,
                    footer=self.footer
                )
                embed.add_field(name='Program was run at', value=self.time, inline=True)
                await inter.edit_original_response(embed=embed)

        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter
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
                title='Pong!.',
                author=inter,
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
                author=inter
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
                    author=inter)
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
                author=inter
            )
            await inter.edit_original_response(embed=embed)

    @commands.slash_command(description='log something to the console')
    async def log(
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
                    title=f'{inter.author} Logged',
                    author=inter,
                    footer=self.footer
                )
                embed.add_field(name='reason', value=reason, inline=True)
                embed.add_field(name='Program was run at', value=self.time, inline=True)

                await inter.edit_original_response(embed=embed)

            else:
                embed = Embeds.embed_builder(
                    title=f'{inter.author} you cant log to the bots console',
                    author=inter,
                    footer=self.footer
                )
                embed.add_field(name='Program was run at', value=self.time, inline=True)
                await inter.edit_original_response(embed=embed)


        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter
            )
            await inter.edit_original_response(embed=embed)
            
    async def Command(
        self,
        inter: disnake.ApplicationCommandInteraction,
        command: str = commands.param(name='Command')
    ):
        try:
            await inter.response.defer()
            member = inter.author
            if member.id == self.owner_id:
                output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if output.stderr:
                    embed = Embeds.embed_builder(
                        author=inter,
                        title=f'Error running command {command}' 
                    )
                    embed.add_field(
                        name = 'Error',
                        value=output.stderr,
                        inline=True
                    )
                else:
                    embed = Embeds.embed_builder(
                        inter,
                        title=f'{command} was run successfuly'
                    )
                    embed.add_field(
                        name='output', 
                        value=output.stdout,
                        inline=True
                    )
        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter
            )
            await inter.edit_original_response(embed=embed)

def setup(bot):
    bot.add_cog(devcommand(bot))
