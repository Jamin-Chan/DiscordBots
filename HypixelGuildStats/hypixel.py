import requests, math, functions
import time
import secrets


API_KEY = secrets.uwusakura
API_KEY2 = secrets.uwutech
API_KEY3 = secrets.steven

# These are just values used to calculate the level (don't worry about them too much)
BASE = 10_000
GROWTH = 2_500
REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH
REVERSE_CONST = REVERSE_PQ_PREFIX
GROWTH_DIVIDES_2 = 2 / GROWTH

def get_level(name):
    url = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
    res = requests.get(url)
    data = res.json()
    
    if data["success"] == False:
      return "You have already looked up this name recently"

    if data["player"] is None:
        return None
        
    exp = int(data["player"]["networkExp"])
    return math.floor(1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * exp))


def get_guild(name):
    try:
      mojang_data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{name}?').json()
    except:
      return "The name you provided is not valid. Are you sure this is the correct name? `{user}`"
    else:
      data = requests.get(f"https://api.hypixel.net/player?key={API_KEY}&uuid={mojang_data['id']}").json()
      
    try:
      guildUuid = data["player"]["uuid"]

      findGuild = f"https://api.hypixel.net/findGuild?key={API_KEY}&byUuid={guildUuid}"
      res = requests.get(findGuild)
      data = res.json()
      guildId = data["guild"]
      guildUrl = f"https://api.hypixel.net/guild?key={API_KEY}&id={guildId}"
      res = requests.get(guildUrl)
      data = res.json()
      guildName = data["guild"]["name"]
      
    except:
      return "no guild"

    return guildName



def get_lastLogout(name, username):
  try:
      guildName = str(name["guild"]["name"])
      memberList = name["guild"]["members"]

  except:
    return "no guild"
  
  list1 = []
  list1.append(guildName)
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
      
    if counter % 2 == 0:
      person = f"https://api.hypixel.net/status?key={API_KEY}&uuid={memberUuid}"
    else:
      person = f"https://api.hypixel.net/status?key={API_KEY2}&uuid={memberUuid}"

    res = requests.get(person)
    status = res.json()

    try: 
      onlineStatus = status["session"]["online"]
      if onlineStatus == True:
        playerStatus = str(status["session"]["gameType"])
        try:
          playerStatus += ": " + str(status["session"]["mode"])
          try:
            playerStatus += " (" + str(status["session"]["map"]) + ")"
          except:
            pass
        except:
          pass
      else:
        try:
          playerStatus = int(guildMembers["player"]["lastLogout"])
          playerStatus = functions.number_to_time(playerStatus)
        except:
          playerStatus = "HIDDEN"

    except:
      return "no guild"
      
    list1.append(str(personName)  + " - " + str(playerStatus))

  return list1

def get_lastLogout_multiprocess(memberList, username):
    list1 = []
    counter = 0
    for member in memberList:
      memberUuid = member["uuid"]

      if counter % 3 == 0:
        person = f"https://api.hypixel.net/player?key={API_KEY}&uuid={memberUuid}"
      elif counter % 2 == 0:
        person = f"https://api.hypixel.net/player?key={API_KEY2}&uuid={memberUuid}"
      else:
        person = f"https://api.hypixel.net/player?key={API_KEY3}&uuid={memberUuid}"
      
      res = requests.get(person)
      guildMembers = res.json()

      personName = str(guildMembers["player"]["playername"])

      if personName == username:
        personName = "`**" + personName + "**`"

      print(personName)
      
      if counter % 2 == 0:
        person = f"https://api.hypixel.net/status?key={API_KEY}&uuid={memberUuid}"
      else:
        person = f"https://api.hypixel.net/status?key={API_KEY2}&uuid={memberUuid}"

      res = requests.get(person)
      status = res.json()
      
      counter += 1

      try: 
        onlineStatus = status["session"]["online"]
        if onlineStatus == True:
          playerStatus = str(status["session"]["gameType"])
          try:
            playerStatus += ": " + str(status["session"]["mode"])
            try:
              playerStatus += " (" + str(status["session"]["map"]) + ")"
            except:
              pass
          except:
            pass
        else:
          try:
            playerStatus = int(guildMembers["player"]["lastLogout"])
            playerStatus = functions.number_to_time(playerStatus)
          except:
            playerStatus = "HIDDEN"

      except:
        return "no guild"
      
      list1.append(str(personName)  + " - " + str(playerStatus))

    return list1



def get_guild_hypixelLvl(name, username):    
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

      time.sleep(0.2)
      print(personName)

      try:
        hypixelExp = int(guildMembers["player"]["networkExp"])
      except:
        hypixelExp = 0

      network_level = (math.sqrt((2 * hypixelExp) + 30625) / 50) - 2.5

      network_level *= 1000
      network_level = int(network_level)
      network_level /= 1000

      sorter.append(personName)
      sorter.append(network_level)
      leaderboard.append(network_level)

    leaderboard.sort(reverse = True)

    for x in leaderboard:
      lbFinal.append(str(sorter[sorter.index(x) - 1]) + " - " + str(x))
      sorter.remove(x)
      
    return lbFinal