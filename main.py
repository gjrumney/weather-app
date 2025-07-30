'''
SIMPLE PYTHON WEATHER APP

- Ask for location
- Convert location to co-ordinates
- Input into WeatherAPI through requests
- Print temperature, precipitation etc
'''

import requests
from geopy import Nominatim

def get_location(geolocator): # turns location input to co-ords
    location_name = input("Enter a location: ")
    location = geolocator.geocode(location_name)
    
    if location:
        return location.latitude, location.longitude
    else:
        print("Location not found. Please try again.")
        return None

def request_weather(coords, api_key): # uses WeatherAPI to grab current weather data
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={coords[0]},{coords[1]}"
    
    weather_data = requests.get(url)
    data = weather_data.json()
    
    return data


def main():
    geolocator = Nominatim(user_agent="main.py")
    api_key = 'your Weather API api key here!'
    
    
    coords = None
    
    while coords is None:
        coords = get_location(geolocator)
    data = request_weather(coords, api_key)
    
    print("\nData found!\n" +
        f"Location: {data['location']['name']}\n" +
        f"Temperature (°C): {data['current']['temp_c']}\n" +
        f"Precipitation (mm): {data['current']['precip_mm']}\n" +
        f"Wind Speed (mph): {data['current']['wind_mph']}\n" +
        f"Visibility (km): {data['current']['vis_km']}\n" +
        f"Condition: {data['current']['condition']['text']}\n"
        )
    
if __name__ == "__main__":
    main()
