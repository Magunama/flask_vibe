from time import strftime

import werkzeug
from flask import Blueprint, jsonify, current_app as app, request
from flask_restx import Api, Resource

default_blueprint = Blueprint('default', __name__)

version = "1.0"
api = Api(
    default_blueprint,
    title='Flask Vibe',
    version=version,
    description=f'Welcome to Flask Vibe v{version}'
)


@api.route("/hello/")
class HelloWorld(Resource):
    # @api.doc("hello")
    @api.response(200, 'Success')
    def get(self):
        return {"hello": "world"}


@default_blueprint.app_errorhandler(werkzeug.exceptions.NotFound)
def resource_not_found(e):
    """APP Error Handler"""
    return jsonify(error=str(e)), 404


@default_blueprint.app_errorhandler(werkzeug.exceptions.Unauthorized)
def unauthorized_access(e):
    """APP Error Handler"""
    return jsonify(error=str(e)), 401


@default_blueprint.app_errorhandler(werkzeug.exceptions.NotAcceptable)
def headers_not_acceptable(e):
    """APP Error Handler"""
    return jsonify(error=str(e)), 406


@default_blueprint.after_app_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    app.logger.info('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme,
                    request.full_path, response.status)
    return response
