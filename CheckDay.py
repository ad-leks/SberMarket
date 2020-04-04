## -*- coding: utf-8 -*-
import requests
from datetime import date, timedelta
import json
import csv
import re
import sys

date_start = date.today()
date_stop = date.today() + timedelta(6)
date_start = date(date_start.year, date_start.month, date_start.day)
date_stop = date(date_stop.year, date_stop.month, date_stop.day)
lsDate = []

url = 'https://sbermarket.ru/api/shipments/H02815115275/shipping_rates'
paramsForUrl = dict()

delta = date_stop - date_start
if delta.days<=0:
    print ("Фигня какая-то в датах")
for i in range(delta.days + 1):
	lsDate.append(date_start + timedelta(i))

for day in lsDate:
	paramsForUrl ["date"] = day
	re = requests.get(url, params=paramsForUrl)
	print(re.text)