from flask import Flask,request,jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
database = client["activities"]
collection  = database["postId"]

@app.route("/create",methods=["POST"])
def create_record():
    try:
        data = request.json
        print(data)
        if not data:
            return jsonify({"no data is provided":""})
        collection.insert_many(data)
        return jsonify({"record created":"Done"})
    except Exception as e:
        return jsonify({"error":str(e)})

@app.route("/read", methods = ["GET"])
def read_records():
    try:
        records = list(collection.find({}))
        for record in records:
            record["_id"] = str(record["_id"])
        print(records)
        return jsonify(records)
    except Exception as e:
        return jsonify({"error":str(e)})

@app.route('/update/<string:key>/<string:value>' , methods = ['PUT'])
def update_record(key,value):
    try:
        new_data = request.get_json()
        if not new_data:
            return jsonify({"error":"No update data provided"})
        query = {key:value}
        update_record = collection.find_one_and_update(query,{"$set":new_data,"$unset":{"name":1}})
        print(update_record)
        if update_record:
            return jsonify({"message":"Record Updated "})
        else: return jsonify({"message":"record not found"})
    except Exception as e:
        return jsonify({"error":str(e)})

@app.route("/delete/<string:key>/<string:value>" , methods = ["DELETE"])
def delete_record(key,value):
    try:
        query = {key:int(value)}
        result = collection.delete_one(query)
        if result.deleted_count>0:
            return jsonify({"message":"record deleted succesfully"})
        else:
            return jsonify({"message":"no record find"})
    except Exception as e:
        return jsonify({"error":str(e)})


app.run(debug=True)
