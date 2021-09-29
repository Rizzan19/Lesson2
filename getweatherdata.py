import requests
import json
from my_key import key


def get_weather_data(place, api_key=None):
    rest = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + place + '&appid=' + key)
    json_requests = rest.json()

    coord = {"lon": round(json_requests['coord']['lon'], 2),
             "lat": round(json_requests['coord']['lat'], 2)}

    feels_like = round(json_requests['main']['feels_like'] - 273.15, 2)

    timezone = int(json_requests['timezone'] / 3600)
    if (timezone >= 0):
        timezone = ('UTC+' + str(timezone))
    else:
        timezone = ('UTC' + str(timezone))

    json_requests = {"name": json_requests['name'],
                     "coord": coord,
                     "country": json_requests['sys']['country'],
                     "feels_like": feels_like,
                     "timezone": timezone}
    json_result = json.dumps(json_requests)
    return (json_result)


if __name__ == "__main__":
    get_weather_data('Petersburg', api_key=key)
    get_weather_data('Moscow', api_key=key)
    get_weather_data('Dhaka', api_key=key)
