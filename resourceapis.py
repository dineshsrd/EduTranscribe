from flask import jsonify, request

class ResourceAPI:
    def get(self):
        # Logic for GET request
        data = {"message": "GET request successful"}
        return jsonify(data), 200

    def create(self):
        # Logic for POST request
        data = request.get_json()
        response = {"message": "POST request successful", "data": data}
        return jsonify(response), 201
