# Summary of Work for Lab 3 - Time Series Analysis on Google Search Keyword

(old contents from below)

## Summary

In this lab, we wish to learn more about the time characteristics of a search term of interest. When you enter a search term on Google, servers will record the time you have tried to search on their website. Over the years, they have collected enormous amount of search data. Through the use of Google's own utility called [Google Trends](https://trends.google.com/trends/?geo=US), users are able to view the interest over time for any search term of your choosing. In addition to time, Google Trend is able to provide geographical locations about where these searches are originated worldwide.

By leveraging this data, we wish to learn about the time characteristics of any given serach term. We will break it down into different time components and further predict the search frequency over the next year or so. We will be using technique called SARIMA.

Applying regession on the time-series dataset for any given keyword is fairly easy -- it only involves applying SARIMA algorithm in a few lines of code. However, choosing the right P, d, Q parameters in SARIMA/ARIMA(P, d, Q) requires tweaking and human trial and error. Since every keywords has very different time characteristics, for example 'diet' and 'covid' exhibits totally different time-varying behavior. We need a more robust way to tweak those number. But, this is out of the scope of this exercise.

<br />

## Juypter Notebook

---

### Lab 3 - Data Preprecessing for Google Trends Keyword Search

Data has been obtained through the use of pytrends package, which connects to Google Trends API web services. Pytrends allows different ways to pull data off from the web services. For our purpose, we just limited ourselves to the "default settings" -- we will let the API to provide us with default region and time frame, which is in the North America region and we will be looking at the 5 most recent years of data. 

Data is determined to be in a very clean state. The only work required was to properly realigning the data and dropping some columns that are not needed. The API provide us weekly data points and we think that this is a good compromise between visibility and computation time. 

We further dig into how we should approach dissecting information from the time series. Since most search term has seasonal effects in it, we wish to focus more on both the trends and seasonality behind these. We believe that most terms do not have much noise associated with it. Nonetheless, it is unlike stock market time-series data in which there are a lot of external factors affecting prices on daily basis. We would expect searches do not have this kind of external behaviors that give rise to noise.

When we are modeling p, d , q parameters of both ARIMA and SARIMA, we took those consideration in mind.

Most terms we tried has an trend associated with it. Depending on whether it is a news topic i.e. Covid-19 or dieting or Justin Bieber, we will see very different trending line associated with such topics. Since the data points are on weekly basis, we used rolling window  of 52 weeks -- a time period of a year to see if there is any upward or downward trend.

We also provide a autocorrelation and partial autocorrelation graphs in Juypter Notebook, and most search term exhibit certain repeating pattern in autocorrelation, but not much apparent patterns in partial autocorrelation.

There are much more information in a seasonal_decomposition graph, and we are able to pick up more pattern with any given time-series graph, using Statsmodels package (sm.tsa.seasonal_decompose).

[Lab 3: Juypter Notebook Time-Series Analysis on Google Search Keyword](time_series.ipynb)

### Lab 3 -- Data Modeling using SARIMA

ARIMA basically consists of 3 models combine into one. AR (autoregressive), I (integrate), MA (Moving-Average) and we can selectively use any or all models at once using parameters specified to ARIMA(P, d, Q).

SARIMA has Seasonal part that breaks up ARIMA further into two components (Trends, Seasonal). In our juypter notebook, we have run a few sample keywords with SARIMA and it turn out good result. Furthermore, we feed this to a grid search and try to locate combinations of SARIMA parameters (6 in totals). We settle with one set of parameters for all cases of all keywords. This is also one of the limitation for this app, because we cannot optimize these parameters on the fly for individual keywords. It took about 30 mins to find an optimal parameters in grid search, and thus it is not ideal for web app where users wish to have a quick response.

[Lab 3: Juypter Notebook Time-Series Analysis on Google Search Keyword](time_series.ipynb)

[Kaggle: Everything you can do with a time series by Siddharth Yadav](https://www.kaggle.com/thebrownviking20/everything-you-can-do-with-a-time-series#3.-Time-series-decomposition-and-Random-walks)

[Machine Learning Mastery: How to Create an ARIMA Model for Time Series Forecasting in Python by Jason Brownlee](https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/)

[Machine Learning Plus: Time Series Analysis in Python – A Comprehensive Guide with Examples by Selva Prabhakaran](https://www.machinelearningplus.com/time-series/time-series-analysis-python/)

[Toward Data Science: An End-to-End Project on Time Series Analysis and Forecasting with Python by Susan Li](https://towardsdatascience.com/an-end-to-end-project-on-time-series-analysis-and-forecasting-with-python-4835e6bf050b)

[Data Camp: Time Series Analysis Tutorial with Python by Hugo Bowne-Anderson](https://www.datacamp.com/community/tutorials/time-series-analysis-tutorial)

<br />

## Python Module

---

### Lab 2a - Spam Identifier

This module contains library of KeywordOverTimeTrends Class. Please refere to the usage on the juypter notebook sample

[Lab 3 kottrends.py - KeywordOverTimeTrends Module Class](kottrends.py)

[Lab 3 kottrends_class_test.ipynb - KeywordOverTimeTrends Module Class Test Notebook](kottrends_class_test.ipynb)

<br />

## Dash App / Docker / Deployment

---

Demonstration can be found in the dash app lab 3 section. For docker and deployment, please refer to lab1 summary of work, under the same section. Main part of the lab3 app is located in the root of the project called lab3app.py

[Lab1 Summary of work](../lab1/summary_of_work_lab1.md)

[Lab 3 Dash App](../lab3app.py)

[This File](summary_of_work_lab3.md)