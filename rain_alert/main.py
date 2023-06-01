import requests
from dataclasses import dataclass

COORDINATES = (44.81863449841634, 20.447057426526552)
API_KEY = "3dc132561183b01dc8af5fa029738bf0"
ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"


@dataclass
class WeatherHour:
    hour: int
    weather: str


class WeatherApp:
    def __init__(self, coordinates):
        self.raw_weather_data, self.hourly_data = self.get_weather_from_server(coordinates)
        self.rain_hours = self.find_rain_hours()
        s


    @staticmethod
    def get_weather_from_server(self, coordinates):
        lat, lon = coordinates
        params = {
            "lon": lon,
            "lat": lat,
            "appid": API_KEY,
            "exclude": "current,minutely,daily"
        }
        response = requests.get(ENDPOINT, params=params)
        response.raise_for_status()
        raw_weather_data = response.json()
        hourly_data = raw_weather_data["hourly"]
        return raw_weather_data, hourly_data


    def find_rain_hours(self, hours):
        results = [WeatherHour() for i in self.hourly_data[:hours - 1] if i["weather"][0]["id"] < 700]
        return results



