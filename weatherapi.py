import requests
import datetime

open_weather_token ="918f25fa621dda912690a0dabc50fe1c"

def get_weather(place, open_weather_token=open_weather_token):
    code_to_emoji = {'Clear': 'Ясно \U00002600', 'few clouds': 'Малооблачно \U000026C5',
                     'scattered clouds': 'Облачно с прояснениями \U000026C5',
                     'broken clouds': 'Пасмурно \U00002601', 'overcast clouds': 'Очень пасмурно \U00002601',
                     'drizzle': 'Морось \U00002614', 'light rain': 'Небольшой дождь \U00002614',
                     'moderate rain': 'Дождь \U00002614', 'heavy intensity rain': 'Умеренно сильный дождь \U00002614',
                     'extreme rain': 'Сильный дождь \U00002614', 'very heavy rain': 'Длительный сильный дождь \U00002614',
                     'shower rain': 'Ливень \U00002614', 'freezing rain': 'Дождь со снегом \U00002614\U00002744',
                     'light snow': 'Небольшой снег \U00002744', 'Snow': 'Снег \U00002744',
                     'Heavy snow': 'Снегопад \U00002744', 'ragged shower rain': 'Град \U00002614',
                     'thunderstorm': 'Гроза \U0001F329', 'thunderstorm with rain': 'Дождь с грозой \U00002614\U0001F329',
                     'thunderstorm with drizzle': 'Гроза с градом \U00002614\U0001F329'}
    try:
        req = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={place}&appid={open_weather_token}&units=metric"
        )
        data = req.json()
        city = place.lower().capitalize()
        feels_like = int(data['main']['feels_like'])
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        temp = int(data['main']['temp'])
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        day_length = sunset - sunrise
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%d-%m-%Y %H-%M-%S')
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%d-%m-%Y %H-%M-%S')
        visibility = data['visibility']
        description = data['weather'][0]['description']

        if description in code_to_emoji:
            weather_emoji = code_to_emoji[description]
        else:
            weather_emoji = 'не могу понять что там в небе происходит... \U0001F914'

        speed = data['wind']['speed']
        res = f"---- {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ----\n" \
              f"Город: {city}\nТемпература: {temp}°C, ощущается как {feels_like}°C, {weather_emoji}\n" \
              f"Влажность: {humidity}%\nДавление: {pressure} мбар\nВидимость: {visibility} м\n" \
              f"Ветер: {speed} м/c\nВосход: {sunrise}\nЗаход: {sunset}\nПродолжительность дня: {day_length}"
        return res

    except:
        return "Проверьте правильность названия города или подключение к интернету!"

if __name__=="__main__":
    print(get_weather('grodno'))