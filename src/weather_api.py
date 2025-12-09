# weather_api.py
# PURPOSE:
# - Handles all OpenWeatherMap communication.
# - Loads API key from config.json.
# - Returns formatted weather data.

import requests
import json
import os
import utils

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.json")

def load_api_key():
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)["OPENWEATHER_API_KEY"]
    except FileNotFoundError:
        raise Exception("config.json missing — copy config.example.json and add your API key.")


def get_weather(city: str):
    api_key = load_api_key()

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()
    except Exception:
        return None

    # Check for city not found
    if data.get("cod") != 200:
        return None

    return {
        "temp": round(data["main"]["temp"]),
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]  # e.g., "04d"
    }
