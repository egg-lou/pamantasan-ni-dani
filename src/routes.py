from flask import Flask, render_template, redirect, url_for, request
from .app import db, mail
from .models import Subscribe
from flask import send_from_directory
from flask_mail import Message
from dotenv import load_dotenv
import os
load_dotenv('.env')

email_sender = os.getenv('EMAIL')

def init_app(app):

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/subscribe_newsletter', methods=['POST'])
    def send_email():
        recipient = request.form.get('email')

        msg = Message("Hello", sender=email_sender, recipients=[recipient])
        msg.body = "This is a message from flask"
        mail.send(msg)
        print(recipient)
        print("Email sent")

        return redirect(url_for('index'))
    