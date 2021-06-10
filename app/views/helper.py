import datetime
from functools import wraps
from app import app
from flask import request, jsonify
from .usuarios import auth_user,auth_user_name
import jwt
from werkzeug.security import check_password_hash

#função que faz a recuperação do token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'token is missing', 'data': []}), 401
        try:
            data=jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = auth_user_name(username=data['username'])
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': []}), 401
        return f(current_user, *args, **kwargs)
    return decorated


# Função para retornar o token do usuário
def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    user = auth_user(auth.username,auth.password)
    if not user:
        return jsonify({'message': 'user not found', 'data': []}), 401
    if user:
        token = jwt.encode({'username': user.USUARIO, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) },
                           app.config['SECRET_KEY'],algorithm="HS256")
        return jsonify({'message': 'Validated successfully', 'token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401