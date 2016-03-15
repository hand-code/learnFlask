# coding=utf-8
from flask.blueprints import Blueprint
from flask import render_template_string
from flask import render_template

mv = Blueprint('main_bp',__name__)

@mv.route('/')
@mv.route('/index')
def index():
    return render_template(u'index.html')