# import requests
# from bs4 import BeautifulSoup
# import json
import telebot



# Making a GET request
# r = requests.get('https://ktu.edu.in/eu/core/announcements.htm')

# print(r)
# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')

# # s = soup.find('div', class_='c-details')

# # content = s.find_all('li')

# s = soup.find('div', class_='c-details')
# link = s.find_all('a')
# sss = link[0].get('href').split(" ")

# # print('https://ktu.edu.in' + sss[0].strip("\r\n") +
# #       sss[len(sss) - 1].strip("\t"))
# # print(sss)
# # print('\n\n')

# # print(content[0].b.text)

bot_token = "5333091432:AAEE-MtnYqdrHo1N09LRBHIFW_BexsCs2pQ"

url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

chat_id = ["865161907", "722830299", "735059361"]
# pop = 'https://ktu.edu.in' + sss[0].strip("\r\n") + sss[len(sss)-1].strip("\t")

# msg = f'<a href={pop}><b>Notification</b></a>'
title = 'How are you?'
body = "I'm here, let figure this out together!"
link = 'www.google.com'
msg = f'*{title}*\n\n{body}\n\n[Google]({link})'


bot = telebot.TeleBot(bot_token)
parse_mode='MARKDOWN'
@bot.message_handler(commands=['start'])
def greet(message):
  bot.send_message(message.chat.id,"*Let's start!!*",parse_mode)

@bot.message_handler(commands=['hi'])
def sendMessage(message):
  print(message)
  bot.send_message(message.chat.id,msg,parse_mode)

# This needs any message
def scrapper(message):
  return True

@bot.message_handler(func=scrapper)
def send(message):
  bot.send_message('865161907','_Trial_','MARKDOWN')

bot.polling()