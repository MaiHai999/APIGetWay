
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort, redirect
from flask_jwt_extended import jwt_required
from dotenv import dotenv_values
import requests
from config import Config

product_blueprint = Blueprint('product', __name__)
config = Config()

@product_blueprint.route('/product_get' , methods=['GET','POST'])
def product_get():
    try:
        url = config.URL_PRODUCT_GET
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


@product_blueprint.route('/product_get_id' , methods=['GET','POST'])
def product_get_id():
    try:
        data = request.json
        id = data['id']
        url = config.URL_PRODUCT_GET_ID
        payload = {'id': id}

        response = requests.get(url, json= payload)

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

@product_blueprint.route('/find', methods=['GET', 'POST'])
def find_product():
    try:
        data = request.json
        keyword = data['keyword']

        url = config.URL_PRODUCT_FIND
        payload = {'keyword': keyword}

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


@product_blueprint.route('/product_get_loai' , methods=['GET','POST'])
def product_get_loai():
    try:
        data = request.json
        id = data['id']
        url = config.URL_PRODUCT_GET_LOAI
        payload = {'id': id}

        response = requests.get(url, json= payload)

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


@product_blueprint.route('/loai_rem' , methods=['GET','POST'])
def product_get_all_loai():
    try:
        url = config.URL_PRODUCT_ALL_LOAI

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

@product_blueprint.route('/comment' , methods=['GET','POST'])
def comment():
    try:
        data = request.json
        noidung = data['noidung']
        sosao = data['sosao']
        email = data['email']
        ten = data['ten']
        idsp = data['idsp']

        data_to_send = {
            'noidung': noidung,
            'sosao': sosao,
            'email': email,
            'ten': ten,
            'idsp': idsp
        }

        url = config.URL_PRODUCT_COMMENT
        response = requests.get(url, json=data_to_send)

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

@product_blueprint.route('/product_add' , methods=['GET','POST'])
@jwt_required()
def product_add():
    try:
        data = request.json
        ten = data['tenremcua']
        donvi = data['donvi']
        xuatxu = data['xuatxu']
        baohanh = data['baohanh']
        kichthuoc = data['kichthuoc']
        chatlieu = data['chatlieu']
        so_luong = int(data['so_luong'])
        id_loairem = int(data['idloairem'])
        gia_goc = float(data['gia'])
        image_base64 = data['hinh_anh']

        product_data = {
            'tenremcua': ten,
            'donvi': donvi,
            'xuatxu': xuatxu,
            'baohanh': baohanh,
            'kichthuoc': kichthuoc,
            'chatlieu': chatlieu,
            'so_luong': so_luong,
            'idloairem': id_loairem,
            'gia': gia_goc,
            'hinh_anh': image_base64
        }


        url = config.URL_PRODUCT_ADD
        response = requests.get(url, json=product_data)


        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            error_message = {'error': 'Failed to fetch data'}
            return jsonify(error_message), response.status_code

    except Exception as e:
        print(e)
        error_message = "Error: {}".format(str(e))
        response = jsonify({"error": error_message})
        return response, 500

@product_blueprint.route('/product_update' , methods=['GET','POST'])
@jwt_required()
def product_update():
    try:
        data = request.json
        id = data['id']
        ten = data['tenremcua']
        donvi = data['donvi']
        xuatxu = data['xuatxu']
        baohanh = data['baohanh']
        kichthuoc = data['kichthuoc']
        chatlieu = data['chatlieu']
        so_luong = data['so_luong']
        id_loairem = int(data['idloairem'])
        gia_goc = float(data['gia'])
        image_base64 = data['hinh_anh']


        product_data = {
            'id':id,
            'tenremcua': ten,
            'donvi': donvi,
            'xuatxu': xuatxu,
            'baohanh': baohanh,
            'kichthuoc': kichthuoc,
            'chatlieu': chatlieu,
            'so_luong': so_luong,
            'idloairem': id_loairem,
            'gia': gia_goc,
            'hinh_anh': image_base64
        }

        url = config.URL_PRODUCT_UPDATE
        response = requests.get(url, json=product_data)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            error_message = {'error': 'Failed to fetch data'}
            return jsonify(error_message), response.status_code

    except Exception as e:
        print(e)
        error_message = "Error: {}".format(str(e))
        response = jsonify({"error": error_message})
        return response, 500

@product_blueprint.route('/product_del' , methods=['GET','POST'])
@jwt_required()
def product_del():
    try:
        data = request.json
        id = data['id']

        url = config.URL_PRODUCT_DEL
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




