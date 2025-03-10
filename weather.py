from dotenv import load_dotenv
from pprint import pprint 
import os
import requests

load_dotenv()

def current_weather(city = "Sofia"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()
    return weather_data
