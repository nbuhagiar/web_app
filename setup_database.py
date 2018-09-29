#!/usr/bin/env python3

# Create SQLite database consisting of all datasets

from sqlalchemy import create_engine
import pandas as pd

def main():

	engine = create_engine("sqlite:///movies.db")
	links = pd.read_csv("imported_datasets/links.csv")
	links.to_sql("links", con=engine)
	movies = pd.read_csv("imported_datasets/movies.csv")
	movies.to_sql("movies", con=engine)
	ratings = pd.read_csv("imported_datasets/ratings.csv")
	ratings.to_sql("ratings", con=engine)
	tags = pd.read_csv("imported_datasets/tags.csv")
	tags.to_sql("tags", con=engine)
	users = pd.read_csv("users.csv")
	users.to_sql("users", con=engine)

if __name__ == "__main__":
	main()