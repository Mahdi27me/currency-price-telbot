from posixpath import split
import threading
import requests
import pyrogram
from pyrogram import Client, idle,filters
from time import sleep
import time
from random import randrange
#ip and hash
api_id = 12345
api_hash = ''
bot_token=''
#Bitcoin price part
def getbtc():
   url=''
   price_btc=requests.get(url)
   data=price_btc.json()
   return data["bpi"]["USD"]['rate']
name_call_btc=['btc','bitcoin','Btc','BTC']
#BINANCE PART
def price(symbol):
    try:
        url = f'https://api.binance.com/api/v3/ticker/price'
        parm= {"symbol" : symbol}
        req = requests.get(url,parm).json()
        return req['price']
    except:
        return False
#Part price in dollars
def getusd():
   url2=''
   price_usd=requests.get(url2)
   info_usd=price_usd.json()
   return info_usd['usd_buy']['value']
usd_call=['DOLLAR','DOLAR','USDT']
#bot AND message
bot = Client('testbot',api_id,api_hash)
@bot.on_message(filters.command("start"))
async def first_info(Client,message):
   await message.reply("Hello\U0001f60A you can ask me the price of Crypto currency\U0001f4b0 For example:BTC, ADA, SOL,...... ")
#TODO{{{{{{{{{{{..........}}}}}}}}}}}
@bot.on_message()
async def currency(Client, message):
   #USDT PART 
   if message.text:
      if message.text.upper() in usd_call:
         await message.reply(f"The price of USA Dollar at this moment: {getusd()}  TOMAN Have an Energetic Day\U000026A1") 
      #calculator USD part
         price_dolar=getusd()
         conversion_usd=message.text.split()
         if len(conversion_usd)==2:
            conversion_usd[0] =float(conversion_usd[0])
            if conversion_usd[1].upper() in usd_call:
               dolar_user=float(conversion_usd[0])
               final_price=float(price_dolar)*dolar_user
               await message.reply(f"{dolar_user} dollars is {final_price} Toman Have an Energetic Day\U000026A1")
   #CURRENCY PART
   req = price(message.text.upper()+"USDT")
   if req != False :
      await message.reply(f"the price of { message.text.upper()} at this moment:{req} \U0001f4b0"+ "Have an Energetic Day\U000026A1")        
def timer():
   bot.send_message(-1001447251721,"Hello\U0001F60A Bitcoin: "+ getbtc()+ "\U0001F4b0"+"USA Dollar:"+ getusd()+' TOMAN' +' Have an Energetic Day\U000026A1')
def looper():
   timer()
   threading.Timer(86400,looper).start()
bot.start()
looper()
idle()
bot.stop()
