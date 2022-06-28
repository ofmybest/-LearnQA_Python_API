import requests

response = requests.put("https://playground.learnqa.ru/api/compare_query_type")
print(response.text)

response = requests.head("https://playground.learnqa.ru/api/compare_query_type", data={"method": "HEAD"})
print(response.text)

response = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": "PUT"})
print(response.text)

methods = ["GET","PUT","POST","DELETE"]
for method in methods:
    response = requests.get("https://playground.learnqa.ru/api/compare_query_type", params={"method": method})
    print("get - " + method)
    print(response.status_code)
    print(response.text)
    print("---------")

    response = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": method})
    print("put - " + method)
    print(response.status_code)
    print(response.text)
    print("---------")

    response = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": method})
    print("post - " + method)
    print(response.status_code)
    print(response.text)
    print("---------")

    response = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data={"method": method})
    print("delete - " + method)
    print(response.status_code)
    print(response.text)
    print("---------")