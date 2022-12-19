import os
import telebot
from telebot import types

# Токент бота
TOKEN = '5831717051:AAEJRBcd34qChYM3xylMF5f10p7WZBp4NKg'

# Сообщения
mes_1 = 'Пн'
mes_2 = 'Вт'
mes_3 = 'Ср'
mes_4 = 'Чт'
mes_5 = 'Пт'
mes_6 = 'Сб'

# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))

# Создание бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	# Идентификатор диалога
	chat_id = message.chat.id

	# Текст, введенный пользователем, то есть текст с кнопки
	text = message.text
	
	# Проверка сообщения и вывод данных
	if text==mes_1:
		img = open(os.path.join(cur_path, 'img\photo_1.jpg'), 'rb')
		bot.send_photo(chat_id, img)
		
	elif text==mes_2:
		img = open(os.path.join(cur_path, 'img\photo_2.jpg'), 'rb')
		bot.send_photo(chat_id, img)

	elif text==mes_3:
		img = open(os.path.join(cur_path, 'img\photo_3.jpg'), 'rb')
		bot.send_photo(chat_id, img)

	elif text==mes_4:
		img = open(os.path.join(cur_path, 'img\photo_4.jpg'), 'rb')
		bot.send_photo(chat_id, img)

	elif text==mes_5:
		img = open(os.path.join(cur_path, 'img\photo_5.jpg'), 'rb')
		bot.send_photo(chat_id, img)

	elif text==mes_6:
		img = open(os.path.join(cur_path, 'img\photo_6.jpg'), 'rb')
		bot.send_photo(chat_id, img)
	
	else:
		markup = types.ReplyKeyboardMarkup()
		itembtn1 = types.KeyboardButton(mes_1)
		itembtn2 = types.KeyboardButton(mes_2)
		itembtn3 = types.KeyboardButton(mes_3)
		itembtn4 = types.KeyboardButton(mes_4)
		itembtn5 = types.KeyboardButton(mes_5)
		itembtn6 = types.KeyboardButton(mes_6)
		markup.add(itembtn1, itembtn2, itembtn3)
		markup.add(itembtn4, itembtn5, itembtn6)
		bot.send_message(chat_id, 'Пожалуйста, нажмите кнопку', reply_markup=markup)

bot.infinity_polling()
