import requests
import datetime
import discord
import secrets


API_KEY = secrets.uwusakura
API_KEY2 = secrets.uwutech
API_KEY3 = secrets.steven

def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

def name_to_memberList(name):
    try:
      mojang_data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{name}?').json()
    except:
      return "The name you provided is not valid. Are you sure this is the correct name? `{user}`"

    else:
      data = requests.get(f"https://api.hypixel.net/player?key={API_KEY}&uuid={mojang_data['id']}").json()

    guildUuid = data["player"]["uuid"]

    findGuild = f"https://api.hypixel.net/findGuild?key={API_KEY}&byUuid={guildUuid}"
    res = requests.get(findGuild)
    data = res.json()
    guildId = data["guild"]
    guildUrl = f"https://api.hypixel.net/guild?key={API_KEY}&id={guildId}"
    res = requests.get(guildUrl)
    data = res.json()

    return data
    try:
      memberList = data["guild"]["members"]

      return memberList
    except:
      return "no guild"



def number_to_time(timeStamp):

  timeStamp = timeStamp / 1000
  readable = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')
  
  return readable