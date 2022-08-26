# from concurrent.futures import thread

import os

try:
   from time import sleep
   import discord
   from discord.ext import commands
   import requests
   from datetime import datetime
   

   intents = discord.Intents.default() #Create an instance of a Client. This client is our connection to Discord.
   intents.message_content = True
   bot = commands.Bot(command_prefix="#",intents=intents)


   def giveMeTime(letter):
      req = requests.get("https://timeapi.io/api/Time/current/zone?timeZone=Asia/Riyadh").json()
      return req[letter]

   @bot.event
   async def on_ready():
      await times()

   def athkar(letter):
      thkr=requests.get(f"https://azkar-api.nawafhq.repl.co/zekr?{letter}&json").json()
      x=str(thkr["content"])
      return x

   async def sleepp(): # اذكار قبل النوم
      channel = bot.get_channel(channelId)
      thkr=athkar("bs")
      await channel.send(thkr)
      channel = bot.get_channel(channelId)
      await channel.send(thkr)
      
   async def Massa():
      channel = bot.get_channel(channelId)
      thkr=athkar("e")
      await channel.send(thkr)
      channel = bot.get_channel(channelId)
      await channel.send(thkr)
      
            
   async def Morning():
      print("in morning")
      channel = bot.get_channel(channelId)
      thkr=athkar("m")
      await channel.send(thkr)
      channel = bot.get_channel(channelId)
      await channel.send(thkr)

   async def Pray(h,m,p):
   
      channel = bot.get_channel(channelId)
      if(h==4 and m==00 and p=="AM"):
         await channel.send("حان وقت صلاة الفجر")
         sleep(900)
         await channel.send(athkar("as"))
      
      elif(h==11 and m==45 and p=="AM"):
         await channel.send("حان وقت صلاة الظهر")
         sleep(900)
         await channel.send(athkar("as"))
      
      elif(h==15 and m==15 and  p=="PM"):
         await channel.send("حان وقت صلاة العصر")
         sleep(900)
         await channel.send(athkar("as"))
      
      elif(h==18 and m==10 and p=="PM"):
         await channel.send("حان وقت صلاة المغرب")
         sleep(900)
         await channel.send(athkar("as"))
      
      elif(h==19 and m==40 and p=="PM"):
         await channel.send("حان وقت صلاة العشاء")
         sleep(900)
         await channel.send(athkar("as"))

   async def times():
      s=00
      print("I'M in times")
      try:
         while True:
         
          h=giveMeTime("hour")
          m=giveMeTime("minute")
         
          if(h>=0 and h<=11):
         
           p="AM"
          else:
            p="PM"
         
          print(h,m,s,p)
          if (h == 6 and m == 14 and p=="AM"):
            await Morning()
            sleep(60)
         
          elif h == 23 and m ==35 and p == 'PM':
            await sleepp()
            sleep(60)
         
          elif((h==4 and m==00 and p=="AM") or(h==11 and m==45 and p=="AM")or (h==15 and m==15 and p=="PM") or (h==18 and m==10 and p=="PM") or (h==19 and m==40 and p=="PM")):
            await Pray(h,m,p)
        
            sleep(60)
          elif h == 21 and m == 35 and p == 'PM':
            await sleepp()
            sleep(60)
          elif h == 16 and m == 30 and p == 'PM':
            await Massa()
            sleep(60)
          sleep(20)
          
      except Exception as e:
       async def alert():
         channel = bot.get_channel(channelId)
         await channel.send(str(e))
       await alert()

   
except:
   os.system("pip install discord")
   os.system("pip install requests")
   os.system("pip install time")
   

   

bot.run("Token")