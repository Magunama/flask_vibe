import jwt
from flask import Blueprint, request, jsonify, current_app
from werkzeug.exceptions import Unauthorized

from app.service.auth_service import AuthService

auth_blueprint = Blueprint('auth', __name__, url_prefix="/auth")


@auth_blueprint.route("/login", methods=["POST"])
async def login():
    auth = request.authorization
    matching_user = await AuthService.look_up_user(**auth)
    if not matching_user:
        raise Unauthorized()

    secret_key = current_app.config["SECRET_KEY"]
    auth_token = AuthService.encode_auth(matching_user.id, secret_key)

    print(jwt.decode(auth_token, secret_key, algorithms=["HS256"]))

    return jsonify({"token": auth_token})
