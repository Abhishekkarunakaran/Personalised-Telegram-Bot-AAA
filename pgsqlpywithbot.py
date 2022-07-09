# import psycopg2
# import telebot
# from scrapper import scrap
# from filtration import filt


# bot_token = "5333091432:AAEE-MtnYqdrHo1N09LRBHIFW_BexsCs2pQ"
# bot = telebot.TeleBot(bot_token)
# parse_mode='MARKDOWN'

# @bot.message_handler(commands=['start'])
# def greet(message): 
#  conn = psycopg2.connect(database="testdb_bot", user = "postgres", password = "pgSQLbyME_09", host = "127.0.0.1", port = "5432")
#  cur = conn.cursor()
#  cidstr=str(message.chat.id)
#  print(type(message.chat.id))
#  conn.commit()
#  conn.close()
#  bot.send_message(message.chat.id,"*Welcome to\nKTU Personal Updates Bot*",parse_mode)

# msg=scrap()  
# print(msg)

# @bot.message_handler(commands=['new'])
# def sendMessage(message):
#  conn = psycopg2.connect(database="testdb_bot", user = "postgres", password = "pgSQLbyME_09", host = "127.0.0.1", port = "5432")
#  cur = conn.cursor()
#  prgm,sem=filt(content[0].b.text)
#  cur.execute("SELECT CID FROM BTECH_DEMO WHERE PRGM=%s AND SEM=%s",(prgm,sem))
#  rows=cur.fetchall()
#  for row in rows:
#   print ("Chat_id : ",row,"\n")
#   bot.send_message(row, msg,parse_mode)
#  conn.close()
 

# bot.polling()
