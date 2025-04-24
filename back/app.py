from flask import Flask, request
from flask_cors import CORS, cross_origin
from  mongo import get_mongo_client
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()

def map_object_ids(document):
    """
    Recursively converts ObjectId fields in a MongoDB document to strings.
    """
    if isinstance(document, list):
        return [map_object_ids(item) for item in document]
    elif isinstance(document, dict):
        return {key: str(value) if isinstance(value, ObjectId) else map_object_ids(value) for key, value in document.items()}
    else:
        return document

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/forms')
def forms_index():
    client = get_mongo_client()

    if client:
        db = client["slack"]
        collection = db["forms"]

        forms = collection.find()
        result = [map_object_ids(form) for form in forms]

        return {"forms": result}

@app.route('/api/forms/<id>')
def forms_show(id):
    client = get_mongo_client()

    if client:
        db = client["slack"]
        collection = db["forms"]

        result = collection.find_one({"_id": ObjectId(id)})

        if result:
            form = map_object_ids(result)

        return {"form": form}

@app.route('/api/forms', methods=['POST'])
def forms_create():
    client = get_mongo_client()

    if client:
        db = client["slack"]
        collection = db["forms"]

        data = request.get_json()

        result = collection.insert_one(data)

        return {"status": "success", "id": str(result.inserted_id)}, 201
    else:
        return {"status": "error", "message": "Could not connect to database"}, 500

@app.route('/api/forms/<id>', methods=['PUT'])
def form_attach_fields(id):
    client = get_mongo_client()

    if client:
        db = client["slack"]
        collection = db["forms"]

        data = request.get_json()

        form = collection.find_one({"_id": ObjectId(id)})
        
        if not form:
            return {"status": "error", "message": "Form not found"}, 404
        
        if not isinstance(form["fields"], list):
            collection.update_one({"_id": ObjectId(id)}, {"$set": {"fields": []}})
        
        newField = {
            "_id": ObjectId(),
            "key": data["key"],
            "type": data["type"],
            "value": data["value"],
        }

        result = collection.update_one({"_id": ObjectId(id)}, {"$push": {"fields": newField}})
        
        if result.modified_count == 0:
            return {"status": "error", "message": "Could not update form"}, 500

        return {"status": "success", "id": str(newField["_id"])}, 200
    else:
        return {"status": "error", "message": "Could not connect to database"}, 5
    
@app.route('/api/forms/<id>', methods=['DELETE'])
def forms_delete(id):
    client = get_mongo_client()

    if client:
        db = client["slack"]
        collection = db["forms"]
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            return {"status": "success"}, 200
        else:
            return {"status": "error", "message": "Field not found"}, 404
        
@app.route('/api/forms/<form_id>/fields/<field_id>', methods=['DELETE'])
def forms_delete_field(form_id, field_id):
    client = get_mongo_client()

    if client:
        db = client["slack"]
        collection = db["forms"]

        result = collection.update_one(
            {"_id": ObjectId(form_id)},
            {"$pull": {"fields": {"_id": ObjectId(field_id)}}}
        )

        if result.modified_count > 0:
            return {"status": "success", "message": "Field deleted successfully"}, 200
        else:
            return {"status": "error", "message": "Field not found or could not be deleted"}, 404
    else:
        return {"status": "error", "message": "Could not connect to database"}, 500