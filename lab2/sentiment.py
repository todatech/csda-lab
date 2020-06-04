import logging
import pickle

import string

import pandas as pd
import numpy as np 
import re
import os.path
from collections import Counter
import itertools
import time


# Scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# from sklearn.svm import LinearSVC

# Keras
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, Embedding, Flatten, Conv1D, MaxPooling1D, LSTM
from keras import utils
from keras.callbacks import ReduceLROnPlateau, EarlyStopping


# nltk
import nltk
from nltk.corpus import stopwords
from  nltk.stem import SnowballStemmer

# Word2vec
import gensim
from gensim.models import Word2Vec


# logger for displaying object builiding status on server
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -------- static variables -------------------------
# DATASET
TRAIN_SIZE = 0.8

# WORD2VEC 
W2V_SIZE = 300
W2V_WINDOW = 7
W2V_EPOCH = 32
W2V_MIN_COUNT = 10

# KERAS
SEQUENCE_LENGTH = 300
EPOCHS = 8
BATCH_SIZE = 1024

# SENTIMENT
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"
SENTIMENT_THRESHOLDS = (0.4, 0.7)

# FILE PATH
FPATH = "../data/"

# EXPORT
KERAS_MODEL = FPATH + "model.h5"
WORD2VEC_MODEL = FPATH + "model.w2v"
TOKENIZER_MODEL = FPATH + "tokenizer.pkl"
ENCODER_MODEL = FPATH + "encoder.pkl"
TWEET_DATA = FPATH + "clean_tweet_small.csv"

# Helper Functions
# decode_map = {0: "NEGATIVE", 2: "NEUTRAL", 4: "POSITIVE"}
# def decode_sentiment(label):
#     return decode_map[int(label)]

def decode_sentiment(score, include_neutral=True):
    if include_neutral:        
        label = NEUTRAL
        if score <= SENTIMENT_THRESHOLDS[0]:
            label = NEGATIVE
        elif score >= SENTIMENT_THRESHOLDS[1]:
            label = POSITIVE

        return label
    else:
        return NEGATIVE if score < 0.5 else POSITIVE

def get_file_path(path):
    this_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(this_path, path)

# SentimentInferencing Class
class SentimentInferencing:
    '''SentinmentInferencing Class
    By extracting users' sentiment data on a set of tweeter messages, this python class can infer sentiment 
    when a text message is given. This engine is based upon the keras RNN/LSTM model.
    TODO: we can tweak the deep learning model with different parameters, more EPOCH run, and larger dataset.
    However, for code demonstration and applied case for DASH app, this python class and model do give a reasonable
    prediction for its purpose.
    '''

    def __init__(self):
        self.df = None
        self.model = None
        self.w2v_model = None
        self.tokenizer = None
        self.encoder = None
        self.start_sentiment_engine()
    
    def save_ml_objects(self):
        logger.info('saving ml objects...')

        logger.info('saving keras model...')
        path = get_file_path(KERAS_MODEL)
        self.model.save(path)

        logger.info('saving word2vec model...')
        path = get_file_path(WORD2VEC_MODEL)
        self.w2v_model.save(path)
        
        logger.info('saving tokenizer...')
        path = get_file_path(TOKENIZER_MODEL)
        pickle.dump(self.tokenizer, open(path, "wb"), protocol=0)
        
        logger.info('saving encoder...')
        path = get_file_path(ENCODER_MODEL)
        pickle.dump(self.encoder, open(path, "wb"), protocol=0)
        logger.info('done!')
        
    def load_ml_objects(self):
        logger.info('loading ml objects...')

        path = get_file_path(KERAS_MODEL)
        if os.path.exists(path):
            logger.info('loading keras model...')        
            self.model = keras.models.load_model(path)

        path = get_file_path(WORD2VEC_MODEL)
        if os.path.exists(path):
            logger.info('loading word2vec model...')        
            self.w2v_model = Word2Vec.load(path)

        path = get_file_path(TOKENIZER_MODEL)
        if os.path.exists(path):
            logger.info('loading tokenizer...')        
            self.tokenizer = pickle.load(open(path, "rb"))

        path = get_file_path(ENCODER_MODEL)
        if os.path.exists(path):
            logger.info('loading encoder...')        
            self.encoder = pickle.load(open(path, "rb"))

        logger.info('done!')


    def start_sentiment_engine(self):
        logger.info('starting sentiment engine...')
        
        self.load_sentiment_data()

        path = get_file_path(KERAS_MODEL)
        if os.path.exists(path):
            self.load_ml_objects()
        else:
            self.build_model()
            self.save_ml_objects()

        logger.info('complete loading sentiment engine...')

    def get_sample_text(self, sentiment='POSITIVE', n=5):
        return self.df[self.df['target'] == sentiment][['text']].sample(n)

    def load_sentiment_data(self):
        path = get_file_path(TWEET_DATA)
        self.df = pd.read_csv(path, encoding='latin-1')

    def build_model(self):
        logger.info('building word2vec model...')
        df_train, df_test = train_test_split(self.df, test_size=1-TRAIN_SIZE, random_state=42)
        documents = [_text.split() for _text in df_train.text]
        self.w2v_model = gensim.models.word2vec.Word2Vec(size=W2V_SIZE, 
                                            window=W2V_WINDOW, 
                                            min_count=W2V_MIN_COUNT, 
                                            workers=8)
        self.w2v_model.build_vocab(documents)
        self.w2v_model.train(documents, total_examples=len(documents), epochs=W2V_EPOCH)
        
        logger.info('building keras tokenizer...')
        self.tokenizer = Tokenizer()
        self.tokenizer.fit_on_texts(df_train.text)
        vocab_size = len(self.tokenizer.word_index) + 1
        x_train = pad_sequences(self.tokenizer.texts_to_sequences(df_train.text), maxlen=SEQUENCE_LENGTH)
        x_test = pad_sequences(self.tokenizer.texts_to_sequences(df_test.text), maxlen=SEQUENCE_LENGTH)

        logger.info('building label encoder...')
        self.encoder = LabelEncoder()
        self.encoder.fit(df_train.target.tolist())
        y_train = self.encoder.transform(df_train.target.tolist())
        y_test = self.encoder.transform(df_test.target.tolist())
        y_train = y_train.reshape(-1,1)
        y_test = y_test.reshape(-1,1)

        embedding_matrix = np.zeros((vocab_size, W2V_SIZE))
        for word, i in self.tokenizer.word_index.items():
            if word in self.w2v_model.wv:
                embedding_matrix[i] = self.w2v_model.wv[word]

        embedding_layer = Embedding(vocab_size, W2V_SIZE, weights=[embedding_matrix], input_length=SEQUENCE_LENGTH, trainable=False)

        logger.info('configuring LSTM model...')
        self.model = Sequential()
        self.model.add(embedding_layer)
        self.model.add(Dropout(0.5))
        self.model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
        self.model.add(Dense(1, activation='sigmoid'))

        self.model.compile(loss='binary_crossentropy',
            optimizer="adam",
            metrics=['accuracy'])

        callbacks = [ ReduceLROnPlateau(monitor='val_loss', patience=5, cooldown=0),
              EarlyStopping(monitor='val_acc', min_delta=1e-4, patience=5)]

        EPOCHS = 2
        logger.info('fitting LSTM model...')
        history = self.model.fit(x_train, y_train,
                    batch_size=BATCH_SIZE,
                    epochs=EPOCHS,
                    validation_split=0.1,
                    verbose=1,
                    callbacks=callbacks)
        
        score = self.model.evaluate(x_test, y_test, batch_size=BATCH_SIZE)
        print()
        print("ACCURACY:",score[1])
        print("LOSS:",score[0])

    def test_w2v(self):
        print(self.w2v_model.most_similar("love"))

    def predict(self, text, include_neutral=True):
        start_at = time.time()
        # Tokenize text
        x_test = pad_sequences(self.tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
        # Predict
        score = self.model.predict([x_test])[0]
        # Decode sentiment
        label = decode_sentiment(score, include_neutral=include_neutral)

        return {"label": label, "score": float(score),
        "elapsed_time": time.time()-start_at} 
