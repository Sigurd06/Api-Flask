from flask import json, jsonify, request, make_response, current_app
from marshmallow.exceptions import ValidationError
from datetime import datetime, timedelta
from flask_restful import Resource, Api
from app.lib.jwt_token import token_required
import jwt

from .schema import auth_schema
from .model import User
from . import auth_bp

api = Api(auth_bp)

class Signup(Resource):
    def post(self):
        data = request.get_json()
        try:
            auth_dic = auth_schema.load(data)
            user = User.query.filter_by(username=auth_dic['username']).first()
            
            if user is None:
                user = User(username=auth_dic['username'], password=auth_dic['password'])
                user.save()
                return make_response(jsonify({
                    'status': 201,
                    'message': 'Registro Exisoto!'
                }), 201)
            else:
                return make_response(jsonify({
                    'status': 400,
                    'message': 'Nombre de usuario en uso.'
                }), 400)

        except ValidationError as err:
            return make_response(jsonify({
                'status': 400,
                'message': err.messages
            }))
    
class Signin(Resource):
    def post(self):
        data = request.get_json()
        try:
            auth_dic = auth_schema.load(data)
            user = User.query.filter_by(username=auth_dic['username']).first()
            
            if user is not None and user.verify_password(auth_dic['password']):
                exp = datetime.now() + timedelta(days=1) 
                payload = {
                    'id': user.id,
                    'username': user.username,
                    'exp': exp
                }
                TOKEN = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")
                return make_response(jsonify({
                    'status': 200,
                    'message': 'Haz iniciado sesión exitosamente.',
                    'token': TOKEN
                }), 200)
            else:
                return make_response(jsonify({
                    'status': 400,
                    'message': 'Credenciales incorrectas',
                }), 400)

        except ValidationError as err:
            return make_response(jsonify({
                'status': 400,
                'message': err.messages
            }))

class Profile(Resource):
    method_decorators = { 'get': [token_required]}
    
    def get(self, current_user):

        return make_response(jsonify({
            'status': 200,
            'user_info': {
                'id': current_user.id,
                'username': current_user.username
            }
        }), 200)

api.add_resource(Signup, '/signup')
api.add_resource(Signin, '/signin')

api.add_resource(Profile, '/me')