import requests

# endpoint = "https://api.github.com/users/AhmedERRAJAAI"
endpoint = "http://127.0.0.1:8000/api/" 
response = requests.get(endpoint)
print(response.text)