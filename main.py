import datetime

import flask
from flask import Flask, render_template, url_for, request
from flask import Flask, render_template, request, jsonify, make_response, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# localhost:5000/
@app.route("/")
def home():
    return flask.redirect(url_for('login'))

@app.route("/login")
def login():
    return render_template('login.html', login_failed=False)

@app.route("/signup")
def play():
    return render_template('signup.html', bad_repeat = False)

@app.route("/signup_process", methods=['POST'])
def handle_signup():
    if request.form["psw"] != request.form["psw-repeat"]:
        return render_template('signup.html', bad_repeat = True)
    # check if user not already exist in db
    # check if password length is not too short (optional*)
    session['remember'] = request.form.get('remember')
    return str(session['remember'])
app.run(debug=True)