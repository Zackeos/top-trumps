from flask import Flask, render_template, redirect, request_started, url_for, request

app = Flask(__name__)

@app.route('/')
def mainPage():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template("home.html", title = "Home")



app.run(host='0.0.0.0', port=5002)