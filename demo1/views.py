from demo1 import app

@app.route('/hello')
def index():
    return 'hello,world'