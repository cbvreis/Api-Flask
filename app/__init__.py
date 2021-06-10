from flask import Flask,jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)


from .models import usuarios,participante
from .views import  helper,usuarios,participantes
from .routes import routes

