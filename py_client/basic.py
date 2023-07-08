import requests

endpoint="https://httpbin.org/anything"

get_response=requests.get(endpoint)

print(get_response.text)