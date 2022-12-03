import requests

API_KEY = 'ad972d2122cddccab12092e88a2ba9b0'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data['weather'][1]['description']
    weather2 = data['weather'][0]
    print(weather)
    print(weather2)
else:
    print("An error occurred.")
        
