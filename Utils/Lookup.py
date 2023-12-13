import aiohttp
from cachetools import TTLCache
import json


class Lookup:
    cache: TTLCache = TTLCache(maxsize=289, ttl=150)

    @classmethod
    async def lookup(cls, server: str = 'aurora', endpoint=None, name=None, version: int = 2):
        try:

            if endpoint is None:
                api_url = f"https://api.earthmc.net/v{version}/{server}/"
            elif name is None:
                api_url = f"https://api.earthmc.net/v{version}/{server}/{endpoint}"
            else:
                api_url = f"https://api.earthmc.net/v{version}/{server}/{endpoint}/{name}"
            if endpoint == 'alliances':
                api_url = f'https://emctoolkit.vercel.app/api/aurora/alliances/{name}'
            if (server, endpoint, name) in cls.cache:
                return cls.cache[(server, endpoint, name)]
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url) as response:
                    response_text = await response.text()

                    content_type = response.headers.get('Content-Type', '').lower()
                    if 'application/json' in content_type:
                        lookup = json.loads(response_text)
                    else:
                        lookup = response_text

                    cls.cache[(server, endpoint, name)] = lookup

            return cls.cache.get((server, endpoint, name))
        except Exception as e:
            raise e

    @classmethod
    def clear_cache(cls):
        try:
            cls.cache.clear()
        except Exception as e:
            raise e
