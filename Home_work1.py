# json_text = {
#     "messages":[
#         {"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},
#         {"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]
# }
# _________________________________________________________________________________________
# print(json_text['messages'][0])
#
# import requests
#
# response = requests.get("https://playground.learnqa.ru/api/long_redirect",)
# print(f"Redirect count: {len(response.history)}")
# print(f"Last request URL: {response.url}")
# __________________________________________________________________________________________
# import requests
#
# methods = ["POST","GET","PUT","DELETE","Wrong method"]
# api_url = "https://playground.learnqa.ru/api/compare_query_type"
#
# for method in methods:
#     get_response = requests.get(
#         api_url,
#         params={'method': f"{method}"})
#     print(f"GET request with parameter 'method' : {method}")
#     print(f"Response code: {get_response.status_code}")
#     print(f"Response text: {get_response.text}")
#     print("-----------------")
#
#     post_response = requests.post(
#         api_url,
#         data={'method': f"{method}"})
#     print(f"POST request with parameter 'method' : {method}")
#     print(f"Response code: {post_response.status_code}")
#     print(f"Response text: {post_response.text}")
#     print("-----------------")
#
#     put_response = requests.put(
#         api_url,
#         data={'method': f"{method}"})
#     print(f"PUT request with parameter 'method' : {method}")
#     print(f"Response code: {put_response.status_code}")
#     print(f"Response text: {put_response.text}")
#     print("-----------------")
#
#
#     delete_response = requests.delete(
#         api_url,
#         data={'method': f"{method}"})
#     print(f"DELETE request with parameter 'method' : {method}")
#     print(f"Response code: {delete_response.status_code}")
#     print(f"Response text: {delete_response.text}")
#     print("-----------------")
# __________________________________________________________________________________
# import requests
# import time
#
#
# status_response = "Job is NOT ready"
# result_response = "Job is ready"
# error_response = "No job linked to this token"
# incorrect_token = "dfaf5f5sefs5f5effesf558"
#
# response1 = requests.get("https://playground.learnqa.ru/api/longtime_job")
# job_time = response1.json()['seconds']
# job_token = response1.json()['token']
#
# data = {
#     'token': job_token
# }
# response2 = requests.get(
#     "https://playground.learnqa.ru/api/longtime_job",
#      params=data
#     )
# if response2.json()['status'] == status_response:
#     print(f"PASSED! Correct server answer, "
#           f"when job is not ready: {response2.json()['status']}")
# else:
#     print(f"FAILED! Incorrect server answer "
#           f"when jon is not ready: {response2.json()['status']}")
# print(f"Response text: {response2.text}")
#
# print("------------")
# time.sleep(job_time)
# response3 = requests.get(
#     "https://playground.learnqa.ru/api/longtime_job",
#      params=data
#     )
#
# if response3.json()['status'] == result_response:
#     print(f"PASSED! Correct server answer, "
#           f"when job is ready: {response3.json()['status']}. Job time: {job_time}")
# else:
#     print(f"FAILED! Incorrect server answer "
#           f"when jon is ready: {response3.json()['status']}. Job time: {job_time}")
# print(f"Response text: {response3.text}")
#
# print("------------")
#
# response4 = requests.get(
#     "https://playground.learnqa.ru/api/longtime_job",
#      params={'token': incorrect_token}
#     )
#
# if response4.json()['error'] == error_response:
#     print(f"PASSED! Correct server answer about job, "
#           f"when incorrect token in request: {response4.json()['error']}")
# else:
#     print(f"FAILED! Incorrect server answer about job, "
#           f"when incorrect token in request: {response4.json()['error']}")
# print(f"Response text: {response4.text}")
# ___________________________________________________________________________________
import requests

passwords = [
    '123456',
    '123456789',
    'qwerty',
    'password',
    '1234567',
    '12345678',
    '12345',
    'iloveyou',
    '111111',
    '123123',
    'abc123',
    'qwerty123',
    '1q2w3e4r',
    'admin',
    'qwertyuiop',
    '654321',
    '555555',
    'lovely',
    '7777777',
    'welcome',
    '888888',
    'princess',
    'dragon',
    'password1',
    '123qwe']
url = "https://playground.learnqa.ru/api/"
correct_login = "super_admin"
correct_password = 'not know'
for password in passwords:

    response = requests.post(
        f"{url}get_secret_password_homework",
        data={
            'login': correct_login,
            'password': password
            }
    )

    if response.status_code == 200:
        auth_cookie = response.cookies['auth_cookie']
    else:
        auth_cookie = "mock_cookie"


    response1 = requests.post(
        f"{url}check_auth_cookie",
        data={
            'auth_cookie' : auth_cookie
        }
    )

    if response1.text == 'You are authorized':
        print(f"Login: {correct_login}. Password: {password} is correct!")
        correct_password = password
        break
    else:
        print(f"Login: {correct_login}. Password: {password} is NOT correct!")

    print("--------------")

print(f"Correct password: {correct_password}")
# ____________________________________________________________________________________