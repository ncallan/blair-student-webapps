from app import app, db

def ohgodnotinprod(value):
    HTMLStart = "<html><body style=\"background-color: #202; color: #fff;\"><center><code>"
    HTMLEnd = "</code></center></body></html>"
    return HTMLStart + str(value) + HTMLEnd


@app.route('/')
@app.route('/<what>/<where>')
@app.route('/select/<what>/<where>')
def select(what="*", where="jsonData"):
    return ohgodnotinprod(db.query("SELECT :what FROM :where", what=what, where=where).as_dict())

@app.route('/explain/<what>/<where>')
def explain(what="*", where="jsonData"):
    return ohgodnotinprod(db.query("EXPLAIN SELECT :what FROM :where", what=what, where=where).as_dict())

@app.route("/sms")
def sms():
    return """
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>""" + str(response.form) + """</Message>
</Response>
"""
