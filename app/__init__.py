import os

from records import Database
from flask import Flask

app = Flask(__name__)
db = Database(os.environ["DATABASE_URL"])

from app import routes
