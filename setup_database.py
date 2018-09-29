#!/usr/bin/env python3

# Create SQLite database consisting of all datasets

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
import pandas as pd

Base = declarative_base()

class Link(Base):

	__tablename__ = "link"
	linkId = Column(Integer, primary_key=True)
	movieId = Column(Integer, ForeignKey("movie.movieId"))
	imdbId = Column(Integer)
	tmdbId = Column(Integer)

class Movie(Base):

	__tablename__ = "movie"
	movieId = Column(Integer, primary_key=True)
	title = Column(String(250))
	genres = Column(String(250))

class Rating(Base):

	__tablename__ = "rating"
	ratingId = Column(Integer, primary_key=True)
	userId = Column(Integer, ForeignKey("user.userId"))
	movieId = Column(Integer, ForeignKey("movie.movieId"))
	rating = Column(Integer)
	timestamp = Column(Integer)

class Tag(Base):

	__tablename__ = "tag"
	tagId = Column(Integer, primary_key=True)
	userId = Column(Integer, ForeignKey("user.userId"))
	movieId = Column(Integer, ForeignKey("movie.movieId"))
	tag = Column(String(250))
	timestamp = Column(Integer)

class User(Base):

	__tablename__ = "user"
	userId = Column(String(250), primary_key=True)
	name = Column(String(250))
	gender = Column(String(6))
	age = Column(Integer)

def main():

	engine = create_engine("sqlite:///movies.db")
	Base.metadata.create_all(engine)
	links = pd.read_csv("imported_datasets/links.csv")
	links.to_sql("link", 
		         con=engine, 
		         if_exists="append", 
		         index_label="linkId")
	movies = pd.read_csv("imported_datasets/movies.csv")
	movies.to_sql("movie", 
		          con=engine, 
		          if_exists="append", 
		          index=False)
	ratings = pd.read_csv("imported_datasets/ratings.csv")
	ratings.to_sql("rating", 
		           con=engine, 
		           if_exists="append", 
		           index_label="ratingId")
	tags = pd.read_csv("imported_datasets/tags.csv")
	tags.to_sql("tag", 
		        con=engine, 
		        if_exists="append", 
		        index_label="tagId")
	users = pd.read_csv("users.csv")
	users.to_sql("user", 
		         con=engine, 
		         if_exists="append", 
		         index=False)

if __name__ == "__main__":
	main()