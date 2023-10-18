from json.decoder import JSONDecodeError
import requests

# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response is not a JSON format")
payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response1.cookies.get('auth_cookie')
cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})
response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(response2.text)
# print(response.status_code)
# print(dict(response.cookies))

# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "Mila"})
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])

# payload = {"name": "Mila"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)

# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)

# # print("Hello, World!")
# url = "https://playground.learnqa.ru/api/hello?name=Mila"
# payload = {}
# headers = {}
# response = requests.request("GET", url, headers=headers, data=payload)
# print(response.text)