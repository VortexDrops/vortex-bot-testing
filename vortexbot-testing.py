import discord
import asyncio
import requests
from bs4 import BeautifulSoup
import json
import os



token = str(os.environ.get("BOT_TOKEN"))
vortex_server_id = str(os.environ.get("VORTEX_SERVER_ID"))
vortex_user_id = str(os.environ.get("VORTEX_USER_ID"))
get_url = str(os.environ.get("GET_URL"))

str_key_1 = str(os.environ.get("STR_KEY_1"))
str_key_2 = str(os.environ.get("STR_KEY_2"))
str_key_3 = str(os.environ.get("STR_KEY_3"))
str_key_4 = str(os.environ.get("STR_KEY_4"))

str_message_1 = str(os.environ.get("STR_MESSAGE_1"))
 


bot = discord.Client()

@bot.event
async def on_ready():

  global vortex_server_id
  global vortex_user_id

  global get_url
  global str_key_1
  global str_key_2
  global str_key_3
  global str_key_4
  global str_message_1

  await bot.wait_until_ready()
  print (bot.user.name + " is ready")
  print ("ID: " + bot.user.id)

  while True:
    await asyncio.sleep(60)
    
    r = requests.get(get_url)
    soup = BeautifulSoup(r.text, "html.parser")
    first = str(soup.find_all("script")[3])
    second = first[20:-15].strip()
    third = second[22:-1].strip()
    info = json.loads(third)
    
    if (int(info[str_key_1][str_key_2]) > 0) and (str_key_4 in info[str_key_1][str_key_3]):
      print("Sent")
      await bot.send_message(bot.get_server(vortex_server_id).get_member(vortex_user_id), str_message_1)


bot.run(token)
