import requests
from pprint import pprint


API_key = "0f8cd7045ed89e83585f6b580a1ef06d"
location = "BOSTON"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="
final_url = weather_url + API_key
weather_data = requests.get(final_url).json()
pprint(weather_data)