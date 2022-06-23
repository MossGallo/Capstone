import requests

params = {
    'lat': 45.5152,
    'lon': -122.678,
    'appid': '6376664df4713d68190d6ddf425b7a2e',
    'exclude': 'minutely,hourly,daily,alerts',
    'units': 'imperial'
}
response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=params)
print((response.json()))

