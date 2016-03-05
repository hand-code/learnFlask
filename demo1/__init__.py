from werkzeug.utils import secure_filename
from flask import Flask, url_for, render_template,request
from flask import redirect

__author__ = 'chenxiaofeng'

app = Flask(__name__)

from demo1 import views