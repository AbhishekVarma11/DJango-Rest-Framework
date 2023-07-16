import requests

from getpass import getpass

auth_endpoint="http://localhost:8000/api/auth/"

password=getpass()

auth_response=requests.post(auth_endpoint,json={'username':'abhishek','password':password})

print(auth_response.json())

if auth_response.status_code==200:
    token=auth_response.json()['token']
    #headers={"Authorization":f"Token {token}"}
    headers={"Authorization":f"Bearer {token}"}
    endpoint = "http://localhost:8000/api/products/3/" 

    get_response = requests.get(endpoint) 
    print(get_response.json())
    