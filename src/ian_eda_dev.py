import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
from surprise import SVD, Dataset, NMF
from surprise.model_selection import train_test_split
from surprise.model_selection.search import GridSearchCV
from surprise.model_selection.validation import cross_validate

def custom_rmse_cv():
    pass

if __name__ == '__main__':
    # df = pd.read_csv('data/ml-latest-small/ratings.csv')
    # # ratings = df.pivot_table(values=df['rating'], index=df['userId'], columns=df['movieId'])
    # ratings = Dataset.load_builtin('ml-100k')
    # train, test = train_test_split(ratings)

    algo = SVD(n_factors=50)
    # SVD.fit(train)

    data = Dataset.load_builtin('ml-100k')

    param_grid = {'n_epochs': [10, 15, 20, 25, 30], 'lr_all': [0.004, 0.005, .007, .01, .15],
                'reg_all': [.01, .02, .05, .1, .2, .4]}
    gs = GridSearchCV(SVD, param_grid, measures=['rmse'], cv=3)

    gs.fit(data)

    print(gs.best_params)
    # results = cross_validate(algo, ratings, measures=['RMSE'])
    # print(np.mean(results['test_rmse']))