from flask import Flask,jsonify, request
from bson import json_util
import mongoquery

app = Flask(__name__)
ontologys = mongoquery.ontologys()

@app.route('/get/canonical/',methods=['POST'])
def get_entity():
    result = {'status': False, 'canonical': False, 'canonical_name': '', 'message': ''}
    try:
        datajson = request.json
        entity = ""
        if "entity" in datajson:
            entity = datajson['entity']

        if entity:
            data = ontologys.get_canonical(entity)
            print(data)
            result['canonical'] = data['canonical']
            result['canonical_name'] = data['canonical_name']
            result['status'] = True if data else False
        print(datajson)
        return jsonify(result)
    except Exception as e:
        return jsonify({"Error":str(e)})

@app.route('/get/category/',methods=['POST'])
def get_category():
    result = {
        'status': False,
        'entity': '',
        'category': [],
        'message': ''
    }
    try:
        datajson=request.json
        print(datajson)
        category =datajson['entity']
        print(category)
        data = ontologys.get_category(category)
        print(data)
        if data:
            result['status'] = True
            result['message'] = 'Entity category retrieved successfully'
            result['entity'] = data['entity']
            result['category'] = data['category']

            return result
        else:
            return jsonify({"message":"No categorical Data found"})
    except Exception as e:
        return jsonify({"Error":str(e)})

@app.route('/get/skill/',methods =['POST'])
def get_skills():
    try:
        synonyms_output = {
            'status': True,
            'entity': '',
            'synonyms':'',
            'message': ''
        }
        datajson= request.json
        #print(datajson)
        if 'entity' in datajson:
            synonyms_output['entity'] = datajson['entity']

        #print(skill)
        if synonyms_output['entity']:
            print(synonyms_output['entity'])
            data = ontologys.get_skills(synonyms_output['entity'])
            print(data)
            if data:
                synonyms_output['status']=True
                synonyms_output['synonyms']=data
                synonyms_output['message']='Synonyms retrieved successfully'
            print(synonyms_output)
            return synonyms_output
        else:
            return jsonify({"Message":"No Data found"})
    except Exception as e:
        return jsonify({"Error":str(e)})

@app.route('/get/type/',methods=['POST'])
def get_type():
    try:

        type_output = {
            'status': False,
            'entity': ' ',
            'type': ['Tools and Technologies'],
            'message': ''
        }
        datajson = request.json
        #print(datajson)
        if 'entity' in datajson:
            type_output['entity'] = datajson["entity"]
            #print(type_output)
        if type_output['entity']:
            data = ontologys.get_type(type_output['entity'])
            print(data)
            if data:
                type_output['status'] =True
                #print(data['type123'])
                type_output['type'] = data['type']
                print(type_output)
                type_output['message'] = "Entity type retrieved successfully"

                print(type_output)
            return type_output
        else:
            return jsonify({"Message":"No record find"})
    except Exception as e:
        return jsonify({"Error":str(e)})

@app.route('/get/date',methods =['GET'])
def get_dates():
    try:
        inbetween_dates = {
            'status': True,
            'startDate': '',
            'endDate': '',
            'Total_entity':[],
            'message': ''
        }
        datajson = request.json
        print(datajson)
        if "From" in datajson:
            From = datajson['From']
            inbetween_dates['startDate']=datajson['From']

        if "To" in datajson:
            To = datajson['To']
            inbetween_dates['endDate']=datajson['To']

        if From and To:
            data = ontologys.get_date(From,To)
            print(data)
            print(inbetween_dates)
            # records =[]
            # for record in data:
            #     if '_id' in record:
            #         record['_id']=str(record['_id'])
            #         records.append(record)
            #     else:
            #         records.append(record)
            inbetween_dates['Total_entity'] = data['total_entity']
            inbetween_dates['message']="Total retrieved in between dates"
            #print(records)
            return inbetween_dates
        else:
            return jsonify({"Message":"No Data Found"})
    except Exception as e:
        return jsonify({"Error":str(e)})

app.run(debug=True)

