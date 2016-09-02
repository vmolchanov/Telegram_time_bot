# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import telebot
import constants


def get_time(city, time_shift=0):
	tm = datetime.today() + timedelta(hours=time_shift)
	week_day = ""

	if tm.strftime("%a") == "Sun":
		week_day = "Воскресенье"
	elif tm.strftime("%a") == "Mon":
		week_day = "Понедельник"
	elif tm.strftime("%a") == "Tue":
		week_day = "Вторник"
	elif tm.strftime("%a") == "Wed":
		week_day = "Среда"
	elif tm.strftime("%a") == "Thu":
		week_day = "Четверг"
	elif tm.strftime("%a") == "Fri":
		week_day = "Пятница"
	elif tm.strftime("%a") == "Sat":
		week_day = "Суббота"

	local_time = tm.strftime("%H:%M")
	day = tm.strftime("%d")
	month = tm.strftime("%m")
	year = "20" + tm.strftime("%y")

	if month == "01":
		month = "Января"
	elif month == "02":
		month = "Февраль"
	elif month == "03":
		month = "Март"
	elif month == "04":
		month = "Апрель"
	elif month == "05":
		month = "Май"
	elif month == "06":
		month = "Июнь"
	elif month == "07":
		month = "Июль"
	elif month == "08":
		month = "Август"
	elif month == "09":
		month = "Сентябрь"
	elif month == "10":
		month = "Октябрь"
	elif month == "11":
		month = "Ноябрь"
	elif month == "12":
		month = "Декабрь"

	utc = 3 + time_shift

	return local_time + "\n" + week_day + ", " + day + " " + month + " " + year + " г. (UTC " + ("+" if utc > 0 else "-") + str(abs(utc)) + ")\n" + city



if __name__ == "__main__":
	token = constants.token
	bot = telebot.TeleBot(token)

	# bot.send_message(82317453, "Hi")

	@bot.message_handler(commands=["spb"])
	def start(msg):
		bot.reply_to(msg, get_time("Санкт-Петербург, Россия"))

	@bot.message_handler(commands=["irkutsk"])
	def start(msg):
		bot.reply_to(msg, get_time("Иркутск, Россия", 5))

	bot.polling()
