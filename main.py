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
    return render_template('login.html', login_failed=False)

@app.route("/login")
def login():
    return render_template('login1.html', login_failed=False)

@app.route("/play")
def play():
    return render_template('play.html', utc_dt=datetime.datetime.utcnow())

@app.route("/success")
def app_page():
    return '<h1 style="color:green">Welcome to the APP</h1>'

@app.route("/failure")
def login_fail():
    return '<h1 style="color:red">FAIL</h1>'

@app.route('/process_form', methods=['POST'])
def process_form():
    print(request.form)
    # return f'GOT it <br /> {str(request.form)}'
    if request.form["txt_name"] == 'itay' and request.form["txt_password"] == '1234':
        return flask.redirect(url_for('app_page'))
    else:
        return flask.redirect(url_for('login_fail'))

@app.route('/process_form_one', methods=['POST'])
def process_form_one():
    print(request.form)
    # return f'GOT it <br /> {str(request.form)}'
    if request.form["txt_name"] == 'itay' and request.form["txt_password"] == '1234':
        return flask.redirect(url_for('app_page'))
    else:
        return render_template('login1.html', login_failed=True)

app.run(debug=True)