import eel
from weatherapi import get_weather

eel.init("web")

@eel.expose
def start_weather(city):
	return get_weather(city)

eel.start("main.html", size=(500, 500))
