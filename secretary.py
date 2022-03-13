from datetime import datetime
import telebot
import random
import schedule
import time
import threading

token = '5122753599:AAFV2wwbNxeDsx9PxoWVMEP8r0wWUekYuDI'
bot = telebot.TeleBot(token)
my_id = 494551640

def choose_morning_greetings():
	seed = random.randrange(0, 5)
	greetings = ['Привет, семпай!', 'Утречкаа!', 'Вставай, чорт!', 'Подъеем!!', 'Вставай, семпай!']
	return greetings[seed]

def choose_greetings():
	seed = random.randrange(0, 5)
	greetings = ['Приветик!', 'Привет, семпай!', 'Хаюшки!', 'Ку', 'Ну привет']
	return greetings[seed]

@bot.message_handler(content_types=['text', 'image'])
def message_recieved(message):
	mess = message.text
	if mess == 'Привет':
		bot.send_message(my_id, choose_greetings())
	elif mess == '/start':
		bot.send_message(my_id, 'Привет! Я твоя новая виртуальная ассистентка.')
	elif mess == 'Слава Україні!':
		bot.send_message(my_id, 'Героям Слава!')
	else:
		bot.send_message(my_id, "Ты сказал "+mess)

def runBot():
	bot.polling()

def runSchedulers():
	schedule.every().day.at("11:00").do(bot.send_message, chat_id= my_id, text=choose_morning_greetings())
	while True:
	    schedule.run_pending()
	    time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=runBot)
    t2 = threading.Thread(target=runSchedulers)
    t1.start()
    t2.start()

# my_id = 494551640