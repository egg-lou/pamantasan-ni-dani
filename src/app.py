from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
load_dotenv('.env')

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__, template_folder="templates")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    email = os.environ.get('EMAIL')
    password = os.environ.get('PASSWORD')

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = email
    app.config['MAIL_PASSWORD'] = password
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app