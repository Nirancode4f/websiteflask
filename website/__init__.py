from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
import time
from datetime import datetime


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'adhfasdfas'
    
    from .views import views
    from .auth import auth 
    from .errors.handles import errors

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    app.register_blueprint(errors)
    return app