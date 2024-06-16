from flask import Blueprint

from resourceapis import ResourceAPI

# Create a Blueprint
api_blueprint = Blueprint('api', __name__)

# Define an API endpoint
# @api_blueprint.route('/resource', methods=['GET'])
# def get_resource():
#     resource = ResourceAPI()
#     return resource.get()

@api_blueprint.route('/api/v1/translate', methods=['POST'])
def create_resource():
    resource = ResourceAPI()
    print('v1/translate endpoint')
    return resource.create()

@api_blueprint.route('/api/v1/generate/summary', methods=['POST'])
def create_resource():
    resource = ResourceAPI()
    print('v1/translate endpoint')

    return resource.create()

@api_blueprint.route('/api/v1/generate/keywords', methods=['POST'])
def create_resource():
    resource = ResourceAPI()
    return resource.create()

@api_blueprint.route('/api/v1/generate/keyword-summary', methods=['POST'])
def create_resource():
    resource = ResourceAPI()
    return resource.create()