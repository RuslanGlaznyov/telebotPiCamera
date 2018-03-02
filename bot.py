import telebot
import traceback
import time
from telebot import types
import const
from log import log





#markup = types.InlineKeyboardMarkup(row_width=2)
#itembtna = types.InlineKeyboardButton(text ='a',callback_data='a')
#itembtnv = types.InlineKeyboardButton(text ='v',callback_data='v')
#itembtnc = types.InlineKeyboardButton(text= 'c',callback_data='c')
#markup.add(itembtna, itembtnv, itembtnv)
#bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)



bot = telebot.TeleBot(const.token)

@bot.message_handler(content_types=['text'])
def handle_start(message):
	if message.from_user.id in const.id_access:
		if message.text == '/start'	or message.text == '/update':
			gui = telebot.types.ReplyKeyboardMarkup(True)
			gui.row('/update', 'take a picture', '/stop')
			gui.row('/log','/clear_log')
			bot.send_message(message.from_user.id,"Always at your service", reply_markup=gui)




		elif message.text =='/log':
			handle_getlog(message)
		elif message.text == '/clear_log':
			handle_clear_log(message)
		elif message.text == 'take a picture':
			handle_photo(message)

	else:
		log(message)
		if message.text == '/start' or message.text == '/update':
			bot.send_message(message.from_user.id, 'Access is denied')


#@bot.message_handler(commands=['log'])
def handle_getlog(message):
	with open(const.log_file_path, 'rb') as file:
		bot.send_chat_action(message.from_user.id, 'upload_document')
		bot.send_document(message.chat.id, file)

#@bot.message_handler(commands=['clear_log'])
def handle_clear_log(message):
	with open(const.log_file_path,'w') as file:
		file.write(" ")
	bot.send_message(message.chat.id, 'log file cleaned')

#@bot.message_handler(content_types=['text'])
def handle_photo(message):
	if message.text == 'take a picture':
		with open(const.photo_path, 'rb') as img:
			bot.send_chat_action(message.from_user.id, 'upload_photo')
			bot.send_photo(message.chat.id, img,'room photo')

def telegram_polling():
    try:
        bot.polling(none_stop=True) #constantly get messages from Telegram
    except:
        # traceback_error_string=traceback.format_exc()
        # with open(const.error_file_path, "a") as myfile:
        #     myfile.write("\r\n\r\n" + time.strftime("%c")+"\r\n<<ERROR polling>>\r\n"+ traceback_error_string + "\r\n<<ERROR polling>>")
        bot.stop_polling()
        time.sleep(10)
        telegram_polling()

if __name__ == '__main__':
    telegram_polling()

