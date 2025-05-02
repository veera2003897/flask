import requests

def create():
        data = [{
                "name": "veeranjaneyulu",
                "age": 23,
                "email": "alice@example12.com"
        },{"name":"rajesh","age":30,"email":"raju2000@gmail.com"}]
        response = requests.post("http://localhost:5000/create",json=data)

        print(response.text)

#create()

def find():
        response=requests.get("http://localhost:5000/read")
        print(response.text)

find()

def update():
        data = {
                # "name": "Alice",
                "age": 31,
                # "email": "alice@example12.com"
        }
        response = requests.put("http://localhost:5000/update/name/Alice",json=data)
        print(response.text)

#update()

def delete():
        response = requests.delete("http://localhost:5000/delete/age/25")
        print(response.text)

#delete()
