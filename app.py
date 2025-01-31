from flask import Flask,render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
app = Flask("__name__")
app.config['SECRET_KEY']="some secret key"#this is WTForm CSRF token (pg-10,MKGVI)
#-----------------------------------------------------------creating a form class
class NameForm(FlaskForm):
    name = StringField("EnterName",validators=[DataRequired()])
    submit = SubmitField("Submit")
#----------------------------------------------------------------route decorators
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    name = None #because initially name field will be empty
    form = NameForm()
    if form.validate_on_submit():#validate form(pg-10,MKGVI)
        name = form.name.data
        form.name.data = ''
        flash("Your form is submitted successfully.")#(pg-11,MKGVI)
    return render_template("login.html",
    name=name,form=form)
#------------------------------------------------------------------Error handling
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