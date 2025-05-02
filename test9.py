import copy

import requests
from bson import ObjectId
from pymongo import MongoClient


def create_job():
    user_input = {'portalID': "65cf32455ab7cd33de468a95", 'mode': 'start', 'selection': 'all_jobs', "pages": "",
                  'category': '', 'sub_category': '', 'keyword': '', 'location': '', 'time_sleep': 3,
                  "scraperTool": "selenium"}

    res_data = requests.post(url="http://192.168.1.222:5000/scraperapi/insertscraperjob", json=user_input)
    print(res_data.json())


def perform_wrangling():
    r = requests.post(url="http://192.168.1.107:8001/scraper/executeQuery",
    # r = requests.post(url="http://10.0.1.26:8001/scraper/executeQuery",
                      json={"processID": "6710b14badbb48cf03e0bf6a", "redisName": ""})
    #                   json={"processID": "65cf04f14cf974e18793dcf3"})
                      # json={"processID": "65c37a714e13f6dfdc6cd60a"})
                      # json={"processID": "65c36f4c4e13f6dfdc6cd609"})
                      # json={"processID": "65c20fd65d724a2f448ac078"})
    print(r.json())


# create_job()
perform_wrangling()

