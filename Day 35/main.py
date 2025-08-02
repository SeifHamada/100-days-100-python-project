import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "" # Replace with your OpenWeatherMap API key
account_sid = "" # Replace with your Twilio Account SID
auth_token = "" # Replace with your Twilio Auth Token

weather_params = {
    "lat":0, # Replace with your latitude
    "lon":0, # Replace with your longitude
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.message \
    .create(
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        from_="",  # Replace with your Twilio number
        to="+"  # Replace with the recipient's number
    )
    print(message.status)
