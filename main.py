# import requests
# from bs4 import BeautifulSoup
# import json
import telebot
from scrapper import scrap
import threading
from time import sleep


delay = 900  #15 mins in seconds


bot_token = "5333091432:AAEE-MtnYqdrHo1N09LRBHIFW_BexsCs2pQ"


chat_id = ["865161907", "722830299", "735059361"]

prgm =  "*Choose your Programme*\n/B.Tech\n/B.Arch\n/MCA\n/M.Tech"

sem_btech = "*Choose current semester*\n/S2\n/S4\n/S6\nS8"

bot = telebot.TeleBot(bot_token)
parse_mode='MARKDOWN'

p_m = 'HTML'
@bot.message_handler(commands=['start'])
def greet(message):
  bot.send_message(message.chat.id,"*Welcome to\nKTU Personal Updates Bot*",parse_mode)
  bot.send_message(message.chat.id,prgm,parse_mode)
  
@bot.message_handler(commands=['new'])
def sendMessage(message):
  msg=scrap()
  bot.send_message(message.chat.id, msg,parse_mode)

@bot.message_handler(commands=['hi'])
def hello(message):
  print(message.chat.first_name+'\n'+message.chat.last_name)


  # bot.send_message(message.chat.id)
# @bot.message_handler(commands=['S2'])
# def sendMessage(message):
  # msg=scrap()
  # bot.send_message(message.chat.id,sem_btech,parse_mode)

# This needs any message ######### 
# def scrapper(message):
#   return True

# @bot.message_handler(func=scrapper)
# def send(message):
#   bot.send_message(message. chat.id,msg,'MARKDOWN')
###############################S###
relevent_id = []

def main():
    bot.polling() # looking for message
  
    def check_notification():
      while True:
        msg,new_notif,relevent_id=scrap()
        if new_notif:
          for id in relevent_id:
            bot.send_message(id,msg)
        sleep(delay)
  
    t = threading.Thread(target=check_notification)
    t.start()

if __name__ == '__main__':
    main() 