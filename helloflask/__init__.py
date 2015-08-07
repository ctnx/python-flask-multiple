from flask import Flask

app = Flask(__name__)


UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'super_secret_key'

from helloflask import views
from helloflask.auth import auth_blueprint

app.register_blueprint(auth_blueprint)
