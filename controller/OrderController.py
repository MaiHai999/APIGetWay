from collections import OrderedDict

from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort, redirect
from flask_jwt_extended import jwt_required
from dotenv import dotenv_values
import requests

order_blueprint = Blueprint('order', __name__)
env_vars = dotenv_values('.env')

#Đơn hàng
@order_blueprint.route('/api/orders' , methods=['GET'])
# @jwt_required()
def order_get():
    try:
        url = env_vars.get('URL_ORDERS_GET')
        respone = requests.get(url)

        if respone.status_code == 200:
            req_data = respone.json(object_pairs_hook=OrderedDict)
            data = req_data.get('data')
            return jsonify(data), 200
        else:
            error_message = {
                "status": respone.status_code,
                "message": respone.json().get('message'),
                "data":[]
            }
            return jsonify(error_message),respone.status_code
    except Exception as e:
            error_message = {
                "status":500,
                "message":respone.json().get('message'),
            }
            return jsonify(error_message), 500
@order_blueprint.route('/api/orders/<id>' , methods=['GET'])
# @jwt_required()
def order_get_id(id):
    try:
        url = env_vars.get('URL_ORDERS_GET_ID')
        url = url.format(id)
        respone = requests.get(url)

        if respone.status_code == 200:
            req_data = respone.json(object_pairs_hook=OrderedDict)
            data = req_data.get('data')
            return jsonify(data), 200
        else:
            error_message = {
                "status": respone.status_code,
                "message": respone.json().get('message'),
                "data":[]
            }
            return jsonify(error_message),respone.status_code
    except Exception as e:
            error_message = {
                "status":500,
                "message":respone.json().get('message'),
            }
            return jsonify(error_message), 500
@order_blueprint.route('/api/orders' , methods=['POST'])
# @jwt_required()
def order_add():
    try:
        data = request.json  # Nhận đối tượng từ client
        response = requests.post(env_vars.get('URL_ORDERS_GET'), json=data)

        if response.status_code == 201:
            return jsonify(response.json()), 201
        else:
            return jsonify({"error": "Failed to create order"}), response.status_code

    except Exception as e:
            error_message = {
                "status":500,
                "message":'Internal Server'
            }
            return jsonify(error_message), 500

@order_blueprint.route('/api/orders/<id>' , methods=['PUT'])
# @jwt_required()
def order_update(id):
    try:
        url = env_vars.get('URL_ORDERS_GET_ID')
        url = url.format(id)
        data = request.json  # Nhận đối tượng từ client
        response = requests.put(url, json=data)

        if response.ok:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": "Failed to update order"}), response.status_code
    except Exception as e:
            error_message = {
                "status":500,
                "message":"Internal server",
            }
            return jsonify(error_message), 500

@order_blueprint.route('/api/orders/<id>' , methods=['DELETE'])
# @jwt_required()
def order_delete(id):
    try:
        url = env_vars.get('URL_ORDERS_GET_ID')
        url = url.format(id)
        respone = requests.delete(url)
        if respone.ok:
            return jsonify('Delete Succesful'), respone.status_code
        else:
            return jsonify('Delete fail'),respone.status_code
    except Exception as e:
            error_message = {
                "status":500,
                "message":respone.json().get('message'),
            }
            return jsonify(error_message), 500
# Chi tiết đơn hàng
@order_blueprint.route('/api/orders/<id>/order/detail_order', methods=['GET'])
def order_detail_get(id):
        try:
            url = env_vars.get('URL_ORDERS_DETAIL_ORDER')
            url = url.format(id)
            response = requests.get(url)
            print(url)
            if response.ok:
                req_data = response.json()
                data = req_data.get('data')
                return jsonify(data), 200
            else:
                error_message = {
                    "status": response.status_code,
                    "message": response.json().get('message'),
                    "data": []
                }
                return jsonify(error_message), response.status_code
        except Exception as e:
            error_message = {
                "status": 500,
                "message": response.json().get('message'),
            }
            return jsonify(error_message), 500

@order_blueprint.route('/api/orders/<id>/order/detail_order', methods=['POST'])
def order_detail_post(id):
        try:
            url = env_vars.get('URL_ORDERS_DETAIL_ORDER')
            url = url.format(id)
            data = request.json
            response = requests.post(url,json=data)
            if response.status_code==201:
                req_data = response.json()
                data = req_data.get('data')
                return jsonify(data), 201
            else:
                error_message = {
                    "status": response.status_code,
                    "message": response.json().get('message'),
                    "data": []
                }
                return jsonify(error_message), response.status_code
        except Exception as e:
            error_message = {
                "status": 500,
                "message": response.json().get('message'),
            }
            return jsonify(error_message), 500


@order_blueprint.route('/api/orders/<id>/order/detail_order/<idrem>', methods=['PUT'])
def order_detail_update(id,idrem):
        try:
            url = env_vars.get('URL_ORDERS_DETAIL_ORDER_ID')
            url = url.format(id,idrem)
            data = request.json
            response = requests.put(url,json=data)
            if response.ok:
                req_data = response.json()
                data = req_data.get('data')
                return jsonify(data), 200
            else:
                error_message = {
                    "status": response.status_code,
                    "message": response.json().get('message'),
                    "data": []
                }
                return jsonify(error_message), response.status_code
        except Exception as e:
            error_message = {
                "status": 500,
                "message": response.json().get('message'),
            }
            return jsonify(error_message), 500

@order_blueprint.route('/api/orders/<id>/order/detail_order/<idrem>', methods=['DELETE'])
def order_detail_delete(id,idrem):
        try:
            url = env_vars.get('URL_ORDERS_DETAIL_ORDER_ID')
            url = url.format(id,idrem)
            data = request.json
            response = requests.delete(url,json=data)
            if response.status_code != 201:
                error_message = {
                    "status": response.status_code,
                    "message": response.json().get('message'),
                    "data": []
                }
                return jsonify(error_message), response.status_code
        except Exception as e:
            error_message = {
                "status": 500,
                "message": response.json().get('message'),
            }
            return jsonify(error_message), 500