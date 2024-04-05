from flask import Flask
from flask_cors import CORS
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_database()

app = Flask(__name__)
CORS(app)

# a ordem do import afeta o funcionamento; Caso este import seja movido para cima, ocorre erro no momento de exec do app.py
from src.main.routes.event_routes import event_routes_bp
app.register_blueprint(event_routes_bp)