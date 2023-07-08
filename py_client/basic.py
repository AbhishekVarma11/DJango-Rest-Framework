import requests

endpoint="https://httpbin.org/anything"

get_response=requests.get(endpoint,json={"query":"hello abhi"})


print(get_response.json())