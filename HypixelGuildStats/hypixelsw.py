import requests, math
import time
import secrets


API_KEY = secrets.uwusakura
API_KEY2 = secrets.uwutech
API_KEY3 = secrets.steven

def get_guild_swLvl(name, username):
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

#calculate skywars exp to skywars level
      try:
        skywarsExp = int(guildMembers["player"]["stats"]["SkyWars"]["skywars_experience"])

        skywarsLvl = 0
    
        if skywarsExp >= 15000:
          skywarsLvl += 12
          skywarsExp -= 15000

          skywarsLvl += (skywarsExp // 10000)  
          skywarsExp -= ((skywarsLvl - 12) * 10000)
          skywarsLvl += skywarsExp / 10000
          print(skywarsLvl)

        elif skywarsExp >= 10000:
          skywarsLvl += 11
          skywarsExp -= 10000
          skywarsLvl += skywarsExp / 5000
        elif skywarsExp >= 6000:
          skywarsLvl += 10
          skywarsExp -= 6000
          skywarsLvl += skywarsExp / 4000
        elif skywarsExp >= 3500:
          skywarsLvl += 9
          skywarsExp -= 3500
          skywarsLvl += skywarsExp / 2500
        elif skywarsExp >= 2000:
          skywarsLvl += 8
          skywarsExp -= 2000
          skywarsLvl += skywarsExp / 1500
        elif skywarsExp >= 1000:
          skywarsLvl += 7
          skywarsExp -= 1000
          skywarsLvl += skywarsExp / 1000
        elif skywarsExp >= 500:
          skywarsLvl += 6
          skywarsExp -= 500
          skywarsLvl += skywarsExp / 500
        elif skywarsExp >= 250:
          skywarsLvl += 5
          skywarsExp -= 250
          skywarsLvl += skywarsExp / 250
        elif skywarsExp >= 150:
          skywarsLvl += 4
          skywarsExp -= 150
          skywarsLvl += skywarsExp / 100
        elif skywarsExp >= 70:
          skywarsLvl += 3
          skywarsExp -= 70
          skywarsLvl += skywarsExp / 80
        elif skywarsExp >= 20:
          skywarsLvl += 2
          skywarsExp -= 20
          skywarsLvl += skywarsExp / 50
        elif skywarsExp >= 0:
          skywarsLvl += 1
          skywarsLvl += skywarsExp / 20

        skywarsLvl *= 1000
        skywarsLvl = int(skywarsLvl)
        skywarsLvl /= 1000

      except:
        skywarsLvl = 0

      sorter.append(personName)
      sorter.append(skywarsLvl)
      leaderboard.append(skywarsLvl)

    leaderboard.sort(reverse = True)
    
    for x in leaderboard:
      lbFinal.append(str(sorter[sorter.index(x) - 1]) + " - " + str(x))
      sorter.remove(x)

    return lbFinal



def get_guild_swWin(name, username): 
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

#calculate skywars exp to skywars level
      try:
        skywarsWins = int(guildMembers["player"]["stats"]["SkyWars"]["wins"])
        
      except:
        skywarsWins = 0

      sorter.append(personName)
      sorter.append(skywarsWins)
      leaderboard.append(skywarsWins)

    leaderboard.sort(reverse = True)
    
    for x in leaderboard:
      lbFinal.append(str(sorter[sorter.index(x) - 1]) + " - " + str(x))
      sorter.remove(x)

    return lbFinal



def get_guild_swKill(name, username):
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

#calculate skywars exp to skywars level
      try:
        skywarsKills = int(guildMembers["player"]["stats"]["SkyWars"]["kills"])

      except:
        skywarsKills = 0

      sorter.append(personName)
      sorter.append(skywarsKills)
      leaderboard.append(skywarsKills)

    leaderboard.sort(reverse = True)
    
    for x in leaderboard:
      lbFinal.append(str(sorter[sorter.index(x) - 1]) + " - " + str(x))
      sorter.remove(x)

    return lbFinal