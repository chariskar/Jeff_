import disnake
import dotenv
from disnake.ext import  tasks
import os
from dotenv import load_dotenv
import random
from Utils.Bot_News import bot

load_dotenv()
activities = [
    disnake.Game(name="play.earthmc.net"),
    disnake.Activity(type=disnake.ActivityType.listening, name="to your commands"),
    disnake.Activity(type=disnake.ActivityType.watching, name="ALL OF YOU"),
    disnake.Game(name='I have a brother Jefferson ModMail')

]


@tasks.loop(minutes=5)
async def change_status():
    activity = random.choice(activities)
    await bot.change_presence(activity=activity)


@bot.event
async def on_ready():
    change_status.start()
    print(f"Logged in as {bot.user}")
    print(f"Operating in {bot.guilds} guild/s")

# bot.load_extension loads a file from another directory in this case the Commands directory it loads all the scripts




for file in os.listdir('Commands'):
    if file.endswith('py'):
        bot.load_extension(f'Commands.{file[:-3]}')
'''try:
    subprocess.run('main.py')
except Exception as e:
    raise e'''

try:
    token: str = dotenv.get_key('TOKEN.env', key_to_get='TOKEN')
    bot.run(token)
    print(f'Logged in as {bot.user}')
except Exception as e:
    raise e
