from flask import Blueprint, json, request, make_response, jsonify
from flask.views import MethodView
from ConfigAPI.core import app,DB
from ConfigAPI.JWT.JWTfunctions import JWT


JWT_blueprint = Blueprint('JWT', __name__)

class Login(MethodView):
          def post(self):
                    tocken = JWT.autenticate_and_return_json(request.json['user'],request.json['password'])
                    request.json['tocken'] = tocken
                    return request.json
          
          def get(self):
                    response = JWT.create_user(request.json['user'],request.json['password'])
                    request.json['tocken'] = response
                    return request.json

          def put(self):
                    response = JWT.checktocken(request.headers.get('user'),request.headers.get('Authorization'))
                    request.json['user'] = response
                    return request.json

Login_view = Login.as_view('Login_api')


JWT_blueprint.add_url_rule(
    '/Login',
    view_func=Login_view,
    methods=['POST','GET','PUT'])