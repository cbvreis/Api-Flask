from app import app
from flask import jsonify
from ..views import helper,participantes

""""""""""""""""""""""""""""""""""""""""""
"    CLASSE ROTEADORA                    "
""""""""""""""""""""""""""""""""""""""""""
#Função hello world para teste da autenticação
@app.route('/v1', methods=['GET'])
@helper.token_required
def root(current_user):
    return jsonify({'message': f'Hello {current_user.NOME}'})

#Função que chama os participantes
@app.route('/v1/participantes', methods=['GET'])
@helper.token_required
def get_one_participante(current_user):
    return participantes.get_participantes()

#Função de chamada para autenticação
@app.route('/v1/authenticate', methods=['POST'])
def authenticate():
    return helper.auth()