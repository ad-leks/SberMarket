## -*- coding: utf-8 -*-
import requests
from datetime import date, timedelta
import telebot
import os
import json
import csv
import re
import sys

def get_intervals(cart_id):
	date_start = date.today()
	date_stop = date.today() + timedelta(6)
	date_start = date(date_start.year, date_start.month, date_start.day)
	date_stop = date(date_stop.year, date_stop.month, date_stop.day)
	slots = []

	url = 'https://sbermarket.ru/api/shipments/{0}/shipping_rates'.format(cart_id)
	paramsForUrl = {}

	delta = date_stop - date_start
	if delta.days <= 0:
		print("Фигня какая-то в датах")
	for i in range(delta.days + 1):
		slots.append({"id": i, "day": date_start + timedelta(i)})

	print(slots)

	for slot in slots:
		paramsForUrl["date"] = slot.get("day")
		r = requests.get(url, params=paramsForUrl).json()
		intervals = []
		for window in r.get("shipping_rates"):
			if window.get("is_free") is True:
				intervals.append(window.get("delivery_window").get("human_interval"))
		slot.update({"intervals": intervals})

	for slot in slots:
		print(slot)

	return slots

def alert(slots):
	token = os.environ("TOKEN")
	bot = telebot.TeleBot(token)
	print(bot.send_message(74152489, "test"))

def main():
	cart_id = "H42237155066"
	slots = 1
	#slots = get_intervals(cart_id)
	alert(slots)

if __name__ == '__main__':
	main()

