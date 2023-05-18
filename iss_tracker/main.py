import requests
from datetime import datetime
import dateutil.parser
import smtplib

LAT = 0
LNG = 0
EMAIL_FROM = ""
PASS = ""
EMAIL_TO = ""
SMTP = ""


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    if not data:
        raise Exception("Response data is empty")
    if data["message"] != "success":
        raise Exception(f"Got {data['message']} instead of \"success\"")

    return float(data["iss_position"]["longitude"]), float(data["iss_position"]["latitude"])


def get_sunrise_and_sunset_time(my_coordinates: tuple[float]) -> dict[str: datetime]:
    parameters = {
        "lat": my_coordinates[1],
        "lng": my_coordinates[0],
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    if not data:
        raise Exception("Empty response!")
    if "results" not in data:
        raise NameError("Results are not found in response!")
    if not data["results"].get("sunrise") or not data["results"].get("sunset"):
        raise NameError("Sunrise or sunset data is not found in results!")

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunrise = dateutil.parser.isoparse(sunrise).replace(tzinfo=None)  # cleanup tz info for comparison
    sunset = dateutil.parser.isoparse(sunset).replace(tzinfo=None)
    return {
        "sunrise": sunrise,
        "sunset": sunset
    }


def check_if_night(sun_data: dict[str: datetime]) -> bool:
    time_now = datetime.now()
    if time_now < sun_data["sunrise"] or time_now > sun_data["sunset"]:
        return True
    return False


def is_iss_near(my_coord: tuple[float], iss_coord: tuple[float]) -> bool:
    if abs(iss_coord[0] - my_coord[0]) < 5 and abs(iss_coord[1] - my_coord[1]) < 5:
        return True
    return False


def send_email(from_email: str, to_email: str, smtp: str) -> None:
    with smtplib.SMTP(smtp, 587) as connection:
        connection.starttls()
        connection.login(EMAIL_FROM, PASS)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg="Subject:ISS Notification\n\nLook up!")


def main() -> int:
    iss_coordinates = get_iss_position()
    my_coordinates = LNG, LAT
    sun_data = get_sunrise_and_sunset_time(my_coordinates)
    if check_if_night(sun_data) and is_iss_near(my_coordinates, iss_coordinates):
        send_email(from_email=EMAIL_FROM, to_email=EMAIL_TO, smtp=SMTP)


if __name__ == "__main__":
    main()
