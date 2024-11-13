from flask import Flask, render_template
from math import sqrt
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Word"

@app.route("/pagina1/<nome>")
def pagina1(nome):
    return render_template("pagina.html", nomePessoa=nome)

@app.route("/pagina2")
def.pagina2():
    return render_template("pagina2.html")

@app.post("/bhaskara")
def bhaskara():
    a = float(request.form.get("a"))
    b = float(request.form.get("b"))
    c = float(request.form.get("c"))

    delta = b**2 - 4 * a * c

    if delta >= 0:
        x1= (-b + sqrt(delta)) / 2 * a
        x2= (-b - sqrt(delta)) / 2 * a
        return f"X1 = {x1} e X2 = {x2}"
        
app.run(port=80, debug=True)