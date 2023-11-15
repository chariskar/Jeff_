import disnake
from disnake.ext import commands
from Utils.Embeds import Embeds
import requests
import aiohttp
import dotenv
dotenv.load_dotenv()


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="weather", help="Get the current weather for a location.", description="Get the current weather for a location")
    async def weather(self, inter: disnake.ApplicationCommandInteraction, location: str, unit: str = "metric"):
        valid_units = ["metric", "imperial"]
        unit = unit.lower()

        if unit not in valid_units:
            await inter.response.send_message("Invalid unit system. Please use 'metric' or 'imperial'.")
            return

        api_key = dotenv.get_key(dotenv_path='OPENWEATHER.env', key_to_get='KEY')
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        params: dict = {
            "q": location,
            "appid": api_key,
            "units": unit,
        }

        async with aiohttp.ClientSession as session:
            async with session.get(url=base_url,params=params) as response:
                response = response.json

        weather_description = response["weather"][0]["description"]
        temperature = response["main"]["temp"]
        humidity = response["main"]["humidity"]
        wind_speed = response["wind"]["speed"]
        unit_symbol = "°C" if unit == "metric" else "°F"
        embed = Embeds.embed_builder(title=f'Weather in {location}',author=inter.author)
        embed.add_field(name="Description", value=weather_description, inline=True)
        embed.add_field(name="Temperature", value=f"{temperature} {unit_symbol}", inline=True)
        embed.add_field(name="Humidity", value=f"{humidity}%", inline=True)
        embed.add_field(name="Wind Speed", value=f"{wind_speed} m/s", inline=True)
        await inter.response.send_message(embed=embed)



def setup(bot):
    bot.add_cog(Weather(bot))
