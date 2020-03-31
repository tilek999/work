from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def homepage():
    return "<h1>welcome to shop<h1>"

@app.route("/1")   
def asd():
    return render_template("1.html") 

@app.route("/abc,<name>")  
def bsd(name):
    name = name.capitalize()
    return render_template("abc.html", name = name)  

