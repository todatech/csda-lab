# Summary of Work for Lab 2 - Text Mining and Deep Learning Exercise

## Summary

We implemented a spam idenifying engine and sentimenet detection engine in Lab 2. In spam identifying engine, we used text mining techiques to clean up and vectorize text found in SMS message dataset. We used a typical scikit-learn preprocessing package to vectorize text into TF-IDF matrix. Next, we evaluated various classification algorithms and determined that linearSVC was more suitable for this particular dataset, in terms of both the performance and accuracy.

For sentiment analysis system, we picked 200k records from the set of 1.6M twitter messages in which have been labelled with sentiment response. Then, we use gensim preprocessing package to extract topics from a large volume of text, as known as topic modeling. Finally, we fed that data and trained a model to perform sentiment perdiction using Keras/LSTM neural network.

<br />

## Juypter Notebook

---

### Lab 2a - Data Preprecessing and Modeling for SMS Spam Collection Dataset

We have selected [this](https://www.kaggle.com/uciml/notebook) dataset for text mining demonstration. It contains ~5k records that identified a string of text as valid legitimate message or spam.

We completed some data preprocessing tasks and performed simple data explorations using this dataset, which can be found [here](lab2/spam_identifier.ipynb).

Then, we used the clean data to perform feature extraction on the string of text we found in the message body. In order to tokenize and vectorize the string of text, we  used preprocessing package from within scikit-learn, called TfidfVectorizer(), to generate a vectorized matrix model.

Following this process, we started to build machine-learning model around this dataset/matrix. We ran a few ML models as suggested by [scikit-learn cheat sheet](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html). The rationale behind selecting one algorithm over the other can be found in the lab2a notebook.

Finally, we selected linearSVC estimator for our spam engine because it gave better accuracy of 0.985 and only takes few milliseconds to compute, while some of the model take up as much as a minute to compute.

[Lab 2a: Text Mining - SMS Spam Collection](lab2/spam_identifier.ipynb)

[SMS Spam Collection Dataset](https://www.kaggle.com/uciml/notebook)

### Lab 2b - Data Preprecessing and Modeling for Sentiment Analysis System

For deep learning part of the exercise, we selected the twitter sentiment dataset for this demonstration. This dataset can be found [here](http://help.sentiment140.com/for-students/).

We went through the same process as lab2a. We carried out data preprocessing, feature extraction, and modeling for this second part of the lab. Instead of using the "traditional" scikit-learn library, we followed the example from [Paolo Ripamonti](https://www.kaggle.com/paoloripamonti) and built a sentiment engine using Gensim/Keras.

Gensim is a Topic Modeling Engine for processing text and for word vector generation. Keras, on the other hand, is a wrapper for the underlying tensorflow neural network engine. In Paolo's example, he used LSTM as the underlying neural networking model for sentiment detection. We borrowed his example and implemented a python engine for our dash app. However, for our application, we tuned down the model by tweaking down some of the paramters, as well as downsizing the dataset in order to minimize the model generation time from 8+ hours down to 10 mins. Nonetheless, this model still give a respectable 0.78 accuracy even though we slashed the model heavily.

We also modified some functions for our Dash app. Our data exploration work can be found [here](lab2/twitter_sentiment_data_explore.ipynb). And, our LSTM modeling work can be found [here](lab2/twitter_sentiment_lstm.ipynb).

[Lab 2b: Deep Learning Model (Part 1): Twitter Sentiment Analysis - Data cleaning and Data exploration](lab2/twitter_sentiment_data_explore.ipynb)

[Lab 2b: Deep Learning Model (Part 2): Twitter Sentiment Analysis - Neural Network Modeling LSTM | Keras](lab2/twitter_sentiment_lstm.ipynb)

[Sentiment140](http://help.sentiment140.com/home)

[Twitter Sentiment Analysis by Paolo Ripamonti](https://www.kaggle.com/paoloripamonti/twitter-sentiment-analysis)

[Gensim - topic modelling for humans](https://radimrehurek.com/gensim/)

[Keras - Deep Learning API](https://keras.io/)

<br />

## Python Module

---

### Lab 2a - Spam Identifier

This module contains library of Spam Identifier Class. After the spam identifying engine is up and running, it is able to predict whether a string of text is a spam or not.

[Lab 2a Spam Identifier Engine Class](lab2/spammer.py)

[Lab 2a Spam Identifier Engine Class Test Notebook](lab2/spammer_class_test.ipynb)

### Lab 2b - Sentiment Analyzer

This module contains library of Sentiment Analyzing Class. When the engine is up and running, it is able to detect sentiment within a text string, whether it is a POSITIVE mesage, NEGATIVE, or NEUTRAL.

[Lab 2b Sentiment Analyzing Engine Class](lab2/sentiment.py)

[Lab 2b Sentiment Analyzing Engine Class Test Notebook](lab2/sentiment_class_test.ipynb)

<br />

## Dash App / Docker / Deployment

---

Demonstration of both engines can be found in the dash app lab 2 section. For docker and deployment, please refer to lab1 summary of work, under the same section.

[Lab1 Summary of work](lab1/summary_of_work_lab1.md)