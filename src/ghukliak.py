import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import surprise
import inspect
from surprise import AlgoBase, Dataset
from surprise import SVD, Dataset, accuracy 
from surprise.model_selection import train_test_split
from surprise.model_selection.search import RandomizedSearchCV
from surprise.model_selection.validation import cross_validate

# df = pd.read_csv('../data/ml-latest-small/ratings.csv')
# print(df.head())

if __name__ == "__main__":
    # df = pd.read_csv('../data/ml-latest-small/ratings.csv')

    # ratings = Dataset.load_builtin('ml-100k')
    # trainset, testset = train_test_split(ratings, test_size=.25)
    # algo = SVD()

    # # Train the algorithm on the trainset, and predict ratings for the testset
    # algo.fit(trainset)
    # predictions = algo.test(testset)

    # # Then compute RMSE
    # accuracy.rmse(predictions)

    # predictions = algo.fit(trainset).test(testset)
    # print(rs.best_score)
    # print(rs.best_params)
    print(inspect.getsource(surprise.SVD()))

