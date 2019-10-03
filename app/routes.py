from app import app
import os

@app.route('/')
@app.route('/<name>')
def index(name="boi"):
    return os.environ["DATABASE_URL"]
