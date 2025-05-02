import requests


data = {
    "rollno": "4031",
    "name": "asdgfdf",
    "age": 11,
}

response = requests.post("http://localhost:5000/insert", json=data)

print(response.json())