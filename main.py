# import requests
# from bs4 import BeautifulSoup
# import json
# import re
import json
from msilib.schema import Error
import re
import telebot
from scrapper import scrap
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot_token = "5333091432:AAEE-MtnYqdrHo1N09LRBHIFW_BexsCs2pQ"

chat_id = ["865161907", "722830299", "735059361"]


bot = telebot.TeleBot(bot_token)
parse_mode = 'MARKDOWN'


# @bot.message_handler(commands=['new'])
# def sendMessage(message):
#     msg = scrap()
#     bot.send_message(message.chat.id, msg, parse_mode)


# A new feature :-
# When a use enters a number 'n'
# then the scrapper scrapes the n-th notification


# @bot.message_handler(content_types=['text'])
# def nthNotif(message):
#     print(message.text)
#     msg = scrap(int(message.text) - 1)
#     bot.send_message(message.chat.id, msg, parse_mode)


# This needs any message #########
# def scrapper(message):
#   return True

# @bot.message_handler(func=scrapper)
# def send(message):
#   bot.send_message(message. chat.id,msg,'MARKDOWN')
##################################

#InlineKeyboard

with open('prg_sem_data.json') as json_file:
    prg_sem = json.load(json_file)

def prg_Markup():
    markup = InlineKeyboardMarkup(row_width= 3)
    button_list = [
        InlineKeyboardButton(prg, callback_data=prg) for prg in prg_sem
    ]
    markup.add(*button_list)
    return markup


def sem_Markup(sem):
    markup = InlineKeyboardMarkup(row_width = 4) 
    button_list = [
        InlineKeyboardButton("S{}".format(i), callback_data="S{}".format(i)) for i in range(1,sem+1)
    ]
    markup.add(*button_list)
    # markup.
    return markup

@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, "*Welcome to\nKTU Personal Updates Bot*",
                     parse_mode)
    bot.send_message(message.chat.id,
                     "Select your *Program*",
                     parse_mode,
                     reply_markup=prg_Markup())
   

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    
    if (call.data in prg_sem):
        #TODO: fn() - enter the chat.id and program to the db
        
        #? inst_db(call.from_user.id,call.data)

        bot.answer_callback_query(call.id,"Saved your program {}".format(call.data))
        
        try :
            bot.send_message(call.from_user.id,
                     "Select your *Semester*",
                     parse_mode,
                     reply_markup = sem_Markup(prg_sem[call.data]))
        except Exception as e:
            print(e)
            
    if(re.search("S*",call.data)):
        #TODO: fn() - enter the chat.id and sem into db

        #? updt_db(call.from_user.id,call.data)

        bot.answer_callback_query(call.id,"Saved your semester {}".format(call.data))
    
    

def main():
    bot.polling()


if __name__ == '__main__':
    main()
