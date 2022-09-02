from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask import Flask
from flask_login.login_manager import LoginManager

from config import Config
app = Flask(__name__)
app.config.from_object(Config)

db=SQLAlchemy(app)
migrate=Migrate(app,db)
login = LoginManager(app,db)


# app = Flask(__name__)
# app.config.from_object(Config)
# db.init_app(app)
# migrate.init_app(app, db)
# login.init_app(app)

login.login_view = 'login'
login.login_message = 'Please Login or Register To Continue'
login.login_message_category = 'warning'
    
from app import routes, models