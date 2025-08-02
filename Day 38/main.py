import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/67d22f4817d7a0b9dbcf6400c88b63bf/workoutTracker/workouts"
WEIGHT = 64
HEIGHT = 176
AGE = 19

test = input("What was you workout today: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

param = {
    "query": test,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

bearer_header = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

response = requests.post(NUTRITIONIX_ENDPOINT, json=param, headers=headers)
#print(response.json())


today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

for exercise in response.json()["exercises"]:
    input = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    exercise_response = requests.post(SHEET_ENDPOINT, json=input, headers=bearer_header)
    print(exercise_response.text)
