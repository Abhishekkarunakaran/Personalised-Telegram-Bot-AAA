import telebot
from scrapper import scrap

bot_token = "5333091432:AAEE-MtnYqdrHo1N09LRBHIFW_BexsCs2pQ"
bot = telebot.TeleBot(bot_token)
parse_mode='MARKDOWN'

@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id,"*Welcome to\nKTU Personal Updates Bot*",parse_mode)
 
@bot.message_handler(commands=['new'])
def sendMessage(message):
  msg=scrap()  
  print(msg)
  bot.send_message(message.chat.id, msg,parse_mode)

bot.polling()

