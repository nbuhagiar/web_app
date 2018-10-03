#!/usr/bin/env python3

# Create SQLite database consisting of all datasets

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy import create_engine
import pandas as pd

Base = declarative_base()

class Movie(Base):

	__tablename__ = "movie"
	movieId = Column(Integer, primary_key=True)
	imdbId = Column(Integer)
	imdbLink = Column(String(250))
	title = Column(String(250))
	imdbScore = Column(Float)
	genres = Column(String(250))
	poster = Column(String(250))
	year = Column(Integer)

class User(Base):

	__tablename__ = "user"
	userId = Column(String(250), primary_key=True)
	name = Column(String(250))
	gender = Column(String(6))
	age = Column(Integer)

def main():

	engine = create_engine("sqlite:///movies.db")
	Base.metadata.create_all(engine)
	movies = pd.read_csv("MovieGenre.csv", encoding="latin-1")
	movies[["title", "year"]] = pd.DataFrame(movies["Title"].str
		                                                    .rsplit(" ", 1)
		                                                    .values
		                                                    .tolist())
	movies.drop("Title", axis=1, inplace=True)
	movies.columns = ["imdbId", 
	                  "imdbLink", 
	                  "imdbScore", 
	                  "genres", 
	                  "poster", 
	                  "title", 
	                  "year"]
	movies.year.replace(r"\D", "", regex=True, inplace=True,)
	movies.to_sql("movie", 
		          con=engine, 
		          if_exists="append", 
		          index=True, 
		          index_label="movieId")
	users = pd.read_csv("users.csv", encoding="latin-1")
	users.to_sql("user", 
		         con=engine, 
		         if_exists="append", 
		         index=False)

if __name__ == "__main__":
	main()