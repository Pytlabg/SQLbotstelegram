import telebot
import sqlite3


bot = telebot.TeleBot('5594186231:AAFxJWorbJxeHCZFwGXZVAdOVa_Yt9Wd26c')

@bot.message_handler(commands=['start'])
def start (message):
    connect = sqlite3.connect('databasetest.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER 
    )""")

    connect.commit()
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id ={people_id}")
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()
    else:
        bot.send_message(message.chat.id, 'Такой пользователь уже существует')
@bot.message_handler(commands=['delete'])
def delete (message):
    pass





bot.infinity_polling()
