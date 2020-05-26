# Summary of Work for Lab1 Exercise

## GIT

- We share work on github.com. Link is [here](https://github.com/todatech/csda-lab.git)

<br />

## Juypter Notebook

---

### Lab 1 - Data Analysis and Data Exploration for Movies Recommender

We have finished data analysis on the TMDB movies dataset, which contains about 45k rows of movies metadata. In addition, it also contains ratings for various movies titles from individual users. The movies dataset can be found on [kaggle.com](https://www.kaggle.com/rounakbanik/the-movies-dataset)

[Lab 1 Data Analysis](lab1/movies_data_explore.ipynb)

### Lab 1 - Performance, Analysis and Machine Learning Models of Movies Recommender Systems

Once we've scrubbed and cleaned the movies dataset, we saved it as a separate csv file and ready to load onto the server. We also carried out modeling for our movies recommender systems on Jupyter Notebook. We've built four different movies recommender systems in this notebook to illustrate the  workings of the engine. The following summary gives a brief description of how each recommender works.

1. Simple Recommender

    For Simple Recommender, we recommend movies that are "highly acclaimed". This means that for those movies that have both high number of vote counts and averages(ie. vote_count > threadhold number), we will use this to present to our end user. We also filter our result based on various genres of user's choice.

2. Content Based Recommender

    For Content Based Recommender, we used text mining techinques to mine keywords for individual movie title. From within the overview and the tagline of the movie, we are able to dig out keywords that are "unique" to each title. Next, we built a cosine similarity matrix to find corelation amoung 45k different movie titles. When end user of the system provides a movie title of his/her choice, the recommender system would recommend a list of movies that are highly related to this choice based on keywords freqencies we found in the description for these movies.  

3. Collaborative Filtering Recommender

    In the dataset, "rating.csv" contained a series of movie rating records (rating from 1-5) by individual users. By leveraging a python package called ["scikit-surprise"](http://surpriselib.com/), we are able to build a collaborative filtering recommender system with ease. In a simplier term, we used SVD algorithm to train a model with sets of rating records, that consisted of userid, movieid, and rating information.  We further used this model to predict what the end user will rate for a given movie id.  We validated our prediction in our analysis and it gives roughly  ~0.9 RSME accuracy for 5-fold cross-validations.

4. Hybrid Recommender

    For Hybrid Recommender, we combine the best of CB Recommender and CF Recommender to give better recommendation. First, we obtain a list of highly-related movies based on end user's input, and then we evaluate each of the title to see which has higher predicted rating. Then, we present this list to our end user in a descending order list.

[Lab 1 Movie Recommender System Performance and Analysis](lab1/movies_recommender.ipynb)

<br />

## Python Module

---

### Lab 1 - Movies Recommender Library and Recommender Class

This module contains Recommender Class design specifically for our separate Dash App. This is an extraction from preivous Juypter Notebook for modeling analysis. There is another Jupyter Notebook that demonstrates how each methods in the Recommender class works.

[Lab 1 Movies Recommender Class](lab1/movies.py)

[Lab 1 Movies Recommender Class test](lab/movies_class_test.ipynb)

<br />

## Dash App

---

Dash App has been divided into separate modules for easy management. Each module carried out its own functions.

1. Server Level (gunicorn.py)
2. App Level (app.py, index.py)
3. Page Level (homepage.py, lab1app.py, lab2app.py, lab3app.py, testapp.py)
4. Function Level (callbacks.py, layouts.py)

<br />

## Docker

---

This app is "docker-enable", which mean it can be built into containerized app.

    ```bash
    $ docker-compose up --build
    ```

<br />

## Deployment

---

### a. Local Test Server

This app can be run locally on your machine. Refer to README.md to setup your enviorment, load the python packages from requirements.txt and you are ready to deploy. Running the following command will launch a test server locally.

    ```bash
    $ python index.py
    ```

### b. Remote Production Server

This app has also been deployed to Google Cloud Platform served by production level WSGI webserver using gunicorn/nginx. Vist http://dash.todatech.ca:8050 for a demo.
