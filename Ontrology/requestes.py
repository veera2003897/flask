from bson import json_util
import requests

url = "http://localhost:5000"

def get_entity1():
    data = {
        'entity': 'python'
    }
    response = requests.post(f'{url}/get/canonical', json=data)
    print(response.text)

# get_entity1()

def get_category():
    data = {
        'entity':'c programming'
    }
    response = requests.post(f'{url}/get/category',json=data)
    print(response.json())

# get_category()

def get_skills():
    data = {'entity':'python'}
    response = requests.post(f'{url}/get/skill',json=data)
    print(response.json())

# get_skills()

def get_type():
    data = {'entity': 'python'}
    response = requests.post(f'{url}/get/type',json=data)
    print(response.json())

# get_type()

def get_dates_inbetween():
    data = {'From':"2023-10-08T18:56:47.734Z",'To':"2024-09-24T10:38:24.037Z"}
    response = requests.get(f'{url}/get/date',json=data)
    print(response.json())


get_dates_inbetween()

