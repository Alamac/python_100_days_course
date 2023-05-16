##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import smtplib
import os
from random import choice

#Constants
EMAIL = ""
PASS = ""


def send_letter(message, to):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(from_addr=EMAIL, to_addrs=to, msg=f"Subject:Happy Birthday!\n\n{message}")


def pick_random_letter():
    file_list = os.listdir('./letter_templates')
    with open(f"./letter_templates/{choice(file_list)}", 'r') as file:
        return file.read()


def process_birthday(entry):
    letter = pick_random_letter()
    letter = letter.replace('[NAME]', entry["name"])
    send_letter(letter, entry["email"])


now = dt.datetime.now()
df = pd.read_csv("birthdays.csv").to_dict(orient='records')
now_day = now.day
now_month = now.month

birthdays = [i for i in df if i["month"] == now_month and i["day"] == now_day]

if birthdays:
    for i in birthdays:
        process_birthday(i)


