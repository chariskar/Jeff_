import disnake
from disnake.ext import commands
import os
from disnake.ext.commands import InteractionBot

bot: InteractionBot = commands.InteractionBot()

@bot.event
async def on_ready():

    await bot.change_presence(activity=disnake.Game(name="play.earthmc.net"))
    print(f"Logged in as {bot.user}")
    print(f"Operating in {len(bot.guilds)} guild/s")
    print("Made by charis_k")

# bot.load_extension loads a file from another directory in this case the Utils directory it loads all the scripts

bot.load_extension("Utils.ServerCommand")
bot.load_extension("Utils.ResCommand")
bot.load_extension("Utils.TownCommand")
bot.load_extension("Utils.NationCommand")
bot.load_extension("Utils.ModerationCommands")
bot.load_extension("Utils.RoleManaging")
bot.load_extension("Utils.LevelingSystem")
bot.load_extension("Utils.VotingSystem")
bot.load_extension("Utils.weather")
bot.load_extension("Utils.AllianceCommand")

token = " MTEyMTc1MTQwMDI5NzI3OTU0OQ.GRa-a6.UOl9t-3MNC446ypGr_ofWx62bYg42fy3J0BI_Y "
if token:
    bot.run(token)
else:
    print("Failed to retrieve bot token.")