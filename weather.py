import datetime
import requests
from pprint import pprint
from config import opweth_token


def get_weather(city, opweth_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={opweth_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}С\n"
              f"Влажность: {humidity}%\nВетер:{wind} м/с")

    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите город:  ")
    get_weather(city, opweth_token)


if __name__ == '__main__':
    main()
