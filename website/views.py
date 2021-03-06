import os
from werkzeug.wrappers import response
from website import app
from flask import render_template, url_for, request, jsonify
from grandpy.app import App

@app.route("/")
def homepage():
    return render_template("index.html", google_key=os.getenv("GOOGLE_FRONT_API_KEY"))

@app.route("/grandpy", methods=["POST"])
def grandpy():
    user_text = request.data.decode()
    parser = App()
    response = parser.answer(user_text)
    return jsonify(response)
