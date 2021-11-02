 #Jamin's Bot hi v2
#HYpixel Guild Stats- by uwutech

import discord
import hypixel, hypixelbw, hypixelsw
import functions
from discord.ext import commands
from keep_alive import keep_alive
from secret import *


client = commands.Bot(command_prefix = '^')
client.remove_command("help")


#makes sure the bot is running and working
@client.event
async def on_ready():
    print("nikhil sucks")
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening ,name="^help"))
    await client.change_presence(activity = discord.Streaming(name = "monke land", url = "https://www.twitch.tv/monketech"))



@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('do ^help to use me or bad')
        break
   


#the help command to show discord commands
@client.command()
async def help(ctx):
    helpEmbed = discord.Embed(
      title = "**:weary: Commands :weary:**",
      colour=0xFF7CEF
    )

    helpEmbed.add_field(name = "GUILD BW STATS", value = "`^guildbw <ign> fkdr \n^guildbw <ign> lvl \n^guildbw <ign> wins`", inline=True)
    helpEmbed.add_field(name = "GUILD SW STATS", value = "`^guildsw <ign> kills \n^guildsw <ign> lvl \n^guildsw <ign> wins`", inline=True)
    helpEmbed.add_field(name = "GUILD STATS", value = "`^guild <ign> lastonline \n^guild <ign> lvl`", inline=False)
    helpEmbed.add_field(name = "INDIVIDUAL STATS", value = "`^guildName <ign>\n^level <ign>`", inline=True)
    helpEmbed.add_field(name = "INVITE LINK", value = "`^invite`", inline=True)
    helpEmbed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/898736814658035712/902975179456643092/uwutech.PNG')

    numServers = len(client.guilds)
    helpEmbed.set_footer(text="I am in " + str(numServers) + " servers. Made by uwutech")

    await ctx.send(embed=helpEmbed) 

    #await ctx.send("**:weary:Commands:weary:** \n\n" 
    #  "^guildbw <ign> fkdr \n" 
    #  "^guildbw <ign> lvl \n"
    #  "^guildbw <ign> wins \n" 
    #  "^guildsw <ign> kills \n" 
    #  "^guildsw <ign> lvl \n" 
    #  "^guildsw <ign> wins \n"
    #  "^guild <ign> lastonline \n"
    #  "^guild <ign> lvl \n" 
    #  "^guildName <ign> \n" 
    #  "^level <ign>\n"
    #  "^invite")


@client.command()
async def invite(ctx): 
      await ctx.send("https://discord.com/api/oauth2/authorize?client_id=897325115568697374&permissions=534723950656&scope=bot")
    

#show the hypixel level of players
@client.command()
async def level(ctx, name):
    level = hypixel.get_level(name)
    if level == "You have already looked up this name recently":
      await ctx.send("You have already looked up this name recently... CHILLLLL")
    if level is None:
        await ctx.send("Player not found! (Make sure to use their **Minecraft** username)")
    else:
        await ctx.send(f"Level of user {name}: {level}")


#returns the guild name of provided player name
@client.command()
async def guildName(ctx, name):
    guild = hypixel.get_guild(name)
    if guild is None:
        await ctx.send("Player not found! (Make sure to use their **Minecraft** username)")
    elif guild == "no guild":
      await ctx.send("This player is not in a guild")
    else:
        await ctx.send(":monkey_face:" + guild + ":monkey_face:")


#runs and general stats of the whole guild
#arg determines which stat (lastonline/lvl)
@client.command()
async def guild(ctx, name, arg):
    memberList = []
    finalMsg, finalMsg2, finalMsg3, finalMsg4, finalMsg5, finalMsg6, finalMsg7 = "", "`", "`", "`", "`", "`", "`"

    try:
      data = functions.name_to_memberList(name)
      memberList = data["guild"]["members"]

      estTime = functions.get_number_of_elements(memberList)

    except:
      memberList == "no guild"

#determines the arg the user input
    if arg == "lastonline":
      estTime = functions.get_number_of_elements(memberList)
      await ctx.send("estimated time: " + str(estTime/2) + " seconds")
      memberList = hypixel.get_lastLogout(data, name)
      title = "**LastLogins(UTC) - " + str(memberList[0]) + "**"
    
    elif arg == "lvl":
      estTime = functions.get_number_of_elements(memberList)
      await ctx.send("estimated time: " + str(estTime/2) + " seconds")
      memberList = hypixel.get_guild_hypixelLvl(data, name)
      title = "**Hypixel Levels - " + str(memberList[0]) + "**"
    
    else:
      await ctx.send("That is not a command :sob:")
    
    if memberList == "The name you provided is not valid. Are you sure this is the correct name? `{user}`":
      await ctx.send(memberList) 
      
    elif memberList == "no guild": #sends if player is not in a guild
      await ctx.send("This player is not in a guild")
    
    else:
      finalMsg += "`"

#creates the msg to send into discord
      if memberList is None:
          await ctx.send("Player not found! (Make sure to use their **Minecraft** username)")

      else:
          counter = 0
          counter2 = 1
          for x in memberList:
            if memberList.index(x) < 20:
              try:
                finalMsg += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 40:
              try:
                finalMsg2 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 60:
              try:
                finalMsg3 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 80:
              try:
                finalMsg4 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 100:
              try:
                finalMsg5 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 120:
              try:
                finalMsg6 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            else:
              try:
                finalMsg7 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
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
            title = title,
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
async def guildsw(ctx, name, arg):
    memberList = []
    finalMsg, finalMsg2, finalMsg3, finalMsg4, finalMsg5, finalMsg6, finalMsg7 = "", "`", "`", "`", "`", "`", "`"

    try:
      data = functions.name_to_memberList(name)
      memberList = data["guild"]["members"]

      estTime = functions.get_number_of_elements(memberList)

    except:
       memberList == "no guild"

    if arg == "wins":
      estTime = functions.get_number_of_elements(memberList)
      await ctx.send("estimated time: " + str(estTime/2) + " seconds")
      memberList = hypixelsw.get_guild_swWin(data, name)
      title = "**Skywars Wins Leaderboard - " + str(memberList[0]) + "**"

    elif arg == "lvl":
      estTime = functions.get_number_of_elements(memberList)
      await ctx.send("estimated time: " + str(estTime/2) + " seconds")
      memberList = hypixelsw.get_guild_swLvl(data, name)
      title = "**Skywars Level Leaderboard - " + str(memberList[0]) + "**"

    elif arg == "kills":
      estTime = functions.get_number_of_elements(memberList)
      await ctx.send("estimated time: " + str(estTime/2) + " seconds")
      memberList = hypixelsw.get_guild_swKill(data, name)
      title = "**Skywars Kills Leaderboard - " + str(memberList[0]) + "**"
    
    else:
      await ctx.send("That is not a command :sob:")
    

    if memberList == "The name you provided is not valid. Are you sure this is the correct name? `{user}`":
      await ctx.send(memberList) 
      
    elif memberList == "no guild":
      await ctx.send("This player is not in a guild") 

    else:
      finalMsg += "`" 
 
      if memberList is None:
          await ctx.send("Player not found! (Make sure to use their **Minecraft** username)")

      else:
          counter = 0
          counter2 = 1
          for x in memberList:
            if memberList.index(x) < 20:
              try:
                finalMsg += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 40:
              try:
                finalMsg2 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 60:
              try:
                finalMsg3 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 80:
              try:
                finalMsg4 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 100:
              try:
                finalMsg5 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 120:
              try:
                finalMsg6 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            else:
              try:
                finalMsg7 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
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
            title = title,
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
async def guildbw(ctx, name, arg):
    memberList = []
    finalMsg, finalMsg2, finalMsg3, finalMsg4, finalMsg5, finalMsg6, finalMsg7 = "", "`", "`", "`", "`", "`", "`"

    try:
      data = functions.name_to_memberList(name)
      memberList = data["guild"]["members"]

    except:
       memberList == "no guild"
       
    if arg == "fkdr":
      estTime = functions.get_number_of_elements(memberList)
      await ctx.send("estimated time: " + str(estTime/2) + " seconds")
      memberList = hypixelbw.get_guild_bwFkdr(data, name)
      title = "**Bedwars FKDR LeaderBoard - " + str(memberList[0]) + "**"

    elif arg == "lvl":
      estTime = functions.get_number_of_elements(memberList)
      await ctx.send("estimated time: " + str(estTime/2) + " seconds")
      memberList = hypixelbw.get_guild_bwLvl(data, name)
      title = "**Bedwars Stars Leaderboard - " + str(memberList[0]) + "**"

    elif arg == "wins":
      estTime = functions.get_number_of_elements(memberList)
      await ctx.send("estimated time: " + str(estTime/2) + " seconds")
      memberList = hypixelbw.get_guild_bwWin(data, name)
      title = "**Bedwars Wins Leaderboard - " + str(memberList[0]) + "**"
    
    else:
      await ctx.send("That is not a command :sob:")
    
    if memberList == "The name you provided is not valid. Are you sure this is the correct name? `{user}`":
      await ctx.send(memberList) 
    
    elif memberList == "no guild":
      await ctx.send("This player is not in a guild") 

    else:
      finalMsg += "`"

      if memberList is None:
          await ctx.send("Player not found! (Make sure to use their **Minecraft** username)")

      else:
          counter = 0
          counter2 = 1
          for x in memberList:
            if memberList.index(x) < 20:
              try:
                finalMsg += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 40:
              try:
                finalMsg2 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 60:
              try:
                finalMsg3 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 80:
              try:
                finalMsg4 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 100:
              try:
                finalMsg5 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            elif memberList.index(x) < 120:
              try:
                finalMsg6 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
                counter += 1
                counter2 += 1
              except:
                break
            else:
              try:
                finalMsg7 += str(counter2) + " - " + str(memberList[counter + 1] + "\n")
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
            title = title,
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
my_secret = TOKEN
client.run(my_secret)