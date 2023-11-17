import aiohttp
import time


class CommandTools:
    def list_to_string(*args):
        return "\n".join(str(item) for item in args)

    @staticmethod
    def get_weather(serverLookup):
        if serverLookup["world"]["hasStorm"] and serverLookup["world"]["isThundering"]:
            weather = "Thundering"
        elif serverLookup["world"]["hasStorm"]:
            weather = "Raining"
        else:
            weather = "Clear"

        return weather

    @staticmethod
    def rnao_perms(json):
        rnaoPermsList = []
        permsKeyList = ["buildPerms", "destroyPerms", "switchPerms", "itemUsePerms"]

        count = 0
        try:
            for _ in json["perms"]["rnaoPerms"]:
                try:
                    resident = json["perms"]["rnaoPerms"][permsKeyList[count]]["resident"]
                except:
                    friend = json["perms"]["rnaoPerms"][permsKeyList[count]]["friend"]
                try:
                    nation = json["perms"]["rnaoPerms"][permsKeyList[count]]["nation"]
                except:
                    town = json["perms"]["rnaoPerms"][permsKeyList[count]]["town"]
                ally = json["perms"]["rnaoPerms"][permsKeyList[count]]["ally"]
                outsider = json["perms"]["rnaoPerms"][permsKeyList[count]]["outsider"]

                rnaoString = "----"
                try:
                    if resident:
                        rnaoString = "r" + rnaoString[1:]
                except:
                    if friend:
                        rnaoString = "f" + rnaoString[1:]
                try:
                    if nation:
                        rnaoString = rnaoString[:1] + "n" + rnaoString[2:]
                except:
                    if town:
                        rnaoString = rnaoString[:1] + "t" + rnaoString[2:]
                if ally:
                    rnaoString = rnaoString[:2] + "a" + rnaoString[3:]
                if outsider:
                    rnaoString = rnaoString[:-1] + "o"

                rnaoPermsList.append(rnaoString)

                count = count + 1

            return rnaoPermsList

        except Exception as e:
            raise e

    @staticmethod
    def claim_bonus(resident_amt: int):
        if resident_amt >= 120:
            return 80
        elif resident_amt >= 80:
            return 60
        elif resident_amt >= 60:
            return 50
        elif resident_amt >= 40:
            return 30
        elif resident_amt >= 20:
            return 10
        else:
            return 0


    @staticmethod
    async def get_discord_api_latency():
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            async with session.get('https://discord.com/api/v10/gateway'):
                end_time = time.time()
                latency = (end_time - start_time) * 1000
                return latency
