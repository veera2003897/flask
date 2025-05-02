from pymongo import MongoClient
from datetime import  datetime

client = MongoClient("mongodb://localhost:27017/")
db = client['ontology']
collection = db['skill']

class ontologys:

    def get_canonical(self,entity):
        canonical_details = {}
        data = collection.find_one({'entity': entity},{'entity_type':1,'entity_details.canonical':1,'entity_details.canonical_name':1})
        canonical_details['canonical_name'] = data['entity_details'][0]['canonical_name']
        canonical_details['canonical'] = data['entity_details'][0]['canonical']
        return canonical_details

    def get_category(self,entity):
        data = collection.find_one({'entity':entity},{'_id':0,'entity':1,'entity_details.category':1})
        return {'entity': entity, 'category': data['entity_details'][0]['category'][0]}

    def get_skills(self,entity):
        canonical = collection.find({'entity':entity},{"_id":0,"entity_details.canonical_name":1})
        a=list(canonical)[0]['entity_details'][0]['canonical_name']
        canonical_name = a
        print(canonical_name)

        data = collection.aggregate([{"$match":{"entity_details.canonical_name":canonical_name}},{"$group":{"_id":"$entity_details.canonical_name","skill":{"$addToSet":"$entity"}}},{"$project":{"_id":0,"skill":1}}])
        print(data)
        return list(data)[0]['skill']

    def get_type(self,entity):
        #data = collection.find_one_and_update({'entity':entity},[{"$set":{"type1234":{"$type":'$entity'}}}])
        data = collection.find({"entity":entity},{"_id":0,"entity_details.type":1})
        a=list(data)
        if data:
            b = a[0]["entity_details"][0]["type"]
            print(b)
            #type_find= collection.find_one({'entity':entity},{'_id':0,'type1234':1})
            return {'type':b}

    def get_date(self,From,To):
        result =[]
        From =datetime.strptime(From,"%Y-%m-%dT%H:%M:%S.%fZ")
        To = datetime.strptime(To,"%Y-%m-%dT%H:%M:%S.%fZ")
        data = collection.find({"created_date":{"$gte":From,"$lte":To}},{"_id":0,"entity":1})
        for i in data:
            result.append(i['entity'])
        return {"total_entity":result}


# obj = ontologys()
# obj.get_type('python')






#pipeline=[{"$set":{"fromDate":{"$dateFromString":{'dateString':From}},"ToDate":{"$dateFromString":{'dateString':To}}}},{"$match":{"$expr":{"$and":[{"$eq":["$created_date","$fromDate"]},{"$eq":["$updated_date","$ToDate"]}}},{"$project":{"_id":0,"entity":1}}]

