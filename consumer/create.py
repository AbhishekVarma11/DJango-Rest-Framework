import requests

endpoint = "http://localhost:8000/api/products/" 

data = {
    "title": "This field is done",
    "content":"this is created for testing post request",
    "price":32.99
}
get_response = requests.post(endpoint, json=data) 
print(get_response.json())