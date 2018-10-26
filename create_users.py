#!/usr/bin/env python3

# Creates csv file consisting of fabricated users with IDs matching 
# those found in 'imported_datasets/ratings.csv'. Each of these users 
# has a fabricated name, gender, and age associated with their ID.

import pandas as pd
import names
import random
import numpy as np
from numpy.random import randint

random.seed(0)
np.random.seed(0)

def main():
    
    user_ids = pd.read_csv("imported_datasets/ratings.csv").userId.unique()
    user_names = [(names.get_first_name(gender="female"), "female") 
                  for i in range(len(user_ids)//2)]
    user_names.extend([(names.get_first_name(gender="male"), "male") 
                       for i in range(len(user_ids)//2)])
    users = pd.DataFrame(user_names, 
                         columns=["name", "gender"], 
                         index=user_ids)
    users["age"] = randint(18, 39, len(users))
    users = users.sample(frac=1)
    users.to_csv("users.csv", index_label="userId")

if __name__ == "__main__":
    main()