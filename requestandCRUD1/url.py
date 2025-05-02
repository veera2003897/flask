import requests
from bson import json_util

url = "http://localhost:5000/"

def create():
    data=[{"id":1,"name":"raju"},{"id":2,"name":"raju"}]
    response = requests.post(f'{url}create',json=data)
    print(response.json())

#create()

def read():
    response = requests.get(f'{url}read')
    #print(list(response))
    data=json_util.loads(response.json())
    for record in data:
        print(record)

#read()

def update():
    response = requests.put(f'{url}update/name/raju')
    print(response.text)

#update()

def delete():
    response=requests.delete(f'{url}delete/name/raju')
    print(response.text)

delete()
