from controller.ProductController import product_blueprint
from controller.LoginController import login_blueprint
from controller.PromotionController import promotion_blueprint

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

import os

app = Flask(__name__)
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app.config["JWT_SECRET_KEY"] = "aasdfsadfkjnoiawj1977"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

app.register_blueprint(product_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(promotion_blueprint)


CORS(app)
jwt = JWTManager(app)


@app.route('/')
def index():
    response = jsonify({"msg": "Test successfully"})
    return response, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5555)