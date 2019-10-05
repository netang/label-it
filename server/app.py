from flask import Flask
from flask_cors import CORS
from flask_hashing import Hashing
from models import db


app = Flask(__name__)

hashing = Hashing(app)

# DB connection configuration
POSTGRES = {
    'user': 'postgres',
    'pw': 'rtr1',
    'db': 'label_it',
    'host': 'localhost',
    'port': '5432'
}
db_uri = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

""" Flask application to enable Cross Origin Resource Sharing (CORS).
Anytime a client makes a request for a resource that resides on another machine as defined by
protocol, IP address / domain name, or port number then additional headers associated with CORS must be added. """
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SECRET_KEY'] = 'dgdfg454567egfdgs'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db.init_app(app)

from api.tasks import tasks_module
app.register_blueprint(tasks_module)