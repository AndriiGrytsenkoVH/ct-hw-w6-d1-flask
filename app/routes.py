from app import app
from flask import render_template

@app.route("/")
def index():
    header = "This is flask header"
    return render_template("index.html", header=header)

@app.route("/games_list")
def games_list():
    games = ["Underrail","Synthetik","Rimworld","Subnautica","Almost everything made by Valve"]
    return render_template("games_list.html", games=games)