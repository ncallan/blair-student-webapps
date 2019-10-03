from app import app
import os
from records import Database

@app.route('/')
@app.route('/<name>')
def index(name="boi"):
    return "<html><body bgcolor=\"#202\" color=\"#fff\"><center>Hello, " + name + ".</center></body></html>"
