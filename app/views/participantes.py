from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.participante import Participante, participante_schema, participantes_schema


"""Retorna lista de participantes"""
def get_participantes():
    cpf = request.args.get('cpf')
    if cpf:
        users = Participante.query.filter(Participante.CPF== int(cpf)).all()
    else:
       # users = Participante.query.all()
        return jsonify({'message': 'nothing found', 'data': {}})
    if users:
        result = participantes_schema.dump(users)
        return jsonify({'message': 'successfully fetched', 'data': result})

    return jsonify({'message': 'nothing found', 'data': {}})



