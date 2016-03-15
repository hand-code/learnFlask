from flask import Flask

import config
from filter import my_format_datetime,format_meta_keywords
from view import main_view

app = Flask(__name__)

def register_blueprint(app):
    app.register_blueprint(main_view.mv)

def register_jinjia_filters(app):
    app.jinja_env.filters['my_format_datetime'] = my_format_datetime
    app.jinja_env.filters['format_meta_keywords'] = format_meta_keywords

app.config.from_object(config)
register_blueprint(app)
register_jinjia_filters(app)