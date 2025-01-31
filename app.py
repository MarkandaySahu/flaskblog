from flask import Flask,render_template

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

#for any other exception
@app.errorhandler(Exception)
def handle_exception(e):
    return render_template("error.html",error=e), 500