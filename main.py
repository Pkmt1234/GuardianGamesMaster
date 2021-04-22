import discord
import os
from replit import db
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  
  if "ServerID" not in db.keys():
    db["ServerID"] = []

  if "ChannelID" not in db.keys():
    db["ChannelID"] = []
  
  if "Titans" not in db.keys():
    db["Titans"] = 0
  
  if "Warlocks" not in db.keys():
    db["Warlocks"] = 0
   
  if "Hunters" not in db.keys():
    db["Hunters"] = 0
  
  
  if "Tgold" not in db.keys():
    db["Tgold"] = 0
  
  if "Wgold" not in db.keys():
    db["Wgold"] = 0
   
  if "Hgold" not in db.keys():
    db["Hgold"] = 0
  
  if "Tsilver" not in db.keys():
    db["Tsilver"] = 0
  
  if "Wsilver" not in db.keys():
    db["Wsilver"] = 0
   
  if "Hsilver" not in db.keys():
    db["Hsilver"] = 0

  if "Tbronze" not in db.keys():
    db["Tbronze"] = 0
  
  if "Wbronze" not in db.keys():
    db["Wbronze"] = 0
   
  if "Hbronze" not in db.keys():
    db["Hbronze"] = 0
  
  if "resultsmessage" not in db.keys():
    db["resultsmessage"] = ""
  
  await client.change_presence(activity=discord.Game('//setup to set up the bot!'))

@client.event
async def on_guild_join(guild):
  await guild.system_channel.send("Thank you for using the Guardian Games Master bot!\nThis bot will give daily updates on the games, including a bunch of other fun stats. In order to help you set up the bot, use //setup.\nUse //help to get all info on other commands")
  print("Joined Server")

            


@client.event
async def on_message(message):

  if message.author == client.user:
        return

  msg = message.content

  if msg.startswith("//setup"):
    if message.author.top_role.permissions.administrator:
      await message.channel.send("Setting up the bot can be done in a few simple steps:\n1: In order to receive daily updates on the winning class, leaderboard, and strike modifiers, use \"//channel set #channel\" in order to choose the channel that you want these updates to appear in.\nShould you ever want to turn these messages off, use \"//channel disable #channel\" to disable it.\n\n2:This bot can change the colors of roles to reflect the color of the in-game class item. In order to set this up, create 3 roles with the names \"Titan\", \"Hunter\", and \"Warlock\".\nYou can assign these roles to members yourself or by using a bot like yagpdb.xyz to do this for you with a rolemenu. These roles will change between bronze/silver/gold on a daily basis.\n**MAKE SURE THAT THE GUARDIAN GAMES MASTER BOT IS ABOVE THESE 3 CLASS ROLES TO MAKE SURE THE BOT CAN CHANGE THESE COLORS.**\n\nTo see what else this bot can do, use //help")
      return
    else:
      await message.channel.send("You don't have permission to do that. Only members with the administrator permission can set up the bot")
  
  if msg.startswith("//channel set <#"):
    try:
      if message.author.top_role.permissions.administrator:
        msg = msg.split("//channel set <#", 1)[1]
        msg = msg.split(">", 1)[0]
        if msg in db["ChannelID"]:
          await message.channel.send("This is already an active channel. Use //channel disable #channel to disable it.")
          return

        db["ServerID"].append(message.guild.id)
        db["ChannelID"].append(int(msg))
        channel = client.get_channel(int(msg))
        await message.channel.send("<#" + str(channel.id) + "> has been set. This channel will receive all Guardian Games updates!")
        print("Channel added " + str(channel.id))
        return
      else:
        await message.channel.send("You don't have permission to do that. Only members with the administrator permission can set up the bot")
        return
    except:
      if message.author.top_role.permissions.administrator:
        await message.channel.send("Make sure to tag the channel correctly in order to set it up.")
        return
      else:
        await message.channel.send("You don't have permission to do that. Only members with the administrator permission can set up the bot")
        return
  
  if msg.startswith("//channel disable "):
    if message.author.top_role.permissions.administrator:
      msg = msg.split("//channel disable <#", 1)[1]
      msg = msg.split(">", 1)[0]
      for index, channel in enumerate(db["ChannelID"]):
        if msg == str(channel):
          await message.channel.send("This channel will no longer receive daily Guardian Games updates.")
          del db["ChannelID"][index]
          print("Channel removed " + str(channel))
          return
      return
    else:
      await message.channel.send("You don't have permission to do that. Only members with the administrator permission can set up the bot")
  
  if msg.startswith("//help"):
    await message.channel.send("These are the commands you can use:\n//leaderboard: Returns the current leaderboard for the event.\n//results: Shows the results from the previous day.\n//modifiers: Shows the daily Strike modifiers for each class on the Guardian Games Strike playlist.\n//setup: This will give you instructions on how to set up the bot.")
    return
      
  
  if message.author.id == 170867461040635904:
    if msg.startswith("//results "):

      resultsmessage = ""

      titangold = db["Tgold"]
      warlockgold = db["Wgold"]
      huntergold = db["Hgold"]

      titansilver = db["Tsilver"]
      warlocksilver = db["Wsilver"]
      huntersilver = db["Hsilver"]

      titanbronze = db["Tbronze"]
      warlockbronze = db["Wbronze"]
      hunterbronze = db["Hbronze"]

      titanscore = db["Titans"]
      warlockscore = db["Warlocks"]
      hunterscore = db["Hunters"]

      msg = msg.split("//results ", 1)[1]
      db["firstplace"] = msg.split(", ", 1)[0]
      if msg.split(", ", 1)[0] == "Titans":
        titangold = titangold + 1
        titanscore = titanscore + 3
        db["Titans"] = titanscore
        db["Tgold"] = titangold

      elif msg.split(", ", 1)[0] == "Warlocks":
        warlockgold = warlockgold + 1
        warlockscore = warlockscore + 3
        db["Warlocks"] = warlockscore
        db["Wgold"] = warlockgold

      else:
        huntergold = huntergold + 1
        hunterscore = hunterscore + 3
        db["Hunters"] = hunterscore
        db["Hgold"] = huntergold

      msg = msg.split(", ", 1)[1]

      db["secondplace"] = msg.split(", ", 1)[0]
      if msg.split(", ", 1)[0] == "Titans":
        titansilver = titansilver + 1
        titanscore = titanscore + 2
        db["Titans"] = titanscore
        db["Tsilver"] = titansilver

      elif msg.split(", ", 1)[0] == "Warlocks":
        warlocksilver = warlocksilver + 1
        warlockscore = warlockscore + 2
        db["Warlocks"] = warlockscore
        db["Wsilver"] = warlocksilver

      else:
        huntersilver = huntersilver + 1
        hunterscore = hunterscore + 2
        db["Hunters"] = hunterscore
        db["Hsilver"] = huntersilver
      
      msg = msg.split(", ", 1)[1]
      
      db["thirdplace"] = msg
      if msg.split(", ", 1)[0] == "Titans":
        titanbronze = titanbronze + 1
        titanscore = titanscore + 1
        db["Titans"] = titanscore
        db["Tbronze"] = titanbronze

      elif msg.split(", ", 1)[0] == "Warlocks":
        warlockbronze = warlockbronze + 1
        warlockscore = warlockscore + 1
        db["Warlocks"] = warlockscore
        db["Wbronze"] = warlockbronze

      else:
        hunterbronze = hunterbronze + 1
        hunterscore = hunterscore + 1
        db["Hunters"] = hunterscore
        db["Hbronze"] = hunterbronze

      Scores = [titanscore, warlockscore, hunterscore]
      Scores = sorted(Scores)
      Standings = []
      if Scores[0] == titanscore:
        Standings.append("T")
      if Scores[0] == warlockscore:
        Standings.append("W")
      if Scores[0] == hunterscore:
        Standings.append("H")
      
      if Scores[1] == titanscore:
        Standings.append("T")
      if Scores[1] == warlockscore:
        Standings.append("W")
      if Scores[1] == hunterscore:
        Standings.append("H")

      if Scores[2] == titanscore:
        Standings.append("T")
      if Scores[2] == warlockscore:
        Standings.append("W")
      if Scores[2] == hunterscore:
        Standings.append("H")

      
      resultsmessage = resultsmessage + ("Today's final standings are as follows\n\n:first_place:: **" + db["firstplace"] + "**\n:second_place:: **" + 
      db["secondplace"] + "**\n:third_place:: **" + db["thirdplace"] + "**\n\n" +
      "Don't worry " + db["thirdplace"] + "! You'll get a 10% boost for the remainder of the event!\n\n"
      + "The current leaderboard is as follows:\n")

      titanset = False
      warlockset = False
      hunterset = False

      if Scores[2] == titanscore and titanset == False:
        resultsmessage = resultsmessage + ("Titans:\n:first_place:" + str(titangold) + " :second_place:" + str(titansilver) + " :third_place:" + str(titanbronze))
        titanset = True
      elif Scores[2] == warlockscore and warlockset == False:
        resultsmessage = resultsmessage + ("Warlocks:\n:first_place:" + str(warlockgold) + " :second_place:" + str(warlocksilver) + " :third_place:" + str(warlockbronze))
        warlockset = True
      elif Scores[2] == hunterscore and hunterset == False:
        resultsmessage = resultsmessage + ("Hunters:\n:first_place:" + str(huntergold) + " :second_place:" + str(huntersilver) + " :third_place:" + str(hunterbronze))
        hunterset = True

      if Scores[1] == titanscore and titanset == False:
        resultsmessage = resultsmessage + ("\nTitans:\n:first_place:" + str(titangold) + " :second_place:" + str(titansilver) + " :third_place:" + str(titanbronze))
        titanset = True
      elif Scores[1] == warlockscore and warlockset == False:
        resultsmessage = resultsmessage + ("\nWarlocks:\n:first_place:" + str(warlockgold) + " :second_place:" + str(warlocksilver) + " :third_place:" + str(warlockbronze))
        warlockset = True
      elif Scores[1] == hunterscore and hunterset == False:
        resultsmessage = resultsmessage + ("\nHunters:\n:first_place:" + str(huntergold) + " :second_place:" + str(huntersilver) + " :third_place:" + str(hunterbronze))
        hunterset = False

      if Scores[0] == titanscore and titanset == False:
        resultsmessage = resultsmessage + ("\nTitans:\n:first_place:" + str(titangold) + " :second_place:" + str(titansilver) + " :third_place:" + str(titanbronze))
        titanset = True
      elif Scores[0] == warlockscore and warlockset == False:
        resultsmessage = resultsmessage + ("\nWarlocks:\n:first_place:" + str(warlockgold) + " :second_place:" + str(warlocksilver) + " :third_place:" + str(warlockbronze))
        warlockset = True
      elif Scores[0] == hunterscore and hunterset == False:
        resultsmessage = resultsmessage + ("\nHunters:\n:first_place:" + str(huntergold) + " :second_place:" + str(huntersilver) + " :third_place:" + str(hunterbronze))
        hunterset = False

      resultsmessage = resultsmessage + ("\n\nCurrent boosts:\nTitans: "+ str(titanbronze * 10) + "%\nWarlocks: " + str(warlockbronze * 10) + "%\nHunters: " + str(hunterbronze * 10) + "%")

      goldmodifier = "-Health, shields, and recovery are increased.\n-Kinetic weapons deal more damage."
      silvermodifier = "-Melee abilities recharge faster.\n-Elemental damage increased from Guardian sources.\n-More Heavy ammo available."
      bronzemodifier = "-Grenade abilities deal more damage and recharge much faster.\n-Elemental damage increased from Guardian sources."

      titan3rd = "-Combatant melee attacks deal more damage."
      titan2nd = "-Combatant melee attacks deal significantly more damage."
      warlock3rd = "-Incoming damage increased while airborne."
      warlock2nd = "-Incoming damage significantly increased while airborne."
      hunter3rd = "-Radar is disabled."
      hunter2nd = "-Radar is disabled and combatants don't flinch when damaged."

      resultsmessage = resultsmessage + "\n\nYour daily strike modifiers are as follows:\n**Titans:**\n"

      if db["firstplace"] == "Titans":
        resultsmessage = resultsmessage + goldmodifier

        if db["secondplace"] == "Warlocks":
          resultsmessage = resultsmessage + ("\n" + warlock2nd + "\n" + hunter3rd)
        else:
          resultsmessage = resultsmessage + ("\n" + hunter2nd + "\n" + warlock3rd)

      elif db["secondplace"] == "Titans":
        resultsmessage = resultsmessage + silvermodifier

        if db["thirdplace"] == "Warlocks":
          resultsmessage = resultsmessage + ("\n" + warlock3rd)
        else:
          resultsmessage = resultsmessage + ("\n" + hunter3rd)
      
      elif db["thirdplace"] == "Titans":
        resultsmessage = resultsmessage + bronzemodifier


      resultsmessage = resultsmessage + ("\n\n**Warlocks:**\n")

      
      if db["firstplace"] == "Warlocks":
        resultsmessage = resultsmessage + goldmodifier

        if db["secondplace"] == "Titans":
          resultsmessage = resultsmessage + ("\n" + titan2nd + "\n" + hunter3rd)
        else:
          resultsmessage = resultsmessage + ("\n" + hunter2nd + "\n" + titan3rd)

      if db["secondplace"] == "Warlocks":
        resultsmessage = resultsmessage + silvermodifier

        if db["thirdplace"] == "Titans":
          resultsmessage = resultsmessage + ("\n" + titan3rd)
        else:
          resultsmessage = resultsmessage + ("\n" + hunter3rd)

      if db["thirdplace"] == "Warlocks":
        resultsmessage = resultsmessage + bronzemodifier

      
      resultsmessage = resultsmessage + ("\n\n**Hunters:**\n")

      
      if db["firstplace"] == "Hunters":
        resultsmessage = resultsmessage + goldmodifier

        if db["secondplace"] == "Titans":
          resultsmessage = resultsmessage + ("\n" + titan2nd + "\n" + warlock3rd)
        else:
          resultsmessage = resultsmessage + ("\n" + warlock2nd + "\n" + titan3rd)

      if db["secondplace"] == "Hunters":
        resultsmessage = resultsmessage + silvermodifier

        if db["thirdplace"] == "Titans":
          resultsmessage = resultsmessage + ("\n" + titan3rd)
        else:
          resultsmessage = resultsmessage + ("\n" + warlock3rd)

      if db["thirdplace"] == "Hunters":
        resultsmessage = resultsmessage + bronzemodifier

      db["resultsmessage"] = resultsmessage
      return
    
    if msg.startswith ("//push all"):
      for guild in client.guilds:
        for channel in guild.text_channels:
          for id in db["ChannelID"]:
            if id == channel.id:
              try:
                await channel.send(db["resultsmessage"])
                await message.channel.send("Message sent")
              except:
                await message.channel.send("Message failed")
      
      for guild in client.guilds:
        for role in guild.roles:
          try:
            if str(role.name) == (db["firstplace"][:-1]):
              await role.edit(color=0xFFD700)
            if str(role.name) == (db["secondplace"][:-1]):
              await role.edit(color=0xC0C0C0)
            if str(role.name) == (db["thirdplace"][:-1]):
              await role.edit(color=0xCD7F32)
          except:
                await message.channel.send("Role change failed")
          

    if msg.startswith("//onlypushhere"):
      await message.channel.send(db["resultsmessage"])
      return
    
    if msg.startswith("//pushmessage "):
      for guild in client.guilds:
        for channel in guild.text_channels:
          for id in db["ChannelID"]:
            if id == channel.id:
              try:
                await channel.send(msg.split("//pushmessage ", 1)[1])
                await message.channel.send("Message sent")
              except:
                await message.channel.send("Message failed")
      


    if msg.startswith("//reset"):
      db["firstplace"] = ""
      db["secondplace"] = ""
      db["thirdplace"] = ""
      db["Titans"] = 0
      db["Warlocks"] = 0
      db["Hunters"] = 0
      db["Tgold"] = 0
      db["Tsilver"] = 0
      db["Tbronze"] = 0
      db["Wgold"] = 0
      db["Wsilver"] = 0
      db["Wbronze"] = 0
      db["Hgold"] = 0
      db["Hsilver"] = 0
      db["Hbronze"] = 0
      return
    
    if msg.startswith("//roleupdate"):
      for guild in client.guilds:
        for role in guild.roles:
          try:
            if str(role.name) == (db["firstplace"][:-1]):
              await role.edit(color=0xFFD700)
              print("Role Update Success")
            if str(role.name) == (db["secondplace"][:-1]):
              await role.edit(color=0xC0C0C0)
              print("Role Update Success")
            if str(role.name) == (db["thirdplace"][:-1]):
              await role.edit(color=0xCD7F32)
              print("Role Update Success")
            
          except:
                print("Role Update Failed")
  
  if msg.startswith("//leaderboard"):
    resultsmessage = "**__Guardian Games 2021 Leaderboard:__**\n\n"
    titanset = False
    warlockset = False
    hunterset = False
    titanscore = db["Titans"]
    warlockscore = db["Warlocks"]
    hunterscore = db["Hunters"]
    titangold = db["Tgold"]
    titansilver = db["Tsilver"]
    titanbronze = db["Tbronze"]
    warlockgold = db["Wgold"]
    warlocksilver = db["Wsilver"]
    warlockbronze = db["Wbronze"]
    huntergold = db["Hgold"]
    huntersilver = db["Hsilver"]
    hunterbronze = db["Hbronze"]

    Scores = [titanscore, warlockscore, hunterscore]
    Scores = sorted(Scores)
    Standings = []
    if Scores[0] == titanscore:
      Standings.append("T")
    if Scores[0] == warlockscore:
      Standings.append("W")
    if Scores[0] == hunterscore:
      Standings.append("H")
      
    if Scores[1] == titanscore:
      Standings.append("T")
    if Scores[1] == warlockscore:
      Standings.append("W")
    if Scores[1] == hunterscore:
      Standings.append("H")

    if Scores[2] == titanscore:
      Standings.append("T")
    if Scores[2] == warlockscore:
      Standings.append("W")
    if Scores[2] == hunterscore:
      Standings.append("H")
    

    if Scores[2] == titanscore and titanset == False:
        resultsmessage = resultsmessage + ("Titans:\n:first_place:" + str(titangold) + " :second_place:" + str(titansilver) + " :third_place:" + str(titanbronze))
        titanset = True
    elif Scores[2] == warlockscore and warlockset == False:
        resultsmessage = resultsmessage + ("Warlocks:\n:first_place:" + str(warlockgold) + " :second_place:" + str(warlocksilver) + " :third_place:" + str(warlockbronze))
        warlockset = True
    elif Scores[2] == hunterscore and hunterset == False:
        resultsmessage = resultsmessage + ("Hunters:\n:first_place:" + str(huntergold) + " :second_place:" + str(huntersilver) + " :third_place:" + str(hunterbronze))
        hunterset = True

    if Scores[1] == titanscore and titanset == False:
        resultsmessage = resultsmessage + ("\nTitans:\n:first_place:" + str(titangold) + " :second_place:" + str(titansilver) + " :third_place:" + str(titanbronze))
        titanset = True
    elif Scores[1] == warlockscore and warlockset == False:
        resultsmessage = resultsmessage + ("\nWarlocks:\n:first_place:" + str(warlockgold) + " :second_place:" + str(warlocksilver) + " :third_place:" + str(warlockbronze))
        warlockset = True
    elif Scores[1] == hunterscore and hunterset == False:
        resultsmessage = resultsmessage + ("\nHunters:\n:first_place:" + str(huntergold) + " :second_place:" + str(huntersilver) + " :third_place:" + str(hunterbronze))
        hunterset = False

    if Scores[0] == titanscore and titanset == False:
        resultsmessage = resultsmessage + ("\nTitans:\n:first_place:" + str(titangold) + " :second_place:" + str(titansilver) + " :third_place:" + str(titanbronze))
        titanset = True
    elif Scores[0] == warlockscore and warlockset == False:
        resultsmessage = resultsmessage + ("\nWarlocks:\n:first_place:" + str(warlockgold) + " :second_place:" + str(warlocksilver) + " :third_place:" + str(warlockbronze))
        warlockset = True
    elif Scores[0] == hunterscore and hunterset == False:
        resultsmessage = resultsmessage + ("\nHunters:\n:first_place:" + str(huntergold) + " :second_place:" + str(huntersilver) + " :third_place:" + str(hunterbronze))
        hunterset = False

    await message.channel.send(resultsmessage)
    return
  
  if msg.startswith("//modifiers"):
      resultsmessage = ""
      #await message.channel.send("The first day of Guardian Games hasn't ended, so there are no daily modifiers yet. Be patient Guardian!")

      goldmodifier = "-Health, shields, and recovery are increased\n-Kinetic weapons deal more damage."
      silvermodifier = "-Melee abilities recharge faster.\n-Elemental damage increased from Guardian sources.\n-More Heavy ammo available."
      bronzemodifier = "-Grenade abilities deal more damage and recharge much faster.\n-Elemental damage increased from Guardian sources."

      titan3rd = "-Combatant melee attacks deal more damage."
      titan2nd = "-Combatant melee attacks deal significantly more damage."
      warlock3rd = "-Incoming damage increased while airborne."
      warlock2nd = "-Incoming damage significantly increased while airborne."
      hunter3rd = "-Radar is disabled."
      hunter2nd = "-Radar is disabled and combatants don't flinch when damaged."

      resultsmessage = resultsmessage + "\n\nYour daily strike modifiers are as follows:\n**Titans:**\n"

      if db["firstplace"] == "Titans":
        resultsmessage = resultsmessage + goldmodifier

        if db["secondplace"] == "Warlocks":
          resultsmessage = resultsmessage + ("\n" + warlock2nd + "\n" + hunter3rd)
        else:
          resultsmessage = resultsmessage + ("\n" + hunter2nd + "\n" + warlock3rd)

      elif db["secondplace"] == "Titans":
        resultsmessage = resultsmessage + silvermodifier

        if db["thirdplace"] == "Warlocks":
          resultsmessage = resultsmessage + ("\n" + warlock3rd)
        else:
          resultsmessage = resultsmessage + ("\n" + hunter3rd)
      
      elif db["thirdplace"] == "Titans":
        resultsmessage = resultsmessage + bronzemodifier


      resultsmessage = resultsmessage + ("\n\n**Warlocks:**\n")

      
      if db["firstplace"] == "Warlocks":
        resultsmessage = resultsmessage + goldmodifier

        if db["secondplace"] == "Titans":
          resultsmessage = resultsmessage + ("\n" + titan2nd + "\n" + hunter3rd)
        else:
          resultsmessage = resultsmessage + ("\n" + hunter2nd + "\n" + titan3rd)

      if db["secondplace"] == "Warlocks":
        resultsmessage = resultsmessage + silvermodifier

        if db["thirdplace"] == "Titans":
          resultsmessage = resultsmessage + ("\n" + titan3rd)
        else:
          resultsmessage = resultsmessage + ("\n" + hunter3rd)

      if db["thirdplace"] == "Warlocks":
        resultsmessage = resultsmessage + bronzemodifier

      
      resultsmessage = resultsmessage + ("\n\n**Hunters:**\n")

      
      if db["firstplace"] == "Hunters":
        resultsmessage = resultsmessage + goldmodifier

        if db["secondplace"] == "Titans":
          resultsmessage = resultsmessage + ("\n" + titan2nd + "\n" + warlock3rd)
        else:
          resultsmessage = resultsmessage + ("\n" + warlock2nd + "\n" + titan3rd)

      if db["secondplace"] == "Hunters":
        resultsmessage = resultsmessage + silvermodifier

        if db["thirdplace"] == "Titans":
          resultsmessage = resultsmessage + ("\n" + titan3rd)
        else:
          resultsmessage = resultsmessage + ("\n" + warlock3rd)

      if db["thirdplace"] == "Hunters":
        resultsmessage = resultsmessage + bronzemodifier
      
      await message.channel.send(resultsmessage)
      return
  
  if msg.startswith("//results"):
    await message.channel.send("Yesterday's final standings were as follows:\n\n:first_place:: **" + db["firstplace"] + "**\n:second_place:: **" + 
    db["secondplace"] + "**\n:third_place:: **" + db["thirdplace"] + "**")
    return
      


keep_alive()
client.run(os.getenv('TOKEN'))