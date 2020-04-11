from InstagramBot import InstagramBot
import requests
from datetime import datetime
import pytemperature
import os


def getBioData():
    getCurrentTime = datetime.now()
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Jakarta&appid=0485dc4694b306c4055ef08657034f79")
    data = response.json()
    timestamp = data["dt"]
    desc = data["weather"][0]["main"]
    time = getCurrentTime.strftime("%a %b %d, %H:%M:%S")
    temp = int(pytemperature.k2c(data["main"]["temp"]))
    city = data["name"]
    bioText = f"{temp}°C {city}\n{desc}\n{time}"
    return bioText
