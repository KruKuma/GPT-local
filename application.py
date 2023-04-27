import flask

import routing

app_config = {
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

application = flask.Flask(__name__)
application.config.from_mapping(app_config)
router = routing.Router(application)
router.define_routing()
