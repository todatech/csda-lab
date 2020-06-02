import logging
import pickle

import string

import pandas as pd 
import numpy as np 
import re
import os.path

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from sklearn.svm import LinearSVC

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import nltk
from nltk.corpus import stopwords


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Helper Functions
def remove_punctuation_and_stopwords(msg):
    
    sms_no_punctuation = [ch for ch in msg if ch not in string.punctuation]
    sms_no_punctuation = "".join(sms_no_punctuation).split()
    
    sms_no_punctuation_no_stopwords = \
        [word.lower() for word in sms_no_punctuation if word.lower() not in stopwords.words("english")]
        
    return sms_no_punctuation_no_stopwords


# SpamIdentifier Class
class SpamIdentifier:
    '''
    A spam message identifier using a set of labelled data whether it is spam/ham (bad/good) msg
    '''
    def __init__(self):
        self.spam_data = None
        self.algo = None
        self.tvec = None
        self.start_spam_id_engine()

    def save_ml_objects(self):
        mypath = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(mypath, '../data/ml_spam_obj.pkl')

        logger.info('Saving ML/spam objects to data/ml_spam_obj.pkl')
        
        my_list = [
            self.tvec,
            self.algo,
        ]
        with open(path, 'wb') as output:
            pickle.dump(my_list, output, pickle.HIGHEST_PROTOCOL)
        logger.info('Finish saving ml_objects.pkl.')
    
    def load_ml_objects(self):
        mypath = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(mypath, '../data/ml_spam_obj.pkl')

        if os.path.exists(path):
            logger.info('found data/ml_spam_obj.pkl, loading from file...')
            with open(path, 'rb') as input:
                my_test = pickle.load(input)
            
            # self.genres, 
            self.tvec, self.algo = my_test
            logger.info('finish loading ml_objects.pkl.')
        else:
            logger.info('cannot data/ml_spam_obj.pkl, starts engine to populate objects...')
            self.start_spam_id_engine()
            self.save_ml_objects()

    def start_spam_id_engine(self):
        logger.info('starting spam id engine...')
        self.load_spam_data()
        self.start_vectorizer()
        logger.info('completing spam id engine...')
    
    def get_sample_ham(self):
        return self.spam_data[self.spam_data['label'] == 'ham'].sample(5)

    def get_sample_spam(self):
        return self.spam_data[self.spam_data['label'] == 'spam'].sample(5)
    
    def load_spam_data(self):
        mypath = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(mypath, '../data/spam_cleaned.csv')
        self.spam_data = pd.read_csv(path, encoding='latin-1')

    def start_vectorizer(self):
        logger.info('Loading TF-IDF Vectorizer...')
        self.tvec = TfidfVectorizer()
        corpus = self.spam_data['filtered_text'].values.astype('U')
        X_fitted = self.tvec.fit(corpus)
        X_transformed = self.tvec.transform(cor)
        X_word_features = self.tvec.fit_transform()
        X_word_features_matrix = X_word_features.A
        y = self.spam_data.spam.values
        logger.info('Preparing Train/Test Set...')
        Xt_train, Xt_test, yt_train, yt_test = train_test_split(X_word_features_matrix, y, test_size=0.25)

        logger.info('Fitting Linear SVC Model...')
        self.algo = LinearSVC()
        self.algo.fit(Xt_train, yt_train)

        yt_pred_LSVC = self.algo.predict(Xt_test)
        LSVC_acc = accuracy_score(yt_test, yt_pred_LSVC)
        msg = 'Finalizing Vectorizer, Linear SVC Accuracy: ' + str(LSVC_acc)
        logger.info(msg)

    def identify_message(self, message):
        # if not self.tvec:
        #    self.start_spam_id_engine()
        
        filtered_msg = remove_punctuation_and_stopwords(message)
        filtered_msg = ' '.join(filtered_msg)


        return filtered_msg