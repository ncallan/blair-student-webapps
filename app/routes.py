from app import app
import os
from records import Database

@app.route('/')
@app.route('/<name>')
def index(name="boi"):
    return "<html><body bgcolor=\"#202\" color=\"#fff\"><center><p>Hello, " + name + ".</p></center></body></html>"
