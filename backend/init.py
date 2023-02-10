from flask import Flask
from turbo_flask import Turbo

turbo = Turbo()

def create_app():
    app = Flask(__name__)

    turbo.init_app(app)

    return app
