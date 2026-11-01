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

class APIClient:
    """API client to fetch user details from external API """ #string literals to create docs for fucntion/methods
    def get_user_data(self, user_id):
        response = requests.get(f"https://api.example.com/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError("API request failed")

class UserService:
    """
    Uses API client to fetch user data
    and process it
    """
    def __init__(self, api_client):
        self.api_client = api_client

    def get_username(self, user_id):
        """ Fetches user details from api client and return name in upper case """
        user_data = self.api_client.get_user_data(user_id)
        return user_data["name"].upper()
