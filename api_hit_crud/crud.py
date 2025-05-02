from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost27017/")
db = client["api_hit_crud"]
#collection = db[]