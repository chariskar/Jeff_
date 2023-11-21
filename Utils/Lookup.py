import aiohttp
from cachetools import TTLCache


class Lookup:
    cache: TTLCache = TTLCache(maxsize=289, ttl=150)

    @classmethod
    async def lookup(cls, server: str = 'aurora', endpoint=None, name=None,version:int=2):
        try:

            if endpoint is None:
                api_url = f"https://api.earthmc.net/v{version}/{server}/"
            elif name is None:
                api_url = f"https://api.earthmc.net/v{version}/{server}/{endpoint}"
            else:
                api_url = f"https://api.earthmc.net/v{version}/{server}/{endpoint}/{name}"
            try:
                if (server, endpoint, name) in cls.cache:
                    return cls.cache[(server, endpoint, name)]
                async with aiohttp.ClientSession() as session:
                    async with session.get(api_url) as response:
                        lookup = await response.json()
            except Exception as e:
                raise e
            cls.cache[(server, endpoint, name)] = lookup
            return lookup

        except Exception as e:
            raise e

    @classmethod
    def clear_cache(cls):
        try:
            cls.cache.clear()
        except Exception as e:
            raise e
