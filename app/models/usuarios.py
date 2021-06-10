import datetime
from app import db, ma


"""Definição da tabela"""
class Auth(db.Model):
    USUARIO = db.Column(db.String(50),primary_key=True, unique=True, nullable=False)
    KEY = db.Column(db.String(50), nullable=False)
    OBSERVACAO = db.Column(db.String(50), nullable=False)


"""Definindo o Schema do Marshmallow """
class UsariosSchema(ma.Schema):
    class Meta:
        fields = ('USUARIO', 'KEY', 'OBSERVACAO')


usuario_schema = UsariosSchema()
usuarios_schema = UsariosSchema(many=True)