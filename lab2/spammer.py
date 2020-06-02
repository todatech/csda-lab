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
        self.Xctr_tf_fitted = None
        self.start_spam_id_engine()

    def save_ml_objects(self):
        mypath = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(mypath, '../data/ml_spam_obj.pkl')

        logger.info('Saving ML/spam objects to data/ml_spam_obj.pkl')
        
        my_list = [
            self.Xctr_tf_fitted,
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
            self.Xctr_tf_fitted, self.algo = my_test
            logger.info('finish loading ml_objects.pkl.')
        else:
            logger.info('cannot data/ml_spam_obj.pkl, starts engine to populate objects...')
            self.start_spam_id_engine()
            self.save_ml_objects()

    def start_spam_id_engine(self):
        logger.info('starting spam id engine...')
        self.load_spam_data()
        self.build_model()
        logger.info('completing spam id engine...')
    
    def get_sample_ham(self):
        return self.spam_data[self.spam_data['label'] == 'ham'].sample(5)

    def get_sample_spam(self):
        return self.spam_data[self.spam_data['label'] == 'spam'].sample(5)
    
    def load_spam_data(self):
        mypath = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(mypath, '../data/spam_cleaned.csv')
        self.spam_data = pd.read_csv(path, encoding='latin-1')

    def build_model(self):
        logger.info('Building Train/Test split from spam data...')
        corpus = self.spam_data.filtered_text.values.astype('U')
        y = self.spam_data.spam.values
        Xc_train, Xc_test, y_train, y_test = train_test_split(corpus, y, test_size=0.25)

        logger.info('Vectorizing Training Set...')
        tf = TfidfVectorizer(use_idf=True)
        self.Xctr_tf_fitted = tf.fit(Xc_train)
        # should save Xct_tf_fitted in pickle to freeze the vocab list
        Xctr_tf_fitted_txform = self.Xctr_tf_fitted.transform(Xc_train)

        logger.info('Vectorizing Test Set...')
        tf_test = TfidfVectorizer(use_idf=True, vocabulary=self.Xctr_tf_fitted.vocabulary_)
        Xcte_tf_fitted_txform = tf_test.fit_transform(Xc_test)

        logger.info('Fitting Linear SVC Model...')
        self.algo = LinearSVC()
        self.algo.fit(Xctr_tf_fitted_txform, y_train)
        y_pred_LSVC = self.algo.predict(Xcte_tf_fitted_txform)
        LSVC_acc = accuracy_score(y_test, y_pred_LSVC)
        msg = 'Finalizing Vectorizer, Linear SVC Accuracy: ' + str(LSVC_acc)
        logger.info(msg)

    def identify_message(self, message):
        # if not self.tvec:
        #    self.start_spam_id_engine()
        
        filtered_msg = remove_punctuation_and_stopwords(message)
        filtered_msg = ' '.join(filtered_msg)
        tf1 = TfidfVectorizer(use_idf=True, vocabulary=self.Xctr_tf_fitted.vocabulary_)
        sample_fitted_txform = tf1.fit_transform([filtered_msg])
        answer = self.algo.predict(sample_fitted_txform)
        
        return answer