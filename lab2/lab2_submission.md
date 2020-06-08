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

# Description of Dataset

We used the SMS Spam Collection Dataset obtained from Kaggle (https://www.kaggle.com/dejavu23/sms-spam-or-ham-beginner/notebook). It contains data for 5,000 legitimate and spam SMS messages classified as SPAM or HAM accordingly.

