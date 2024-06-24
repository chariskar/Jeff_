import disnake
import dotenv
from disnake.ext import  tasks
import os
from dotenv import load_dotenv
import random
from disnake.ext.commands import InteractionBot, Cog, command
from disnake.ext import commands
from Utils import monitor
import asyncio
bot: InteractionBot = commands.InteractionBot()

load_dotenv()
activities = [
    disnake.Game(name="play.earthmc.net"),
    disnake.Activity(type=disnake.ActivityType.listening, name="to your commands"),
    disnake.Activity(type=disnake.ActivityType.watching, name="ALL OF YOU"),
]


@tasks.loop(minutes=5)
async def change_status():
    activity = random.choice(activities)
    await bot.change_presence(activity=activity)


@bot.event
async def on_ready():
    change_status.start()
    print(f"Logged in as {bot.user}")

for file in os.listdir('Commands'):
    if file.endswith('py'):
        bot.load_extension(f'Commands.{file[:-3]}')
        
'''try:
    subprocess.run('main.py')
except Exception as e:
    raise e'''

try:
    token: str = str(dotenv.get_key('secrets.env', key_to_get='TOKEN'))
    bot.run(token)
    print(f'Logged in as {bot.user}')
    asyncio.run(monitor.Monitor().monitor())
    print('Monitor service running')
except Exception as e:
    raise e
