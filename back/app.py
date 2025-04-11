from flask import Flask, request
from flask_cors import CORS, cross_origin
from  mongo import get_mongo_client
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/fields')
def fields():
    client = get_mongo_client()

    if client:
        db = client["slack"]
        collection = db["fields"]

        fields = collection.find()
        print(fields)
        result = []
        for field in fields:
            result.append({
                "key": field["key"],
                "type": field["type"],
                "value": field["value"],
            })
        return {"fields": result}

@app.route('/api/fields', methods=['POST'])
def create():
    client = get_mongo_client()

    if client:
        db = client["slack"]
        collection = db["fields"]

        data = request.get_json()

        result = collection.insert_one(data)

        return {"status": "success", "id": str(result.inserted_id)}, 201
    else:
        return {"status": "error", "message": "Could not connect to database"}, 500
    


