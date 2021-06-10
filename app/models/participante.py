import datetime
from app import db, ma


"""Definição da tabela"""
class Participante(db.Model):
    MATRICULA = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NOME = db.Column(db.String(70), unique=False, nullable=False)
    CPF = db.Column(db.Integer, nullable=False)
    IDADE = db.Column(db.Integer, nullable=False)
    RG = db.Column(db.String(15), nullable=False)
    NOME_MAE = db.Column(db.String(70), nullable=False)
    DATA_NASCIMENTO = db.Column(db.Date, default=datetime.datetime.now())


"""Definindo o Schema do Marshmallow """
class ParticipantesSchema(ma.Schema):
    class Meta:
        fields = ('MATRICULA', 'NOME', 'CPF','IDADE','RG','NOME_MAE','DATA_NASCIMENTO')


participante_schema = ParticipantesSchema()
participantes_schema = ParticipantesSchema(many=True)