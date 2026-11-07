import requests
import os
from dotenv import load_dotenv
load_dotenv()

print("================================")
print("       WEATHER APPLICATION")
print("================================")

city = input("Enter City Name: ")

api_key = os.getenv("API_KEY")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"]

        print("\n========== WEATHER REPORT ==========")
        print(f"City          : {city}")
        print(f"Temperature   : {temperature} °C")
        print(f"Feels Like    : {feels_like} °C")
        print(f"Humidity      : {humidity}%")
        print(f"Wind Speed    : {wind_speed} m/s")
        print(f"Weather       : {description}")
        print("====================================")

    else:
        if response.status_code == 404:
            print("City Not Found! Please enter a valid city name.")
        elif response.status_code == 401:
            print("Invalid API Key!")
        else:
            print("Error:", data.get("message", "Unable to get weather data"))

except requests.exceptions.RequestException:
    print("Network Error! Please check your internet connection.")