**CSDA1040: Advanced Methods of Data Analysis**

**Lab 2 - Text Mining and Sentiment Analysis**

**SMS Spam Identifyer and Twitter Sentiment detection**

**Submitted By Group 8**

Michaela Hrabetova (ID: 217590209)

Lu Han (ID: 217618638)

Tony Chan (ID: 217635038)

Cristina Endara (ID: 217625567)

Sangeeta Khanna (ID: 217638719)

**Date of Submission:** June 8, 2020


# GIT

- We share work on github.com. Link is [here](https://github.com/todatech/csda-lab.git)


# SMS SPAM IDENTIFYER

# Introduction

Over the past two decades SMS spam has grown significantly. Canada's Reporting Centre receives approximately 5,000 spam complaints per week. Some are connected to legitimate commercial messages from various companies and others are related to scams, fraud and privacy threats, hence the increasing importance of mechanisms to identify such type of messages.

The first part of this project includes a Spam Identifyer Engine from an SMS dataset. We relied on text mining techiques to clean up and vectorize the text messages in the dataset. We used a typical scikit-learn preprocessing package to vectorize the text messages into TF-IDF matrix. We evaluated various classification algorithms and determined that linearSVC was more suitable for this particular dataset in terms of performance and accuracy.

# Description of Dataset and Data Exploration

We used the SMS Spam Collection Dataset obtained from Kaggle (https://www.kaggle.com/dejavu23/sms-spam-or-ham-beginner/notebook). It contains data for 5,000 legitimate and spam SMS messages classified as SPAM or HAM accordingly. 

Since ~75% of the messages are HAM (legimate), the model might skew more towards the legimate side. Also, most of the SPAM messages tend to have a higher number of words (towards the 160 maximum words in SMS) versus the HAM messages where the majority have less than 100 words.

# Text Mining

We applied Python's Natural Language Toolkit NLTK to remove punctuation and stopwords. Both are common tokens in the language and by removing them we expect to increase the classification models accuracy.

| Label | Text | Spam | length	| filtered_text
| --- | --- | --- | --- | --- |
| ham | Go until jurong point, crazy.. Available only ... | 0 | 111	| [go, jurong, point, crazy, available, bugis, n...
| ham |	Ok lar... Joking wif u oni...	| 0 |	29 |	[ok, lar, joking, wif, u, oni]
| spam	| Free entry in 2 a wkly comp to win FA Cup fina...	| 1	| 155	| [free, entry, 2, wkly, comp, win, fa, cup, fin...
| ham	| U dun say so early hor... U c already then say...	| 0	| 49	| [u, dun, say, early, hor, u, c, already, say]
| ham | Nah I don't think he goes to usf, he lives aro...	| 0	| 61	| [nah, dont, think, goes, usf, lives, around, t...

A typical wordcloud show us that many SPAM messages include words related to prizes, free goods/services and requiring the receiver to take an action (i.e. call or do something urgent). Here are some main characteristics of the two types of massages where some of the most frequent words are:

    SPAM: free, text, tone, now, call, won, to claim your mobile.

    HAM: I'm, how, will, no, now, ok, now
 
 # Feature extraction