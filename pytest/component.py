import requests

def add(a, b):
    return a+b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by 0")
    return a / b     

def get_weather(city):
    response = requests.get(f"https://api.weather.com/v1/{city}")
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Could not fetch weather data")

