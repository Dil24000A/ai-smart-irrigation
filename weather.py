import requests

def is_raining():
    api_key = "YOUR_API_KEY"
    city = "Bhubaneswar"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    data = requests.get(url).json()

    return "rain" in data