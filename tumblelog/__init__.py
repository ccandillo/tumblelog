from flask import Flask
from flask.ext.mongoengine import MongoEngine
from pymongo import read_preferences

DB_NAME = 'my_tumble_log'
DB_HOST = 'localhost'

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': DB_NAME,
    'HOST': DB_HOST,
    'read_preference': read_preferences.ReadPreference.PRIMARY
}
app.config['SECRET_KEY'] = 'KeepThisS3cr3t'

db = MongoEngine(app)

# Register blueprints
def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    app.register_blueprint(posts)

register_blueprints(app)


if __name__ == '__main__':
    app.run()
