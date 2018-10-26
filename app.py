#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from setup_database import Base, Movie, User
from recommender_system import recommender_system

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

@app.route("/movienight/movierecommender/", methods=["GET", "POST"])
def recommend_movie():
    if request.method == "POST":
        if request.form.get("random"):
            recommendation = db.session.query(Movie).order_by(func.random()).first()
        if request.form.get("recommend"):
            try:
                rec_title = recommender_system(dict(request.form))
            except ValueError:
                # ADD FLASH MESSAGE THAT RESTRICTIONS WERE TOO NARROW OR 
                # DATE RANGE WAS INCORRECT
                return render_template("movie_recommender.html")
            recommendation = db.session.query(Movie).filter_by(title=rec_title).one()
        return redirect(url_for("movie_recommendation_page", movieId=recommendation.movieId))
    else:
        return render_template("movie_recommender.html")

@app.route("/movienight/movierecommender/recommended_movie/<int:movieId>/")
def movie_recommendation_page(movieId):
    movie = db.session.query(Movie).filter_by(movieId=movieId).one()
    return render_template("recommended_movie.html", movie=movie)

@app.route("/lookingforsomeone/")
def recommend_partner():
    return render_template("looking_for_someone.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)