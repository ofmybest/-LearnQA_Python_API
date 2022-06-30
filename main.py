import time
import requests
import json

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = json.loads(response.text)
print(response.text)

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": obj['token']})
print(response.text)

time.sleep(obj['seconds'])

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": obj['token']})
print(response.text)
