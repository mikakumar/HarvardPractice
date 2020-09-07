import datetime

from flask import Flask, render_template, request, session
from flask_session.__init__ import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"

Session(app)


notes = []
session["notes"] = []

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/<string:name>")
def nindex(name):
	name = name.capitalize()
	return render_template("index.html", name=name)

@app.route("/newyear")
def ncheck():
	now = datetime.datetime.now()
	newyear = now.day == 1 and now.month == 1
	if newyear: 
		ntext = "YES"
		return render_template("index.html", newyear=ntext)
	else: 
		ntext = "NO"
		time = now.strftime("%Y/%m/%d, %H:%M:%S")
		return render_template("index.html", newyear=ntext, time=time)

@app.route("/notes", methods=["GET", "POST"])
def notes():
	if request.method == "POST":
		note = request.form.get("note")
		session["notes"].append(note)
		return render_template("index.html", notes=session["notes"])
	else:
		return "Please submit the form instead."