from app import app, db

@app.route('/')
@app.route('/<name>')
def index(name="boi"):
    return "<html><body style=\"background-color: #202; color: #fff;\"><center><code>" + str([[i.id, i.data] for i in db.query("SELECT * FROM jsonData")]) + "</code></center></body></html>"
