import pandas as pd
import numpy as np

def convert_to_list(x):
  return [y.strip("\'") for y in x.strip("[]").split(', ')]

def load_df():
    md = pd.read_csv('../input/movies_cleaned.csv')
    return md

def get_genres(md):
    # s = md.apply(lambda x: pd.Series(x['genres']),axis=1).stack().reset_index(level=1, drop=True)
    s = md.apply(lambda x: pd.Series(convert_to_list(x['genres'])),axis=1).stack().reset_index(level=1, drop=True)
    s.name = 'genre'
    s = s.to_frame()
    s.columns = ['genre']
    genre_list = s['genre'].unique()
    #s['genre'].value_counts()

    #remove empty strings
    result = []
    for x in genre_list:
        if (x != ''):
            result.append(x)

    return result

def test():
    my_df = load_df()
    lst = get_genres(my_df)
    print(lst)


if __name__ == "__main__":
    test()