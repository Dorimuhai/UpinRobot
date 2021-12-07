import random
from UpinRobot import telethn as tbot
from telethon import events

@tbot.on(events.NewMessage(pattern="/wish"))
async def wish(upin):
   if upin.is_reply:
         mm = random.randint(1,100)
         lol = await upin.get_reply_message()
         await tbot.send_message(upin.chat_id, f"**Your wish has been cast.🌈**\n\n__chance of success {mm}%__", reply_to=lol)
   if not upin.is_reply:
         mm = random.randint(1,100)
         UPIN = "https://telegra.ph/file/5a4dc8f8cc2cdb408df18.jpg"
         await tbot.send_file(upin.chat_id, UPIN,caption=f"**Your wish has been cast.🌈**\n\n__chance of success {mm}%__", reply_to=upin)
         lol = await upin.get_reply_message()
         await tbot.send_file(upin.chat_id, f"**Your wish has been cast.🌈**\n\n__chance of success {mm}%__", reply_to=lol, file=UPIN)
   if not upin.is_reply:
         mm = random.randint(1,100)
         UPIN = "https://telegra.ph/file/5a4dc8f8cc2cdb408df18.jpg"
         await tbot.send_file(upin.chat_id,f"**Your wish has been cast.🌈**\n\n__chance of success {mm}%__", reply_to=lol, file=UPIN)
         await tbot.send_file(upin.chat_id, UPIN,caption=f"**Your wish has been cast.🌈**\n__chance of success {mm}%__", reply_to=upin)
         lol = await upin.get_reply_message()
         await tbot.send_file(upin.chat_id, f"**Your wish has been cast.🌈**\n__chance of success {mm}%__", reply_to=lol)
   if not upin.is_reply:
         mm = random.randint(1,100)
         UPIN = "https://telegra.ph/file/10139851d5bf597ce8c25.jpg"
         await tbot.send_file(upin.chat_id, UPIN,caption=f"**Your wish has been cast.🌈**\n__chance of success {mm}%__", reply_to=lol,file=UPIN)

        
   
        #thanks to @h0daka for image
      #Codes by @Tamilvip008
#Kang With Else Gay
