from flask import Flask
from pathlib import Path
import os
import pyrebase
import firebase_admin
from firebase_admin import credentials

key_path = Path(__file__).resolve()
key_path = key_path.parent.parent
key_path = key_path.joinpath('ffsite/key/serviceAccountKey.json').__str__()
cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred)

config ={
    'apiKey': "AIzaSyANowCknqQtfkKjzeQBTmfVq0FStjLzc7E",
    'authDomain': "fungi-fantasia.firebaseapp.com",
    'projectId': "fungi-fantasia",
    'storageBucket': "fungi-fantasia.appspot.com",
    'messagingSenderId': "165617223999",
    'appId': "1:165617223999:web:cabafd87a41744f2912b8a",
    'databaseURL': "fungi-fantasia.appspot.com"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DEBUG = True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import home
    app.register_blueprint(home.bp)

    from . import about
    app.register_blueprint(about.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
