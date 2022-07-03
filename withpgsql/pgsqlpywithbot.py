import psycopg2
import telebot
from scrapper import scrap


bot_token = "5333091432:AAEE-MtnYqdrHo1N09LRBHIFW_BexsCs2pQ"
bot = telebot.TeleBot(bot_token)
parse_mode='MARKDOWN'

@bot.message_handler(commands=['start'])
def greet(message): 
 conn = psycopg2.connect(database="testdb_bot", user = "postgres", password = "pgSQLbyME_09", host = "127.0.0.1", port = "5432")
 cur = conn.cursor()
 cidstr=str(message.chat.id)
 print(type(message.chat.id))
 @bot.message_handler(commands=['BTech'])
 @bot.message_handler(commands=['S6'])
 cur.execute("INSERT INTO BTECH_DEMO(CID,SEM,PRGM)  VALUES (%s,%s,%s)",(cidstr,'S6','BTech'))
 conn.commit()
 conn.close()
 bot.send_message(message.chat.id,"*Welcome to\nKTU Personal Updates Bot*",parse_mode)

msg=scrap()  
print(msg)

@bot.message_handler(commands=['new'])
def sendMessage(message):
 conn = psycopg2.connect(database="testdb_bot", user = "postgres", password = "pgSQLbyME_09", host = "127.0.0.1", port = "5432")
 cur = conn.cursor()
 cur.execute("SELECT CID FROM BTECH_DEMO")
 rows=cur.fetchall()
 for row in rows:
  print ("Chat_id : ",row,"\n")
  bot.send_message(row, msg,parse_mode)
 conn.close()
 

bot.polling()
