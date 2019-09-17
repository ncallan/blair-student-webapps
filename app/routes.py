from app import app

@app.route('/')
@app.route('/<name>')
def index(name="boi"):
    return name
