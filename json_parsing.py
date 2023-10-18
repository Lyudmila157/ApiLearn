import requests

headers = {"some_header": "123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
print(response.text)
print(response.headers)

# response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
# print(response.text)
#
# response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
# print(response.text)
#
# response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
# print(response.status_code)

# response = requests.post("https://playground.learnqa.ru/api/get_500")
# print(response.status_code)
# print(response.text)
#
# response = requests.post("https://playground.learnqa.ru/api/something")
# print(response.status_code)
# print(response.text)

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
# print(response.status_code)

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# first_response = response.history[0]
# second_response = response
# print(first_response.url)
# print(second_response.url)

# import json
#
# string_as_json_format = '{"answer": "Hello, Mila"}'
# obj = json.loads(string_as_json_format)
# # print(obj['answer'])
#
# key = "answer"
#
# if key in obj:
#     print(obj[key])
# else:
#     print(f"Ключа {key} в JSON нет")