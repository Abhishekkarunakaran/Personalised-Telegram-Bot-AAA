# import requests
# from bs4 import BeautifulSoup
# import json
import telebot
from scrapper import scrap
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot_token = "5333091432:AAEE-MtnYqdrHo1N09LRBHIFW_BexsCs2pQ"

chat_id = ["865161907", "722830299", "735059361"]

# prgm=  "*Choose your Programme*\n/B.Tech\n/B.Arch\n/MCA\n/M.Tech"

# sem_btech = ""

bot = telebot.TeleBot(bot_token)
parse_mode = 'MARKDOWN'


@bot.message_handler(commands=['new'])
def sendMessage(message):
    msg = scrap()
    bot.send_message(message.chat.id, msg, parse_mode)


# A new feature :-
# When a use enters a number 'n'
# then the scrapper scrapes the n-th notification


@bot.message_handler(content_types=['text'])
def nthNotif(message):
    print(message.text)
    msg = scrap(int(message.text) - 1)
    bot.send_message(message.chat.id, msg, parse_mode)


# This needs any message #########
# def scrapper(message):
#   return True

# @bot.message_handler(func=scrapper)
# def send(message):
#   bot.send_message(message. chat.id,msg,'MARKDOWN')
##################################

#InlineKeyboard


def prg_Markup():
    markup = InlineKeyboardMarkup()
    markup.width = 2
    markup.add(
        InlineKeyboardButton("B.Tech", callback_data="B.Tech"),
        InlineKeyboardButton("B.Arch", callback_data="B.Arch"),
        InlineKeyboardButton("B.Des", callback_data="B.Des"),
        InlineKeyboardButton("M.Tech", callback_data="M.Tech"),
        InlineKeyboardButton("MCA", callback_data="MCA"),
        InlineKeyboardButton("M.Arch", callback_data="M.Arch"),
        InlineKeyboardButton("MBA", callback_data="MBA"),
    )
    return markup


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, "*Welcome to\nKTU Personal Updates Bot*",
                     parse_mode)
    bot.send_message(message.chat.id,
                     "Select your program",
                     reply_markup=prg_Markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print(call.data)


def main():
    bot.polling()


if __name__ == '__main__':
    main()
