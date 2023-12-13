import disnake
from disnake.ext.commands import InteractionBot, Cog, command
from disnake.ext import commands
from Utils.Embeds import Embeds

bot: InteractionBot = commands.InteractionBot()


class NewsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    async def on_message(self, guild_id, channel_id, owner_id):
        try:
            guild: disnake.Guild = self.bot.get_guild(guild_id)
            channel: disnake.TextChannel = guild.get_channel(channel_id)

            if channel.last_message.author.id == owner_id:
                last_message = str(channel.last_message.content)
                message_last: disnake.message.Message = channel.last_message

                if not message_last.mention_everyone:
                    if not last_message.islower():
                        last_message = last_message.lower()
                elif message_last.mention_everyone:
                    last_message += ' message contains mention'

                return last_message

        except Exception as e:
            raise e




# Add the cog to the bot

