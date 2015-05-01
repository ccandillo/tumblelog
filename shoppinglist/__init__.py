from flask import Flask
from flask.ext.mongoengine import MongoEngine
from pymongo import read_preferences

DB_NAME = 'groceries'
DB_HOST = 'localhost'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'KeepThisS3cr3t'
app.config['MONGODB_SETTINGS'] = {
    'db': DB_NAME,
    'HOST': DB_HOST,
    'read_preference': read_preferences.ReadPreference.PRIMARY
}

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from shoppinglist.view import shoppinglists
    app.register_blueprint(shoppinglists)

register_blueprints(app)


if __name__ == '__main__':
    app.run()
