#!/usr/bin/env python3

from sqlalchemy import create_engine
import pandas as pd
from numpy.random import choice

def recommender_system(prefs):

	del prefs["recommend"]
	oldest = int(prefs["oldest"][0])
	del prefs["oldest"]
	newest = int(prefs["newest"][0])
	del prefs["newest"]
	engine = create_engine("sqlite:///movies.db")
	data = pd.read_sql("movie", con=engine, index_col="movieId")
	data.year = pd.to_numeric(data.year)
	data["interest"] = 0
	timely_movies = data[(data.year >= oldest) & (data.year <= newest)]
	interested_movies = [list(timely_movies[timely_movies[pref] == 1].index) 
	                     for pref in prefs.keys()]
	interested_movies = data.loc[[movie for movie_list in interested_movies 
	                                    for movie in movie_list]]
	interested_movies.imdbScore = interested_movies.imdbScore / interested_movies.imdbScore.sum()
	return choice(interested_movies.title, p=interested_movies.imdbScore)

def main():

	prefs = {'recommend': ['Recommend Film'], 
	         'oldest': ['2010'], 
	         'musical': ['on'], 
	         'newest': ['2016'], 
	         'western': ['on']}
	recommender_system(prefs)

if __name__ == "__main__":
	main()