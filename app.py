from database import *
from flask import Flask, request, redirect, render_template, Response, send_file, url_for, flash
from flask import session as login_session
import json
from functools import wraps
from datetime import datetime, timedelta 

app = Flask(__name__)
app.config['SECRET_KEY'] = "a;lfkdsjaflksdj"

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        print("status",get_status())
        return render_template("home.html", status = get_status())
    else:
        print("request form", request.form)
        set_status(request.form["state"], request.form["label"])
        return render_template("home.html", status = get_status())


@app.route('/set_status', methods = ['POST'])
def server_set_status():
    print("request form", request.form)
    set_status(request.form["state"], request.form["label"])
    return f'{request.form["state"]},{request.form["label"]}'

@app.route('/get_status')
def server_get_status():
    return get_status().state



if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
