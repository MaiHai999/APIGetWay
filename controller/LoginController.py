from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort, redirect

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity, get_jwt
from flask_jwt_extended import jwt_required

from sevices.UserHandler import UserHandler

login_blueprint = Blueprint('login', __name__)
user_handler = UserHandler()

@login_blueprint.route('/login' , methods=['POST'])
def login():
    try:
        #Lấy các tham số
        email = request.json.get('email')
        password = request.json.get('password')
        check = user_handler.check(email , password)

        #tạo tokens
        if check is False:
            return jsonify({"msg": "That Bai"}), 408
        else:
            iden_info = {
                "id_user": "maihai"
            }

            access_token = create_access_token(identity=iden_info, fresh=True)
            refresh_token = create_refresh_token(identity=iden_info)
            return jsonify(access_token=access_token, refresh_token=refresh_token) , 200

    except Exception as e:
        error_message = "Error: {}".format(str(e))
        response = jsonify({"error": error_message})
        return response, 500

@login_blueprint.route("/refresh_access", methods=["POST"])
@jwt_required(refresh=True)
def refresh_access():
    try:
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return jsonify(access_token=access_token)

    except Exception as e:
        error_message = "Error: {}".format(str(e))
        response = jsonify({"error": error_message})
        return response, 500

@login_blueprint.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    try:
        identity = get_jwt_identity()
        refresh_token = create_refresh_token(identity=identity)
        return jsonify(refresh_token=refresh_token)
    except Exception as e:
        error_message = "Error: {}".format(str(e))
        response = jsonify({"error": error_message})
        return response, 500