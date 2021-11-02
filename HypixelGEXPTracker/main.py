#Jamin's discord bot (uwutech)

import discord
from discord.ext import commands
from keep_alive import keep_alive
import functions
import requests
import datetime
import secrets

client = commands.Bot(command_prefix = '&')
client.remove_command("help")
API_KEY = secrets.uwusakura
API_KEY2 = secrets.uwutech
API_KEY3 = secrets.steven


@client.event
async def on_ready():
    print("nikhil sucks")
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening ,name="^help"))
    await client.change_presence(activity = discord.Streaming(name = "monke land", url = "https://www.twitch.tv/monketech"))

@client.command()
async def invite(ctx): 
      await ctx.send("https://discord.com/api/oauth2/authorize?client_id=903057763108814888&permissions=534723951680&scope=bot")

@client.command()
async def help(ctx):
    helpEmbed = discord.Embed(
      title = "**:weary: Commands :weary:**",
      colour=0xFF7CEF
    )

    helpEmbed.add_field(name = "GEXP GRABBER", value = "`&getweekly <guild name>\n&getdaily <guild name>`", inline=True)
    helpEmbed.add_field(name = "INVITE LINK", value = "`&invite`", inline=True)
    helpEmbed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/898736814658035712/902975179456643092/uwutech.PNG')

    numServers = len(client.guilds)
    helpEmbed.set_footer(text="I am in " + str(numServers) + " servers. Made by uwutech")

    await ctx.send(embed=helpEmbed) 

@client.command()
async def getweekly(ctx, *guild):
  sorter = []
  leaderboard = []

  guildName = "+".join(guild)
  print(guildName)
  today = datetime.date.today()
  day1 = today - datetime.timedelta(days=7)
  day2 = today - datetime.timedelta(days=6)
  day3 = today - datetime.timedelta(days=5)
  day4 = today - datetime.timedelta(days=4)
  day5 = today - datetime.timedelta(days=3)
  day6 = today - datetime.timedelta(days=2)
  day7 = today - datetime.timedelta(days=1)
  day8 = today - datetime.timedelta(days=0)

  guildInfo = functions.get_guildInfo(guildName)
  try:
    memberList = guildInfo["guild"]["members"]
    estTime = functions.get_number_of_elements(memberList)
    await ctx.send("estimated time: " + str(estTime/6) + " seconds")
  except:
    await ctx.send("**" + guildName + "**" + " IS NOT A GUILD MONKE")

  counter = 0
  for member in memberList:
      lbFinal = []
      exp = 0
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
      print(personName)

      try:
        exp += member["expHistory"][str(day8)]
      except:
        exp += member["expHistory"][str(day1)]

      exp += member["expHistory"][str(day2)]
      exp += member["expHistory"][str(day3)]
      exp += member["expHistory"][str(day4)]
      exp += member["expHistory"][str(day5)]
      exp += member["expHistory"][str(day6)]
      exp += member["expHistory"][str(day7)]

      sorter.append(personName)
      sorter.append(exp)
      leaderboard.append(exp)

      leaderboard.sort(reverse = True)

  for x in leaderboard:
    lbFinal.append(str(sorter[sorter.index(x) - 1]) + " - " + str(x))
    sorter.remove(x)

  finalMsg, finalMsg2, finalMsg3, finalMsg4, finalMsg5, finalMsg6, finalMsg7 = "`", "`", "`", "`", "`", "`", "`"
  counter = 0
  counter2 = 1

  for x in lbFinal:
    if lbFinal.index(x) < 20:
      try:
        finalMsg += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
    elif lbFinal.index(x) < 40:
      try:
        finalMsg2 += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
    elif lbFinal.index(x) < 60:
      try:
        finalMsg3 += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
    elif lbFinal.index(x) < 80:
      try:
        finalMsg4 += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
    elif lbFinal.index(x) < 100:
      try:
        finalMsg5 += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
    elif lbFinal.index(x) < 120:
      try:
        finalMsg6 += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
    else:
      try:
        finalMsg7 += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
                
  finalMsg += "`"
  finalMsg2 += "`"
  finalMsg3 += "`"
  finalMsg4 += "`"
  finalMsg5 += "`"
  finalMsg6 += "`"
  finalMsg7 += "`"
  #checks if discord needs to send multiple message
  finalText = discord.Embed(
    title = "Weekly GEXP Leaderboard" + " - " + " ".join(guild),
    colour=0xFF7CEF
  )

  finalText.add_field(name = "Top 20", value = finalMsg, inline=False)

  if finalMsg2 != "``":
    finalText.add_field(name = "Top 40", value = finalMsg2, inline=False)

  if finalMsg3 != "``":
    finalText.add_field(name = "Top 60", value = finalMsg3, inline=False)
          
  if finalMsg4 != "``":
    finalText.add_field(name = "Top 80", value = finalMsg4, inline=False)

  if finalMsg5 != "``":
    finalText.add_field(name = "Top 100", value = finalMsg5, inline=False)
          
  if finalMsg6 != "``":
    finalText.add_field(name = "Top 120", value = finalMsg6, inline=False)

  if finalMsg7 != "``":
    finalText.add_field(name = "Top 125", value = finalMsg7, inline=False)

  numServers = len(client.guilds)
  finalText.set_footer(text="I am in " + str(numServers) + " servers. Made by uwutech")
  await ctx.send(embed=finalText)


@client.command()
async def getName(ctx, uuid):
  name = requests.get(f'https://api.mojang.com/user/profiles/{uuid}/names').json()
  name = name["name"]
  await ctx.send(name)



@client.command()
async def getdaily(ctx, *guild):
  sorter = []
  leaderboard = []

  guildName = "+".join(guild)
  print(guildName)
  today = datetime.date.today()
  day7 = today - datetime.timedelta(days=1)
  day8 = today - datetime.timedelta(days=0)

  guildInfo = functions.get_guildInfo(guildName)
  try:
    memberList = guildInfo["guild"]["members"]
    estTime = functions.get_number_of_elements(memberList)
    await ctx.send("estimated time: " + str(estTime/6) + " seconds")
  except:
    await ctx.send("**" + guildName + "**" + " IS NOT A GUILD MONKE")

  counter = 0
  for member in memberList:
      lbFinal = []
      exp = 0
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
      print(personName)

      try:
        exp += member["expHistory"][str(day7)]
      except:
        exp += member["expHistory"][str(day8)]

      sorter.append(personName)
      sorter.append(exp)
      leaderboard.append(exp)

      leaderboard.sort(reverse = True)

  for x in leaderboard:
    lbFinal.append(str(sorter[sorter.index(x) - 1]) + " - " + str(x))
    sorter.remove(x)

  finalMsg, finalMsg2, finalMsg3, finalMsg4, finalMsg5, finalMsg6, finalMsg7 = "`", "`", "`", "`", "`", "`", "`"
  counter = 0
  counter2 = 1

  for x in lbFinal:
    if lbFinal.index(x) < 20:
      try:
        finalMsg += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
    elif lbFinal.index(x) < 40:
      try:
        finalMsg2 += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
    elif lbFinal.index(x) < 60:
      try:
        finalMsg3 += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
    elif lbFinal.index(x) < 80:
      try:
        finalMsg4 += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
    elif lbFinal.index(x) < 100:
      try:
        finalMsg5 += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
    elif lbFinal.index(x) < 120:
      try:
        finalMsg6 += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
    else:
      try:
        finalMsg7 += str(counter2) + " - " + str(lbFinal[counter] + "\n")
        counter += 1
        counter2 += 1
      except:
        break
                
  finalMsg += "`"
  finalMsg2 += "`"
  finalMsg3 += "`"
  finalMsg4 += "`"
  finalMsg5 += "`"
  finalMsg6 += "`"
  finalMsg7 += "`"
  #checks if discord needs to send multiple message
  finalText = discord.Embed(
    title = "Daily GEXP Leaderboard" + " - " + " ".join(guild),
    colour=0xFF7CEF
  )

  finalText.add_field(name = "Top 20", value = finalMsg, inline=False)

  if finalMsg2 != "``":
    finalText.add_field(name = "Top 40", value = finalMsg2, inline=False)

  if finalMsg3 != "``":
    finalText.add_field(name = "Top 60", value = finalMsg3, inline=False)
          
  if finalMsg4 != "``":
    finalText.add_field(name = "Top 80", value = finalMsg4, inline=False)

  if finalMsg5 != "``":
    finalText.add_field(name = "Top 100", value = finalMsg5, inline=False)
          
  if finalMsg6 != "``":
    finalText.add_field(name = "Top 120", value = finalMsg6, inline=False)

  if finalMsg7 != "``":
    finalText.add_field(name = "Top 125", value = finalMsg7, inline=False)

  numServers = len(client.guilds)
  finalText.set_footer(text="I am in " + str(numServers) + " servers. Made by uwutech")
  await ctx.send(embed=finalText)



keep_alive()
my_secret = secrets.TOKEN
client.run(my_secret)