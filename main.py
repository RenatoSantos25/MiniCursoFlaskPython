from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Word"

@app.route("/pagina1")

def pagina1():
    return render_template("pagina.html")



app.run(port=80, debug=True)