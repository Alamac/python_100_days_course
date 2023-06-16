from twilio.rest import Client
import requests
from dataclasses import dataclass
from datetime import datetime
import os


COORDINATES = (44.81863449841634, 20.447057426526552)
WEATHER_API_KEY = os.environ.get("OWM_API_KEY")
ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")


@dataclass
class WeatherHour:
    hour: int
    weather: str


class WeatherApp:
    def __init__(self, coordinates):
        self.raw_weather_data, self.hourly_data = self.get_weather_from_server(
            coordinates)
        self.rain_hours = self.find_rain_hours(12)

    @staticmethod
    def get_weather_from_server(coordinates):
        lat, lon = coordinates
        params = {
            "lon": lon,
            "lat": lat,
            "appid": WEATHER_API_KEY,
            "exclude": "current,minutely,daily"
        }
        response = requests.get(ENDPOINT, params=params)
        response.raise_for_status()
        raw_weather_data = response.json()
        hourly_data = raw_weather_data["hourly"]
        return raw_weather_data, hourly_data

    def find_rain_hours(self, hours) -> list[WeatherHour]:
        results = []
        for i in self.hourly_data[:hours - 1]:
            if i["weather"][0]["id"] < 700:  # check if it's gonna be rain or snow
                hour = datetime.fromtimestamp(i["dt"]).hour
                weather = i["weather"][0]["main"]
                results.append(WeatherHour(hour, weather))

        return results

    def stringify(self):
        result = ""
        for i in self.rain_hours:
            result += f"It's gonna {i.weather} at {i.hour}\n"
        return result

    def __str__(self) -> str:
        return self.stringify()

    def send_message(self):
        send_sms(self.stringify())


def send_sms(text: str) -> None:
    client = Client(TWILIO_SID, TWILIO_TOKEN)

    message = client.messages \
                    .create(
                        body=text,
                        from_=TWILIO_NUMBER,
                        to=MY_NUMBER
                    )

    print(message.sid)
