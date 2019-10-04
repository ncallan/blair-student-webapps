from app import app, db

def ohgodnotinprod(value)
    HTMLStart = "<html><body style=\"background-color: #202; color: #fff;\"><center><code>"
    HTMLEnd = "</code></center></body></html>"
    return HTMLStart + str(value) + HTMLEnd


@app.route('/')
@app.route('/<what>/<where>')
@app.route('/select/<what>/<where>')
def index(what="*", where="jsonData"):
    return ohgodnotinprod(db.query("SELECT :what FROM :where", what=what, where=where).export("html"))

@app.route('/explain/<what>/<where>')
def index(what="*", where="jsonData"):
    return ohgodnotinprod(db.query("EXPLAIN SELECT :what FROM :where", what=what, where=where).export("html"))
