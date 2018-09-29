#!/usr/bin/env python3

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from setup_database import Base, Link, Movie, Rating, Tag, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/movienight/")
def movie_night():
	return render_template("movie_night.html")

@app.route("/movienight/movielist/")
def show_movies():
	movies = db.session.query(Movie).all()
	return render_template("movie_list.html", movies=movies)

@app.route("/movienight/recommendedmovie/")
def recommend_movie():
	return render_template("recommended_movie.html")

@app.route("/lookingforsomeone/")
def recommend_partner():
	return render_template("looking_for_someone.html")

if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port=5000)