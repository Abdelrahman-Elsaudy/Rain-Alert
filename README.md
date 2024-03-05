# Rain Alert Tool

---

This tool emails you in the morning if it's going to rain on that day.

---

## Applied Skills:

---
**1. API Requests**

- Making _API_ calls to [OpenWeatherMap](https://api.openweathermap.org/data/2.5/forecast) with the required parameters 
to get the weather details of the day.
- Manipulating the data to determine whether it is going to rain or not.

**2. Emailing with SMTP Module**

Emailing with Python built-in email service: _SMTP_.

**3. Environment Variables**

Introducing the _environment variables_ concept to secure private data like passwords and API keys.

---

## About The Project:

---

Raining is determined by _precipitation_ and when an area is probably going to rain, it's given a weather id less than 700 according to openweathermap.org.

```
will_rain = False

for hours_data in data["list"]:
    weather_code = hours_data["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True
```

This tool accesses the weather details of each hour of the day, gets to the weather id, and when it finds an id that is less than 700, it emails you saying: 
>"It's probably going to rain today" 

in the morning so you can be ready by bringing a coat or an umbrella.

---

## User Guide:

---

- To test the code, you can visit [Ventusky](https://www.ventusky.com) and choose precipitation to show you where it's probably
going to rain on this day.

- Then you go on [Latlong](https://www.latlong.net/) to determine the latitude and longitude of that area.

- You will also need to have an API key from [OpenWeatherMap](https://openweathermap.org/) by signing up.
- This tool becomes useful when it is run every day, and this can be automated by a website like [PythonAnywhere](https://www.pythonanywhere.com/).

---
_Credits to: 100-Days of Code Course on Udemy._