# accuweather keys
# API key = 8aaae57f966915b85ed963bd8af3866f
# COdes for openweather https://openweathermap.org/weather-conditions

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
from flask_login import LoginManager

app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///site.db'
app.config["SECRET_KEY"] = '07f6eb13ea9fc96e2a0a213a0e17becd'
db = SQLAlchemy(app) 
bcrypt = Bcrypt()
login_manager= LoginManager(app)
#sets the path for the login view (used in @login_required)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info' 

from app import routes