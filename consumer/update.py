import requests

endpoint = "http://localhost:8000/api/products/7/update/" 
headers={'Authorization':'Bearer f55e82c18af3d7cbfa5b12be50783c16c7b10d67'}
data = {
    "title": "this is tested by using update api",
    "price": 500
}

get_response = requests.put(endpoint, json=data,headers=headers) 
print(get_response.json())