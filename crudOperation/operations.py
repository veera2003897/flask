from flask import Flask, render_template,request,redirect,jsonify
from pymongo import MongoClient
import json


app=Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")

database = client["Collections"]
collection = database["Crud_Operation"]


@app.route('/insert',methods=['POST'])
def write_operation():
    dic={}
    if request.method == 'POST':

        request_data = request.json

        rollno = request_data.get("rollno")
        name = request_data.get("name")
        age = request_data.get("age")
        graduation = request_data.get("qualification")

        dic["rollno"] = rollno
        dic["name"] = name
        dic["age"] = age
        dic["qualification"] = graduation
        collection.insert_one(dic)

    return {'status': True}

@app.route('/Crud_Operation',methods=['POST'])
def operation():
    if request.method == 'POST':
        n=request.form['number']
        if int(n)>=1 and int(n)<=4:
            if n=="1":
                return render_template('data_insert.html')

    else:
        return jsonify("please Enter Valid data")

@app.route('/')
def operation_choose():
    return render_template('index.html')


app.run(debug=True)