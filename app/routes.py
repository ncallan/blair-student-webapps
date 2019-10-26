from app import app, db

def ohgodnotinprod(value):
    HTMLStart = "<html><body style=\"background-color: #202; color: #fff;\"><center><code>"
    HTMLEnd = "</code></center></body></html>"
    return HTMLStart + str(value) + HTMLEnd


@app.route('/<name>')
def index(name):
    return ohgodnotinprod("Hi " + name + ".")

@app.route('/<what>/<where>')
@app.route('/select/<what>/<where>')
def select(what="*", where="jsondata"):
    return ohgodnotinprod(db.query("SELECT :what FROM :where", what=what, where=where).as_dict())

@app.route('/explain/<what>/<where>')
def explain(what="*", where="jsondata"):
    return ohgodnotinprod(db.query("EXPLAIN SELECT :what FROM :where", what=what, where=where).as_dict())

@app.route("/sms")
def sms():
    return """
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Media>""" + str("https://img.ifunny.co/images/b685b26cb8d1c4563636a5becdfbce6a064d3ecdff2f34cf14a84bbfbbc4b97d_1.jpg") + """</Media>
</Response>
"""
