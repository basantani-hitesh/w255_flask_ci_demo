from flask_restful import Resource

from api.app import api

class DefaultResouce(Resource):
    def get(self):
        return {"status": "success", "data" : {"msg": "Hello World"}}


api.add_resource(DefaultResource, "/", endpoint = "home")
