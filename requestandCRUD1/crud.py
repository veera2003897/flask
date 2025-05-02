from flask import Flask,request,jsonify
from pymongo import MongoClient
from bson import json_util


app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["activities"]
collection = db["lang"]

@app.route('/create/',methods=['POST'])
def create():
    try:
        data = request.get_json()
        print(data)
        collection.insert_many(data)
        return jsonify({"message":"Data inserted"})
    except Exception as e:
        return jsonify({"error":f'{e}'})

@app.route('/read/',methods=['GET'])
def read():
    try:
        data=collection.find({"name":"raju"})
        #print(data)
        # for record in data:
        #     record['_id'] =str(record['_id'])
        #     print(record)
        data1=json_util.dumps(data)
        return jsonify(data1)
    except Exception as e:
        return jsonify({"error":str(e)})

def update(key,value):
    try:
        print(type(key))
        #query={key:value},{"$set":{"age":25}}

        data=collection.update_many({key:value},{"$set":{"age":25}})
        print(data)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error":str(e)})

@app.route('/delete/',methods=['DELETE'])
def delete(key,value):
    collection.delete_one({key:value})
    return  jsonify({"message":"record deleted"})

app.add_url_rule("/update/<string:key>/<string:value>/","update",update,methods=["PUT"])
app.run(debug=True)