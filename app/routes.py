from app import app
import os
from records import Database

@app.route('/')
@app.route('/<name>')
def index(name="boi"):
    return os.environ["DATABASE_URL"]
