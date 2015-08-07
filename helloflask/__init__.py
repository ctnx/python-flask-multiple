from flask import Flask

app = Flask(__name__)

from helloflask import views

UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'super_secret_key'
