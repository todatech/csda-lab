import logging
import pandas as pd
import numpy as np
import re
import os.path

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

from surprise import Dataset, SVD
from surprise import Reader
from surprise.model_selection import cross_validate

from collections import defaultdict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Helper Functions

def get_name():
    print(__name__)

def convert_to_list(x):
  return [y.strip("\'") for y in x.strip("[]").split(', ')]

def get_top_n(predictions, n=10):
    '''Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


# Recommender Class
class Recommender:
    '''
    A Movie Recommenders with various recommenders methods
    '''
    def __init__(self):
        self.md = None
        self.rd = None
        self.genres = None
        self.cosine_similarity_matrix = None
        self.cf_top_ten_prediction_matrix = None
        self.algo = None
        logger.info('loading data...')
        self.load_movie_data()
        self.load_rating_data()
        #self.start_recommender_engine()
        logger.info('finish initialize recommender object...')

    
    def start_recommender_engine(self):
        logger.info('populating genres list...')
        self.populate_genres_list()
        logger.info('starting cb engine...')
        self.start_content_based_engine()
        logger.info('starting cf engine...')
        self.start_collaborative_filtering_engine()

    
    def load_movie_data(self):
        mypath = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(mypath, '../input/movies_cleaned.csv')
        self.md = pd.read_csv(path)

    def load_rating_data(self):
        mypath = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(mypath, '../input/ratings_small.csv')
        self.rd = pd.read_csv(path)

    def get_sample_df(self):
        return self.get_movie_list_df_by_ids([862, 807, 11, 680, 13])

    def get_sample_df2(self):
        return self.get_movie_list_df_by_ids([414, 268, 364, 14919, 16234])

    def get_sample_df3(self):
        return self.get_movie_list_df_by_ids([1371, 2105, 2193, 2294, 1405])

    def populate_genres_list(self):
        # s = md.apply(lambda x: pd.Series(x['genres']),axis=1).stack().reset_index(level=1, drop=True)
        s = self.md.apply(lambda x: pd.Series(convert_to_list(x['genres'])),axis=1).stack().reset_index(level=1, drop=True)
        s.name = 'genre'
        s = s.to_frame()
        s.columns = ['genre']
        genre_list = s['genre'].unique()

        #remove empty strings
        result = []
        for x in genre_list:
            if (x != ''):
                result.append(x)

        self.genres = result

    def print_movie_list_by_ids(self, ids, n=10):
        # print(self.md[self.md.id.isin(ids)][['id', 'title', 'release_date']].head(n))
        print(self.md[self.md.id.isin(ids)][['id', 'title', 'release_date']])

    def get_movie_list_df_by_ids(self, ids, n=10):
        this_df = self.md[self.md.id.isin(ids)][['id', 'title', 'release_date']] 
        return this_df

    def print_md(self):
        print(self.md)
    
    def print_rd(self):
        print(self.rd)
    
    def print_genres(self):
        print(self.genres)

    # Top Charts
    def get_topchart(self, genre='', quantile=0.995):
        qualified_df = self.md[self.md['vote_count'] > self.md['vote_count'].quantile(quantile)].sort_values('vote_average', ascending=False)
        
        if genre != '':
            genre_filtered_df = qualified_df['genres'].str.contains(genre, flags=re.IGNORECASE, regex=True)
            # return qualified_df[genre_filtered_df]
            return qualified_df[genre_filtered_df].id
        else:
            # return qualified_df
            return qualified_df.id

    def print_topchart(self, genre=''):
        ids = self.get_topchart(genre)
        self.print_movie_list_by_ids(ids)

    # Content-Based Recommender
    def start_content_based_engine(self):
        self.md['tagline'] = self.md['tagline'].fillna('')
        self.md['overview'] = self.md['overview'].fillna('')
        self.md['keywords'] = self.md['tagline'] + ' ' + self.md['overview']

        vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 2),min_df=0, stop_words='english')
        X = vectorizer.fit_transform(self.md['keywords'])
        self.cosine_similarity_matrix = linear_kernel(X,X)

    def cb_recommended_movies_by_title(self, title, n=30):
        #a = md.index[md['Title'] == 'The Godfather']
        a = self.md[self.md['title'] == title]
        if a.empty:
            #print('Is Empty')
            return []
        else:
            # print('Found Title')
            # print(a.index)
            
            b = a.index.astype('int')
            
            # slice the cosine_similiarity matrix for this specific title
            # for cosine_similarity matrix it's "index by index"
            c = self.cosine_similarity_matrix[b]
            d = c.tolist()
            e = list(*d)
            f = list(enumerate(e))
            g = sorted(f, key=lambda x:x[1], reverse=True)
            g = g[1:n+1]
            movies_idx = [x[0] for x in g]
            # print('movies_idx', movies_idx)
            ids = []
            for idx in movies_idx:
                ids.append(self.md[self.md.index == idx]['id'].astype('int'))

            return ids

    def print_cb_recommender_by_title(self, title):
        ids = self.cb_recommended_movies_by_title(title, n=10)
        print('Recommended these movies if you like :', title)
        self.print_movie_list_by_ids(ids)


    # Collaborative Filtering
    def start_collaborative_filtering_engine(self):

        # rating_df = pd.read_csv('../input/ratings_small.csv')
        reader = Reader()
        self.algo = SVD()

        # The columns must correspond to user id, item id and ratings (in that order).
        data = Dataset.load_from_df(self.rd[['userId', 'movieId', 'rating']], reader)

        trainset = data.build_full_trainset()
        self.algo.fit(trainset)

        testset = trainset.build_anti_testset()
        predictions = self.algo.test(testset)

        self.cf_top_ten_prediction_matrix = get_top_n(predictions, n=10)

    def cf_recommended_movies_by_uid(self, uid):
        ids = [x for (x, _) in self.cf_top_ten_prediction_matrix[uid]]
        return ids
    
    def print_cf_recommender_by_uid(self, uid):
        print("For User: ", uid)
        print("Movies that this user rated before:")
        ids = self.rd[self.rd['userId'] == uid][['movieId']]
        self.print_movie_list_by_ids(ids['movieId'])

        print("\nMoives that this user may like:")
        ids = self.cf_recommended_movies_by_uid(uid)
        self.print_movie_list_by_ids(ids)


    # Hybrid Recommender
    def hybrid_recommender(self, uid, title):
        ids = self.cb_recommended_movies_by_title(title)
        rec_df = self.md[self.md.id.isin(ids)][['id', 'title']]
        rec_df['est_rating'] = rec_df['id'].apply(lambda x: self.algo.predict(uid, x).est)
        rec_df = rec_df.sort_values('est_rating', ascending=False)
        # comment to show estimated rating for the df
        # print(rec_df) 
        return rec_df.id

    def print_hybrid_recommender(self, uid, title):
        print('Hi, user#: ', uid)
        print('Based on your ranking history and that you are watching this movie: ')
        print(title)
        print('\nWe think you might like these: ')
        ids = self.hybrid_recommender(uid,title)
        self.print_movie_list_by_ids(ids)


# General Test Code
def test():
    rec = Recommender()
    rec.print_movie_list_by_ids([862])
    print("Code should show Toy Story")


if __name__ == "__main__":
    test()