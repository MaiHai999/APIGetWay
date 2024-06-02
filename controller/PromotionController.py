from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort, redirect
from flask_jwt_extended import jwt_required
from dotenv import dotenv_values
import requests

promotion_blueprint = Blueprint('promotion', __name__)
env_vars = dotenv_values('.env')

@promotion_blueprint.route('/promotion_get' , methods=['GET','POST'])
def promotion_get():
    try:
        url = env_vars.get('URL_PROMOTION_GET')
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            error_message = {'error': 'Failed to fetch data'}
            return jsonify(error_message), response.status_code

    except Exception as e:
        error_message = "Error: {}".format(str(e))
        response = jsonify({"error": error_message})
        return response, 500

@promotion_blueprint.route('/promotion_add' , methods=['GET','POST'])
@jwt_required()
def promotion_add():
    try:
        data = request.json
        ten = data.get('ten')
        ngaybatdau_str = data.get('ngaybatdau')
        ngayketthuc_str = data.get('ngayketthuc')
        phantram = float(data.get('phantram'))
        list_rem = data.get('id_rem')

        data_dict = {
            'ten': ten,
            'ngaybatdau': ngaybatdau_str,
            'ngayketthuc': ngayketthuc_str,
            'phantram': phantram,
            'id_rem': list_rem
        }

        url = env_vars.get('URL_PROMOTION_ADD')
        response = requests.get(url, json=data_dict)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            error_message = {'error': 'Failed to fetch data'}
            return jsonify(error_message), response.status_code

    except Exception as e:
        error_message = "Error: {}".format(str(e))
        response = jsonify({"error": error_message})
        return response, 500

@promotion_blueprint.route('/promotion_get_id' , methods=['GET','POST'])
def promotion_get_id():
    try:
        data = request.json
        id = data['id']

        url = env_vars.get('URL_PROMOTION_GET_ID')
        payload = {'id': id}

        response = requests.get(url, json=payload)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            error_message = {'error': 'Failed to fetch data'}
            return jsonify(error_message), response.status_code

    except Exception as e:
        error_message = "Error: {}".format(str(e))
        response = jsonify({"error": error_message})
        return response, 500

@promotion_blueprint.route('/promotion_update' , methods=['GET','POST'])
@jwt_required()
def promotion_update():
    try:
        data = request.json

        id = data.get('id')
        ten = data.get('ten')
        ngaybatdau_str = data.get('ngaybatdau')
        ngayketthuc_str = data.get('ngayketthuc')
        phantram = float(data.get('phantram'))
        list_rem = data.get('id_rem')

        data_dict = {
            'id' : id,
            'ten': ten,
            'ngaybatdau': ngaybatdau_str,
            'ngayketthuc': ngayketthuc_str,
            'phantram': phantram,
            'id_rem': list_rem
        }

        url = env_vars.get('URL_PROMOTION_UPDATE')
        response = requests.get(url, json=data_dict)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            error_message = {'error': 'Failed to fetch data'}
            return jsonify(error_message), response.status_code

    except Exception as e:
        error_message = "Error: {}".format(str(e))
        response = jsonify({"error": error_message})
        return response, 500

@promotion_blueprint.route('/promotion_del' , methods=['GET','POST'])
@jwt_required()
def promotion_del():
    try:
        data = request.json
        id = data['id']

        url = env_vars.get('URL_PROMOTION_DEL')
        payload = {'id': id}

        response = requests.get(url, json=payload)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            error_message = {'error': 'Failed to fetch data'}
            return jsonify(error_message), response.status_code
    except Exception as e:
        error_message = "Error: {}".format(str(e))
        response = jsonify({"error": error_message})
        return response, 500







