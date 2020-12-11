import numpy as np 
import pandas as pd 
pd.options.display.max_columns = None 
df = pd.read_csv('/home/allen/Galva/caseStudy/Team_Cave_Goblins/data/ml-latest-small/ratings.csv')


if __name__=='__main__':
    print(df.head())