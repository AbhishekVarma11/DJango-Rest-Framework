import requests

endpoint = "http://localhost:8000/api/products/1/update/" 

data = {
    "title": "this is tested by using update api",
    "price": 500
}

get_response = requests.put(endpoint, json=data) 
print(get_response.json())