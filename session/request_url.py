import requests


base_url = "http://localhost:5000/"

session = requests.session()

def session_create():
    response=requests.post(f"{base_url}set_session",json={"username1":"alice1"})
    print(response.json())

session_create()

def get_session():
    response=requests.get(f"{base_url}get_session")
    print(response.text)

get_session()

def clear_session():
    response=requests.get(f"{base_url}clear_session")
    print(response.json())

#clear_session()