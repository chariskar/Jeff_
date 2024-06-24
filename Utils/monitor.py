from Utils import Lookup
from disnake.ext import commands
from disnake.ext import  tasks
from disnake.ext.commands import InteractionBot
import pytz,datetime, random
monitored = [
    'Savageplant702',
    'Friendofmario',
    'Leslynuts',
    'Moomincrimes',
    'Arielblablabla',
    'Oreosodas',
    'Kombolizmo',
    'Dwaggo15',
    'Aether182',
    'Yarou',
    'brylol1201',
    'John_By',
    'Psllonllc',
    'Wallguardian',
    'KangChub',
    'Creepyguardian'
]


class Monitor():
    def __init__(self, enabled: bool):pass
        
    @tasks.loop(minutes=1440)
    async def monitor(self,bot: InteractionBot):      
        tz = pytz.timezone('Europe/Stockholm')
        for name in monitored:
            lookup = await Lookup.lookup(
                server='aurora',
                endpoint='residents',
                name=name,
                version=1
            )
            if not lookup:
                return
            time = lookup['timestamps']['lastOnline'] / 1000
            now = datetime.datetime.now(tz)
            difference = now - time
            difference = difference * 60 * 1440
            if difference >= 30:
                channel = bot.fetch_channel(1098076385085505598)
                channel.send(f'{name} has {difference} days before 42d')
