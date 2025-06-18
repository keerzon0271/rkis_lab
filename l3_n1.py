import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
now = datetime.now()
day_of_week = now.strftime("%A")
month = now.strftime("%B")
day = now.strftime("%d")

name = "Вадим"
print(f"День недели: {day_of_week}\nТекущий месяц: {day} {month}\nИмя: {name}")