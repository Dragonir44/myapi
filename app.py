from flask import Flask, render_template, request
from Data.films import pictures
import random

app = Flask(__name__)

@app.route('/api/pictures')
def getFilms():
    return render_template("home.html", pictures=pictures)

@app.route('/api/picture/<id>')
def getFilm(id):
    for picture in pictures:
        if picture["id"] == int(id):
            return render_template("picture.html", picture=picture)
    return "Film not found"

@app.route('/api/shuffle')
def getShuffledFilms():
    random.shuffle(pictures)
    return render_template("home.html", pictures=pictures)