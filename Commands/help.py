import disnake
from disnake.ext import commands
from Utils.Embeds import Embeds


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.footer = 'made by charis_k'
        self.command_dict: dict = {
            'nation':
                [
                    'search',
                    'allylist',
                    'reslist',
                    'ranklist',
                    'townlist',
                    'unallied'],
            'town':
                ['search',
                 'outlawlist',
                 'reslist',
                 'ranklist'],
            'devcommands':
                ['restart',
                 'stop',
                 'ping',
                 'log_to_console',
                 'clear_cache'],
            'res':
                ['search',
                 'friendlist'],
            'general':
                ['weather',
                 'server']
        }

    @commands.slash_command(description='stars are appreciated <3')
    async def github(self, inter: disnake.ApplicationCommandInteraction):
        try:
            await inter.response.defer()
            await inter.edit_original_response(
                'https://github.com/chariskar/Jeff_/tree/python stars are appreciated <3')

        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter
            )
            await inter.response.send_message(embed=embed)

    @commands.slash_command(description='Help command')
    async def help(self, inter: disnake.ApplicationCommandInteraction):
        try:
            await inter.response.defer()
            embed = Embeds.embed_builder(
                title='Commands',
                footer=self.footer,
                author=inter
            )
            embed.add_field(
                name='Nation',
                value='see /nation for more info',
                inline=True

            )
            embed.add_field(
                name='Resident',
                value='see /res for more info',
                inline=True

            )
            embed.add_field(
                name='Town',
                value='see /town for more info',
                inline=True

            )
            embed.add_field(
                name='Server',
                value='only one command for now',
                inline=True
            )
            embed.add_field(
                name='Weather',
                value='only one command for now',
                inline=True
            )
            await inter.edit_original_response(embed=embed)
        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter
            )
            await inter.edit_original_response(embed=embed)

    @commands.slash_command(description='Help for a specific command and subcommand')
    async def help_specific(
            self,
            inter: disnake.ApplicationCommandInteraction,
            command: str = commands.param(name='command'),
            subcommand: str = commands.param(name='subcommand',default='')
    ):
        try:
            await inter.response.defer()
            command_dict: dict = self.command_dict
            if command in command_dict and subcommand in command_dict[command]:
                embed = Embeds.embed_builder(
                    title=f'Help for {inter.author.global_name}',
                    author=inter,
                    footer=self.footer
                )
                if command == 'nation':
                    if subcommand == command_dict[command][0]:
                        embed.add_field(
                            name='The nation search command',
                            value='Used to search general info for a nation as with all nation commands default is Jefferson',
                            inline=True
                        )
                    elif subcommand == command_dict[command][1]:
                        embed.add_field(
                            name='The nation allylist command',
                            value='Used to get the allies of a nation as with all nation commands default is Jefferson',
                            inline=True
                        )
                    elif subcommand == command_dict[command][2]:
                        embed.add_field(
                            name='The nation reslist command',
                            value='Used to get the residents of a nation as with all nation commands default is Jefferson',
                            inline=True
                        )
                    elif subcommand == command_dict[command][3]:
                        embed.add_field(
                            name='The nation ranklist command',
                            value='Used to get the ranked residents of a nation as with all nation commands default is Jefferson',
                            inline=True
                        )
                    elif subcommand == command_dict[command][4]:
                        embed.add_field(
                            name='The nation townlist command',
                            value='Used to get the towns of a nation as with all nation commands default is Jefferson',
                            inline=True
                        )
                    elif subcommand == command_dict[command][5]:
                        embed.add_field(
                            name='The nation unallied command',
                            value='Used to get the unallied nations a nation has as with all nation commands default is Jefferson',
                            inline=True
                        )
                elif command == 'town':
                    if subcommand == command_dict[command][0]:
                        embed.add_field(
                            name='The town search command',
                            value='Used to get info about a town as with all town commands it is a pick of 3 towns',
                            inline=True
                        )
                    elif subcommand == command_dict[command][1]:
                        embed.add_field(
                            name='The town outlawlist command',
                            value='Used to get the outlawed users of a town as with all town commands it is a pick of 3 towns',
                            inline=True
                        )
                    elif subcommand == command_dict[command][2]:
                        embed.add_field(
                            name='The reslist command',
                            value='As with the nation reslist command it gets the residents of a town as with all town commands it is a pick of 3 towns',
                            inline=True
                        )
                    elif subcommand == command_dict[command][3]:
                        embed.add_field(
                            name='The ranklist command',
                            value='As with the nation ranklist command it gets the ranked residents of a town as with all town commands it is a pick of 3 towns',
                            inline=True
                        )
                elif command == 'devcommands':
                    if subcommand == command_dict[command][0]:
                        embed.add_field(
                            name='The restart command',
                            value='Restart the bot available to devs only',
                            inline=True
                        )
                    elif subcommand == command_dict[command][1]:
                        embed.add_field(
                            name='The stop command',
                            value='Stop the bot available to devs only',
                            inline=True
                        )
                    elif subcommand == command_dict[command][3]:
                        embed.add_field(
                            name='The log_to_console command',
                            value='Log to the bots console available to devs only',
                            inline=True
                        )
                    elif subcommand == command_dict[command][4]:
                        embed.add_field(
                            name='The clear_cache command',
                            value='Clear the bots cache available to devs only',
                            inline=True
                        )
                    elif subcommand == command_dict[command][2]:
                        embed.add_field(
                            name='The ping command',
                            value='Get the bots ping available to everyone',
                            inline=True
                        )
                elif command == 'weather' or command == 'server':
                    if command == 'weather':
                        embed.add_field(
                            name='The weather command',
                            value='Not an emc command just a real world weather command',
                            inline=True
                        )
                    elif command == 'server':
                        embed.add_field(
                            name='The server command',
                            value='An emc related command just didnt know where to put it so it ended up here',
                            inline=True
                        )
                await inter.edit_original_response(embed=embed)
            elif command and subcommand == 'None' or not subcommand:
                embed = Embeds.embed_builder(
                    title=f'Help for {inter.author.global_name}',
                    author=inter,
                    footer=self.footer
                )
                if command == 'nation':
                    embed.add_field(
                        name=f'The {command} command',
                        value=f'It is the base command for all {command} commands it doesnt do anything.',
                        inline=True
                    )
                elif command == 'town':
                    embed.add_field(
                        name=f'The {command} command',
                        value=f'It is the base command for all {command} commands it doesnt do anything.',
                        inline=True
                    )
                elif command == 'res':
                    embed.add_field(
                        name=f'The {command} command',
                        value=f'It is the base command for all {command} commands it doesnt do anything.',
                        inline=True
                    )
                elif command == 'server':
                    embed.add_field(
                        name=f'The {command} command',
                        value=f'It is the only {command} command and it displays server info.',
                        inline=True
                    )
                elif command == 'weather':
                    embed.add_field(
                        name=f'The {command} command',
                        value=f'It is the only {command} command and it displays server info.',
                        inline=True
                    )
                elif command == 'devcommands':
                    embed.add_field(
                        name=f'The {command} command',
                        value=f'The dev commands only ping is available to anyone',
                        inline=True
                    )
                await inter.edit_original_response(embed=embed)
            else:
                await inter.send("Invalid command or subcommand")
        except Exception as e:
            embed = Embeds.error_embed(
                value=e,
                footer=self.footer,
                author=inter
            )
            await inter.edit_original_response(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
