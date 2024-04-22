from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort, redirect
from flask_jwt_extended import jwt_required
from dotenv import dotenv_values
import requests

order_blueprint = Blueprint('order', __name__)
env_vars = dotenv_values('.env')

@order_blueprint.route('/test' , methods=['GET'])
@jwt_required()
def product_get():
    error_message = {'error': 'Okla'}
    return jsonify(error_message), 200



