import requests, json

#TODO INTRODUCTION

url1 = "https://nominatim.openstreetmap.org/search"

q = input("Enter your location: ")

params1 = {
    "q": q,
    "format": "json",
    "limit": 1
}

headers = {
    "User-Agent": "Weather-App-by-Arsh"
}

loc_resp = requests.get(
    url1,
    params = params1,
    headers = headers
)

loc_data = loc_resp.json()

lat = loc_data[0]["lat"]
lon = loc_data[0]["lon"]

url2 = "https://api.open-meteo.com/v1/forecast"

params2 = {
    "latitude": lat,
    "longitude": lon,
    "current_weather": True
}

wea_resp = requests.get(url2, params=params2)

wea_data = wea_resp.json()

temp = wea_data["current_weather"]["temperature"]
speed = wea_data["current_weather"]["windspeed"]

print(f"Temperature: {temp}\u00b0C")
print(f"Wind Speed: {speed} km/h")