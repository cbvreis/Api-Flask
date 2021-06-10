from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.usuarios import Auth, usuario_schema, usuarios_schema

"""
    FUNÇÃO PARA AUTENTICAÇAO DO USUÁRIO
"""
def auth_user(username, key):
    try:
        return Auth.query.filter(Auth.USUARIO == username and Auth.KEY == key).one()
    except:
        return None

"""
    FUNÇÃO PARA RETORNAR O NOME DO USUARIO
"""
def auth_user_name(username):
    try:
        return Auth.query.filter(Auth.USUARIO == username).one()
    except:
        return None