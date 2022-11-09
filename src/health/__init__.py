from flask import Blueprint
from flask import jsonify
from flask_restx import Namespace
from flask_restx import Resource

# Restx health check
api = Namespace("health", description="Health check related operations")

class Health(Resource):
    def get(self):
        # import pymongo
        # from os import getenv
        # # print(getenv('MONGODB_URL'))
        # client = pymongo.MongoClient(getenv('MONGODB_URL'))
        # return jsonify(status="OK", message="Server is healthy", server_info=client.server_info())
        return jsonify(status="OK", message="Server is healthy")

api.add_resource(Health, "")
