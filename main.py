import requests
import smtplib
import os

Page = "https://api.openweathermap.org/data/2.5/forecast"

my_email = "abdelrahmanelsaudyyy@gmail.com"
password = os.getenv("EMAIL_PASS")           # Environment variables on my Windows.
API_KEY = os.getenv("OWM_API")

MY_LAT = "30.044420"         # These are the coordinates of Cairo, Egypt.
My_long = "31.235712"

parameters = {
    "lat": MY_LAT,
    "lon": My_long,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4                  # to check the weather in the next 4 hours.
}

response = requests.get(url=Page, params=parameters)
response.raise_for_status()
data = response.json()

# To check the rain we get the weather id which is the code that determines the weather condition
# according to: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
# Any number less than 700 means it will rain.

will_rain = False

for hours_data in data["list"]:
    weather_code = hours_data["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        full_msg = "It's probably gonna rain today."
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="abdelrahman.elsaudy@gmail.com",
                            msg=full_msg)
