import disnake
from disnake.ext.commands import InteractionBot, Cog, command
from disnake.ext import commands
from Utils.Embeds import Embeds

bot: InteractionBot = commands.InteractionBot()


class NewsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = 1158381660107198614
        self.guild_id = 1131117400985706538
        self.owner_id = 927581845787402240

    @commands.Cog.listener()
    async def on_socket_response(self, payload):
        if payload["t"] == "MESSAGE_CREATE":
            message = disnake.message.Message(data=payload["d"], state=self.bot._connection)
            await self.on_message(message)

    async def on_message(self, message: disnake.message.Message):
        try:
            guild: disnake.Guild = self.bot.get_guild(self.guild_id)
            channel: disnake.TextChannel = guild.get_channel(self.channel_id)
            owner: disnake.Member = guild.get_member(self.owner_id)

            if message.author.id == self.owner_id:
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
bot.add_cog(NewsCog(bot))
