from flask import Flask

# Import (and init) config
from . import config

# Init flask app
app = Flask(__name__)

# Import routes
from . import routes

def run():
    conf = config.get()
    app.run(debug=conf.get('debug', False), host=conf.get('host', '0.0.0.0'), port=conf.get('port', 80))