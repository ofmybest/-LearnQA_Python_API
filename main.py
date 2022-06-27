import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
end_response = response

print(len(response.history))
print(end_response.url)



