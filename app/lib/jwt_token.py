from flask import request, jsonify, make_response, current_app
from ..resources.auth.model import User
from app.resources.auth.schema import auth_schema

from functools import wraps
import jwt

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs): 
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        
        if not token:
            return make_response(jsonify({
                'status': 403,
                'message': 'Acceso prohibido, inicia sesión'
            }), 403)
        
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms="HS256")
            # print(data)
            current_user = User.get_by_id(data['id'])
            
        except:
            return make_response(jsonify({
                    'status': 400,
                    'message': 'Token invalido'
            }), 400)
        
        return f(current_user, *args, **kwargs)
    
    return decorator
   