from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<body bgcolor=\"#202\"><p color=\"#fff\">oh hai</p></body>"
