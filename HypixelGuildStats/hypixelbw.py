import requests, math
import functions
import secrets


API_KEY = secrets.uwusakura
API_KEY2 = secrets.uwutech
API_KEY3 = secrets.steven


def get_guild_bwLvl(name, username):    
    try:
      guildName = str(name["guild"]["name"])
      memberList = name["guild"]["members"]

    except: 
      return "no guild"
      
    leaderboard = []
    lbFinal = []
    lbFinal.append(guildName)
    sorter = []
    counter = 0

    for member in memberList:
      memberUuid = member["uuid"]

      if counter % 3 == 0:
        person = f"https://api.hypixel.net/player?key={API_KEY}&uuid={memberUuid}"
      elif counter % 2 == 0:
        person = f"https://api.hypixel.net/player?key={API_KEY2}&uuid={memberUuid}"
      else:
        person = f"https://api.hypixel.net/player?key={API_KEY3}&uuid={memberUuid}"

      counter += 1

      res = requests.get(person)
      guildMembers = res.json()

      personName = str(guildMembers["player"]["playername"])
      
      if personName == username:
        personName = "`**" + personName + "**`"
    
      print(personName)

      try:
        bedwarsExp = int(guildMembers["player"]["stats"]["Bedwars"]["Experience"])

#calc bedwars exp to bedwars level
        bedwarsLvl = (bedwarsExp // 488000)
      
        print(bedwarsLvl)
        bedwarsExp -= (bedwarsLvl * 488000)
        bedwarsLvl *= 100    

        if bedwarsExp >= 8000:
          bedwarsLvl += 4
          bedwarsExp -= 8000
        elif bedwarsExp >= 4500:
          bedwarsLvl += 3
          bedwarsExp -= 4500
        elif bedwarsExp >= 1500:
          bedwarsLvl += 2
          bedwarsExp -= 1500
        elif bedwarsExp >= 500:
          bedwarsLvl += 1
          bedwarsExp -= 500
      
        bedwarsLvl += (bedwarsExp / 5000)
        bedwarsLvl *= 100
        bedwarsLvl = int(bedwarsLvl)
        bedwarsLvl /= 100

      except:
        bedwarsLvl = 0

      sorter.append(personName)
      sorter.append(bedwarsLvl)
      leaderboard.append(bedwarsLvl)

    leaderboard.sort(reverse = True)

    for x in leaderboard:
      lbFinal.append(str(sorter[sorter.index(x) - 1]) + " - " + str(x))
      sorter.remove(x)

    return lbFinal
    
def get_guild_bwFkdr(name, username):
    try:
      guildName = str(name["guild"]["name"])
      memberList = name["guild"]["members"]

    except: 
      return "no guild"

    leaderboard = []
    lbFinal = []
    lbFinal.append(guildName)
    sorter = []
    counter = 0

    for member in memberList:
      memberUuid = member["uuid"]
      
      if counter % 3 == 0:
        person = f"https://api.hypixel.net/player?key={API_KEY}&uuid={memberUuid}"
      elif counter % 2 == 0:
        person = f"https://api.hypixel.net/player?key={API_KEY2}&uuid={memberUuid}"
      else:
        person = f"https://api.hypixel.net/player?key={API_KEY3}&uuid={memberUuid}"
      
      counter += 1
      
      res = requests.get(person)
      guildMembers = res.json()

      personName = str(guildMembers["player"]["playername"])

      if personName == username:
        personName = "`**" + personName + "**`"

      print(personName)

      try:
        bedwarsFinals = int(guildMembers["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
        bedwarsFinalDeaths = int(guildMembers["player"]["stats"]["Bedwars"]["final_deaths_bedwars"])
      
#calc bedwars fkdr
        bedwarsFkdr = bedwarsFinals/bedwarsFinalDeaths
        bedwarsFkdr *= 1000
        bedwarsFkdr = int(bedwarsFkdr)
        bedwarsFkdr /= 1000

      except:
        bedwarsFkdr = 0
      
      sorter.append(personName)
      sorter.append(bedwarsFkdr)
      leaderboard.append(bedwarsFkdr)

    leaderboard.sort(reverse = True)

    for x in leaderboard:
      lbFinal.append(str(sorter[sorter.index(x) - 1]) + " - " + str(x))
      sorter.remove(x)

    return lbFinal

def get_guild_bwWin(name, username):
    try:
      guildName = str(name["guild"]["name"])
      memberList = name["guild"]["members"]
      
    except: 
      return "no guild"
      
    leaderboard = []
    lbFinal = []
    lbFinal.append(guildName)
    sorter = []

    counter = 0
    for member in memberList:
      memberUuid = member["uuid"]

      if counter % 3 == 0:
        person = f"https://api.hypixel.net/player?key={API_KEY}&uuid={memberUuid}"
      elif counter % 2 == 0:
        person = f"https://api.hypixel.net/player?key={API_KEY2}&uuid={memberUuid}"
      else:
        person = f"https://api.hypixel.net/player?key={API_KEY3}&uuid={memberUuid}"

      counter += 1
      
      res = requests.get(person)
      guildMembers = res.json()

      personName = str(guildMembers["player"]["playername"])

      if personName == username:
        personName = "`**" + personName + "**`"

      print(personName)

      try:
        bedwarsWins = int(guildMembers["player"]["achievements"]["bedwars_wins"])

      except:
        bedwarsWins = 0

      sorter.append(personName)
      sorter.append(bedwarsWins)
      leaderboard.append(bedwarsWins)

    leaderboard.sort(reverse = True)

    for x in leaderboard:
      lbFinal.append(str(sorter[sorter.index(x) - 1]) + " - " + str(x))
      sorter.remove(x)
      
    return lbFinal