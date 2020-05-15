![](RackMultipart20200514-4-7k83uf_html_f0f8d480a12c0737.jpg)

**CSDA1010: Basic Methods of Data Analytics**

**Final Project - Clustering**

**Marketing Strategy for Credit Card Customers**

**Submitted By Group 8**

Zeerat Marzana (ID: 215639677)

Michaela Hrabetova (ID: 217590209)

Lu Han (ID: 217618638)

Tony Chan (ID: 217635038)

**Date of Submission:** December 30, 2019

# Abstract

We have used a dataset that summarizes the usage behavior of 8950 active credit card users over a period of six months. The goal of this project is to identify distinguished characteristics of the credit card users -- each of them have their own unique Customer I.D. number. Then, we segment these customers into different groups through clustering techniques based on various attributes of card usage i.e. credit limit, minimum payments, purchase frequency etc. The input variables in the model can be summarized into two broad categories, namely, Personal Finance and Spending Habits. We have used these factors to analyze and group different customers so that the marketing team can further investigate for a proper marketing strategy for similar customers who share the same purchasing behaviors. Thus, increases the chance of success for their campaigns. We have used a few model evaluation techniques, such as the inertial study, the elbow method, and the silhouette score to assess the quality of the clusters. Since this particular dataset did not have any particular &quot;outcome&quot; that are useful for supervised learning models, data analytics was primarily focused on unsupervised learning models, such as clustering.

#


# Introduction

Regression, Principal Component Analysis (PCA) and Clustering are commonly used tools for statistical data analysis and exploratory data mining. Regression estimates the relationship between a dependent variable and a set of explanatory variables; PCA is a technique for feature extraction that emphasizes variation and brings out strong patterns in a dataset; and Clustering groups objects into different clusters where objects within a cluster has similar features. A vital business problem in today&#39;s world of finance is the prediction of credit card usage by cardholders and setting different market strategies for different clusters of clients.

Credit cards are now widely used to pay for purchases of goods and services and accepted by numerous businesses. The _card issuer_ which is usually a bank assigns a particular _credit limit_ to the cardholder from which the user can use any unused portion of the limit for any given transaction. Therefore, _credit limit_ refers to the maximum amount of debt a user can have at any given time. Some cards allow users the flexibility of either paying in full or paying in installments with very low and even zero interests for certain goods and services. A card user can also directly borrow cash termed as _cash advance_ from their assigned credit limit as opposed to using the card to pay a merchant. While the users get a _grace period_ of around 20-25 days to pay back with zero interest for trades with merchants, there is no grace period for _cash advance_. It is up to the users whether they want to pay the full amount within the grace period or accept additional charges and interest on the unpaid amount. However, the user must pay a minimum payment as set by the card issuer within the grace period to continue availing the credit card services.

## Background

The dataset used in this project is obtained from[https://www.kaggle.com/arjunbhasin2013/ccdata/data#](https://www.kaggle.com/arjunbhasin2013/ccdata/data#). The dataset features 18 input variables which are broadly divided into two main groups, namely, Personal Finance attributes (Balance, Credit Limit, Payments etc.), and Purchasing Habits attributes (Purchase, Purchase Frequency, Cash Advance etc.). Based on these customers&#39; behaviours, our group would like to develop a &quot;reusable&quot; process, so that we can group different customers with special traits. Other teams from this company, such as the marketing team or the product development team, can access such grouping arrangements and reach out to these specific group of customers.

The primary focus of this project mainly aimed to segment the customers in defined groups through clustering. Several model evaluation techniques, such as the inertial study, the elbow method, and the silhouette\_score have been used to assess the quality of the clusters. Since this particular dataset did not have any particular _outcome (or output value)_ that are useful for supervised learning models, data analytics was primarily done on unsupervised learning models using k-mean clustering methodology.

## Objective

The primary objective of this project is to segment the customers according to their credit card usage attributes into the numbers of clusters who share similar purchasing patterns, behaviours and traits. Based on the given dataset and a workable size of variables, our objective is to find an optimum number of clusters to describe these customers. The goals are two folds:

1. Associate unique customer id to cluster that exhibit specific trait.
2. Assess and associate new customers based on their new information and group these customers accordingly.

#


# Description of Dataset

This dataset has been obtained from Kaggle, and it is related to credit card usage of about 9000 customers. ([https://www.kaggle.com/arjunbhasin2013/ccdata/data#](https://www.kaggle.com/arjunbhasin2013/ccdata/data#)).

However, there is no further background information given related to this dataset. Therefore, we do not know the geographics location, currency used, bank type (commercial, investment or retail) or information about an individual (sex, age, etc) for the sake of confidentiality. This limitation might be triggered into validity of the final model. But for this given set of data, we believe that we have adequate data with regards to customers&#39; traits and habits associated and meaningful groupings can be formed.

This dataset contains 8950 rows of data and 17 individual data columns. However, this dataset does not contain any useful &quot;output variable&quot; for predictive modeling. Therefore, we will focus primarily on unsupervised model development for the rest of the document.

#


# Data Preparation

The purpose of this dataset is to develop a customer segmentation study in order to define a proper marketing strategy for a credit card company. We wish to determine how customers are divided based on two important matrices 1) Financial Habits 2) Spending Habits for a given set of customers. Our group has done a preliminary study about our customers and determined sets of criteria based on various behaviors. We summarized this in table listed in **Table 10:** Customers&#39; Habits and Classification. To evaluate the effectiveness of this prediction, we used a few model evaluation techniques, such as the inertial study, the elbow method and the silhouette\_score, etc to assess the quality of the clusters. However, this particular dataset did not any particular &quot;outcome&quot; that are useful for supervised learning models. Therefore, the objective will be primarily focused on unsupervised learning models, such as clustering.

Note: for all frequency attributes (1 = frequently updated, 0 = not frequently updated)

### Outcome

**CUST\_ID** : Identification of Credit Card holder (Categorical)

### Financial Habits

**CREDIT\_LIMIT** : Limit of Credit Card for user

**BALANCE** : Balance amount left in their account to make purchases

**BALANCE\_FREQUENCY** : How frequently the Balance is updated, score between 0 and 1

**PAYMENTS** : Amount of Payment done by user

**MINIMUM\_PAYMENTS** : Minimum amount of payments made by user

**PRCFULLPAYMENT** : Percent of full payment paid by user

**TENURE** : Tenure of credit card service for user

###

### Spending Habits

#### _overall purchases (oneoff + installment)_

**PURCHASES** : Amount of purchases made from account

**PURCHASES\_FREQUENCY** : How frequently the Purchases are being made, score between 0 and 1

**PURCHASES\_TRX** : Number of purchase transactions made

#### _oneoff_

**ONEOFF\_PURCHASES** : Maximum purchase amount done in one-go

**ONEOFFPURCHASESFREQUENCY** : How frequently Purchases are happening in one-go, score between 0 and 1

_ **installment** _

**INSTALLMENTS\_PURCHASES** : Amount of purchase done in instalment

**PURCHASESINSTALLMENTSFREQUENCY** : How frequently purchases in instalments are being done, score between 0 and 1

#### _cash advance_[_¶_](http://localhost:8888/notebooks/Google%20Drive%20(tonani%40gmail.com)/CSDA1010%20Project/2_final_project/notebook_1212/CC_Clustering_final_project_group8_tony.ipynb#cash-advance)

**CASH\_ADVANCE** : Cash in advance given by the user

**CASHADVANCEFREQUENCY** : How frequently the cash in advance being paid, score between 0 and 1

**CASHADVANCETRX** : Number of Transactions made with &quot;Cash in Advanced&quot;

###

###

### Data Augmentation

_ **aggregated** _

**Overall Spending [OAS]** = PURCHASES + CASH\_ADVANCE

_ **comparing to CREDIT\_LIMIT** _

**Balance vs Credit Limit [BAL\_VS\_LIMIT]** = BALANCE / CREDIT\_LIMIT

**Payment vs Credit Limit [PMT\_VS\_LIMIT]** = PAYMENTS / CREDIT\_LIMIT

**Minimum Payment vs Credit Limit [MIN\_PMT\_VS\_LIMIT]** = MINIMUM\_PAYMENTS / CREDIT\_LIMIT

**Overall Spending vs Credit Limit [OAS\_VS\_LIMIT]** = OAS / CREDIT\_LIMIT

**Purchase vs Credit Limit [PUR\_VS\_LIMIT]** = PURCHASES / CREDIT\_LIMIT

**One-off Purchase vs Credit Limit [OFP\_VS\_LIMIT]** = ONEOFF\_PURCHASES / CREDIT\_LIMIT

**Installment Purchase vs Credit Limit [INS\_VS\_LIMIT]** = INSTALLMENTS\_PURCHASES / CREDIT\_LIMIT

**Cash Advance vs Credit Limit [CA\_VS\_LIMIT]** = CASH\_ADVANCE / CREDIT\_LIMIT

_ **comparing to Overall Spending** _

**Purchase vs Overall Spending [PUR\_VS\_OAS]** = PURCHASES / OAS

**Oneoff [OFP\_VS\_OAS]** = ONEOFF\_PURCHASES / OAS

**Installment [INS\_VS\_OAS]** = INSTALLMENTS\_PURCHASES / OAS

**Cash Advance vs Overall Spending [CA\_VS\_OAS]** = CASH\_ADVANCE / OAS

**Payment vs Minimum Payment [PMT\_VS\_MIN\_PMT]** = PAYMENTS / MINIMUM\_PAYMENTS

Towards the end of the modeling stage, we reduced the float numbers further into integer ranges for ease of modeling, in order to shorten the computing time. We split the above features into 3 different categories

1. Monetary Features - range from 1 to 6
2. Frequency Features - range from 1 to 10
3. Transactional Features - range from 1 to 8

We used the whole dataset except for 1) TENURE columns, which does not give us useful information for our marketing purposes. 2) Rows contains outliers and missing value, we decided to discard those information because it is only a small fraction to our dataset and it does not worth to spend time fixing them.

## Preview of the Data

The following is a chart of the statistics description of all the attributes in our study.

|
 | **CREDIT\_
 LIMIT **|** BALANCE **|** BALANCE\_
 FREQUENCY **|** PAYMENTS **|** PRC\_FULL\_
 PAYMENT **|** MINIMUM\_
 PAYMENTS **|** TENURE** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **count** | 8636.00 | 8636.00 | 8636.00 | 8636.00 | 8636.00 | 8636.00 | 8636.00 |
| **mean** | 4522.09 | 1601.22 | 0.90 | 1784.48 | 0.16 | 864.30 | 11.53 |
| **std** | 3659.24 | 2095.57 | 0.21 | 2909.81 | 0.30 | 2372.57 | 1.31 |
| **min** | 50.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.02 | 6.00 |
| **25%** | 1600.00 | 148.10 | 0.91 | 418.56 | 0.00 | 169.16 | 12.00 |
| **50%** | 3000.00 | 916.86 | 1.00 | 896.68 | 0.00 | 312.45 | 12.00 |
| **75%** | 6500.00 | 2105.20 | 1.00 | 1951.14 | 0.17 | 825.50 | 12.00 |
| **max** | 30000.00 | 19043.14 | 1.00 | 50721.48 | 1.00 | 76406.21 | 12.00 |
|
 |
 |
 |
 |
 |
 |
 |
 |
|
 | **PURCHASES** | **PURCHASES\_
 FREQUENCY **|** PURCHASES\_TRX **|** ONEOFF\_
 PURCHASES **|** ONEOFF\_
 PURCHASES\_
 FREQUENCY **|** INSTALMENTS\_
 PURCHASES **|** PURCHASES\_
 INSTALLMENTS\_
 FREQUENCY** |
| **count** | 8636.00 | 8636.00 | 8636.00 | 8636.00 | 8636.00 | 8636.00 | 8636.00 |
| **mean** | 1025.43 | 0.50 | 15.03 | 604.90 | 0.21 | 420.84 | 0.37 |
| **std** | 2167.11 | 0.40 | 25.18 | 1684.31 | 0.30 | 917.25 | 0.40 |
| **min** | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| **25%** | 43.37 | 0.08 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| **50%** | 375.41 | 0.50 | 7.00 | 45.00 | 0.08 | 94.79 | 0.17 |
| **75%** | 1145.98 | 0.92 | 18.00 | 599.10 | 0.33 | 484.15 | 0.75 |
| **max** | 49039.57 | 1.00 | 358.00 | 40761.25 | 1.00 | 22500.00 | 1.00 |
|
 |
 |
 |
 |
 |
 |
 |
 |
|
 | **CASH\_
 ADVANCE **|** CASH\_
 ADVANCE\_
 FREQUENCY **|** CASH\_
 ADVANCE\_
 TRX** |
 |
 |
 |
 |
| **count** | 8636.00 | 8636.00 | 8636.00 |
 |
 |
 |
 |
| **mean** | 994.18 | 0.14 | 3.31 |
 |
 |
 |
 |
| **std** | 2121.46 | 0.20 | 6.91 |
 |
 |
 |
 |
| **min** | 0.00 | 0.00 | 0.00 |
 |
 |
 |
 |
| **25%** | 0.00 | 0.00 | 0.00 |
 |
 |
 |
 |
| **50%** | 0.00 | 0.00 | 0.00 |
 |
 |
 |
 |
| **75%** | 1132.39 | 0.25 | 4.00 |
 |
 |
 |
 |
| **max** | 47137.21 | 1.50 | 123.00 |
 |
 |
 |
 |

**Table 1:** Data Description of all variables

## Distribution of values in the dataset

We further examine how these attributes contribute to our problem of understanding the behaviours of our customers. We will look at these attributes individually to see how each of these numbers and range of numbers means, and their underlying meanings behind individual customer.

**Personal Financial Habits**

BALANCE : From the statistics description, we see a lot of customers used up their credit limit, and Balance over credit limit is only the low side.

BALANCE\_FREQUENCY : We have a lot of customers who are actively using our service. We see 0.909 for the low 25% tile users. And the mean is 89%, that indicates their balance is updated fairly frequently.

CREDIT\_LIMIT : There is an interesting mix of credit limit value ranging from $50-$30,0000. Something to note is that, there are customers who are able to spend over their credit limits. i.e. (single purchase of $50,000), we will examine further to see how customers will get approved for over-limit usage.

PAYMENTS : 75 percentile of customers are paying back ~ $2000 every month for credit card bill (while we see only $1100 purchases made and $1100 cash advance made). Therefore, we see a fairly healthy business going on.

MINIMUM\_PAYMENTS : We did further investigation on payment over minimum\_payments in the middle section of the study, we found out that there are as many as 2364 out of 8636 customers who do not meet the minimum payment criteria.

TENURE : Continue further from the above MINIMUM\_PAYMENT study, we found that TENURE score is very similar to a credit score for each individual customer. 12 being good, 6 being bad. 75 percentile of customers have a high credit score of 12. And there are about 1290 out of 8636 customers who do not have a score of 12. This reflects customers behaviour, where customer will accumulate credits owe, but they are willing to make the effort to pay back the bill, and their credit rating are generally good. However, for the purpose of this study we are not focusing on risk factor in order to simplify our model calculations.

PRCFULLPAYMENT : we see an interesting fact that 75 percentile people only pay around 14% of what they owe us. Table XXX in the following section has a good overview of how customers are paying back for their service.

**Purchasing Habits**

PURCHASES : 75 percentile of customers spend \&lt; $1100, but we see there are some big spenders, who is able to afford purchase for slightly less than $50k. (Also looking at oneoff purchase max, we see max amount purchase pay is ~ $40k

PURCHASES\_FREQUENCY : if we look at the purchase frequency chart, we see a pattern that is very symmetrical, meaning we have a good mix of someone who use and not use our service.

![](RackMultipart20200514-4-7k83uf_html_3dcb5743223b45b9.png)

**Table 2:** Distribution plot of Purchase Frequency

PURCHASES\_TRX : about 75 percentile of customers use our service up to 17 times. There are some unusual usage i.e. up to 358 transactions is quite high.

ONEOFF\_PURCHASES : customers who use our service to pay for small purchases (about 75 percentile who spend a max amount of \&lt;$600).

ONEOFFPURCHASESFREQUENCY : not too many customers who make one-off purchase frequently, we see about 75 percentile customers with \&lt; 0.33 out of 1.

INSTALLMENTS\_PURCHASES : graphs in the coming section will show how installments purchases affects overall customer spending.

PURCHASESINSTALLMENTSFREQUENCY : we see much higher frequency than one-off purchases, 75 percentile customers with \&lt; 0.75 out of 1. This might indicated that this is a popular service choices for most people.

CASH\_ADVANCE : over 50% of customers do not use cash advance feature, where cash advance is 0.0. However, if we look at calculation later on in the study, cash advance actually take up 50% of the overall business.

CASHADVANCEFREQUENCY : we see similar results from before, but this takes up a major part of the business.

CASHADVANCETRX : 75 percentile of our customers make on average 4 transactions, where we see as much as 123 times.

## Data Cleansing and Preparation

There are about ~300 records that are missing minimum payments and credit limit data. Since this is not a great proportion out of the 9000 records (which is about 3% of the data loss), we just removed the affected rows from the dataset. We do not have any duplicate of data because each row is identified by a unique customer id. There are some outliers, but we removed one by one manually when we see there is an anomaly during each modeling step.

#


# Data Understanding

If we wish to group customers into different segments, it is better for us to understand their behaviours first.

![](RackMultipart20200514-4-7k83uf_html_65a7ee973000e7c.png)

**Table 3:** Ratio of balance over Credit Limit

Let&#39;s take a look at (balance/credit\_limit). Just by observing the chart, we know that about 50% of customers who will used up 80% of their Credit limit. If we look at the &quot;outliers&quot; (which is not included in the chart). We have around ~200 cases where their balance is higher than their approved credit limits for certain administrative reasons. But we will safely disregard those cases for now.

![](RackMultipart20200514-4-7k83uf_html_9fce69746f606e79.png)

**Table 4:** Payments over Credit Limit

![](RackMultipart20200514-4-7k83uf_html_76883e7a0ebe71da.png)

**Table 5:** Distribution of Percent Full Payment Made

Although the number from the above chart looks staggering, we do not have enough information to conclude whether &quot;debt&quot; pose a risk to both the company and the customers. However, we are confident that only a handful of customers (~5%) who prefer to pay in full, while others are accumulating debts over time. On the other hand of the spectrum, we see more than 70% of people, who either not need to pay (because they did not use our service at all) or they paid \&lt; 10% of their whole payment.

How customers are using our service?

![](RackMultipart20200514-4-7k83uf_html_7378cbe45ada1a26.png)

**Table 6:** Cash Advance and Purchase Splits

We see a clear split between those who use cash advance and those who use card-swipe purchase exclusively.

![](RackMultipart20200514-4-7k83uf_html_adf7c4ffccbd9479.png)

**Table 7:** Spending Spread

From the first chart, we see most customers have a strong preference for using one service over the other; namely, card purchase or cash advance.

If we do an accumulation over the amount each category made, as we plot this into a pie chart as shown above, we see an interesting mix of ~50/50 over card/cash. Furthermore, customers are still preferring to use our service for purchasing one-off items, but we see installment purchase consist of around ~40% of &quot;card swiping&quot; activity.

The following charts depict the number of transactions and the relationship of purchases.

![](RackMultipart20200514-4-7k83uf_html_5ef621ca73aa28a3.png)

**Table 8:** Purchase Transaction and Purchases

![](RackMultipart20200514-4-7k83uf_html_2be7d980f845abfa.png)

**Table 9:** Cash Advance Transactions

## Pre-modeling

The following matrix contains a preliminary study of how different habits and behaviours should be categorized. We give them an easy name for marketing staff to visualize, i.e. Big Spenders, Frugal Users.
There are two major aggregated features that are of great impact for our modeling calculation: This information helps to give a more accurate depiction of how individual customers are compared. &quot;CREDIT\_LIMIT&quot; has a huge influence on the rest of the calculation, as so the sum of PURCHASES + CASH\_ADVANCE, which is equal to the overall spending that are acquired over a particular month. We capture this information on column &quot;OAS&quot;. We perform further calculations based on these two attributes, (i.e. purchases\_vs\_LIMIT, balance\_vs\_LIMIT, one\_off\_purchase\_vs\_OAS, etc)

![](RackMultipart20200514-4-7k83uf_html_17c353ef4c30d09d.png)

**Table 10:** Customers&#39; Habits and Classification

## Getting visualization from 2-D clustering exercise

Before we start with a full clustering model, we try to build a simple 2-D visualization model with two prevalent variables (CREDIT\_LIMIT, PAYMENTS) to start off. We see a good mix of clusters by observing the charts below. We tried a few more with different number of clusters to see if clustering models do provide &quot;visually&quot; good results. We also did some preliminary evaluation using the dendrogram, elbow graph, etc to see if this is a good modeling method.

![](RackMultipart20200514-4-7k83uf_html_10af9c3456553b30.png)

**Table 11:** 2D Cluster Plot for 2 variables only in the pre-modeling stage, cluster = 4

![](RackMultipart20200514-4-7k83uf_html_bbc3aaab705944b3.png)

**Table 12:** 2D Cluster Plot for 2 variables only in the pre-modeling stage, cluster = 6

![](RackMultipart20200514-4-7k83uf_html_3ad350cb68ef9c49.png)

**Table 13:** 2D Cluster Plot for 2 variables only in the pre-modeling stage, cluster = 8

# K-means Clustering Model

## Bucketing floats into integers and normalizing all variables

After completing a preliminary study with a simplified k-means model from the previous section just using 2 variables, we determine that a full scale model with all 16 variables should be proceeded. First step is to bucket monetary variables into integers from 1-6, representing low to high ranges. Then, we bucket frequency-based variables into integers from 1-10 instead of 0 to 1. We separate transaction-based variables into integers from 1-8. The finally step to prepare the data to fit the model would be to use the StandardScaler() function to ease the model computation.

## Finding the appropriate number clusters through Dendrogram

To further our study, we incorporated all of the features given (except for TENURE rates) to formulate our clustering model. First, we get a rough idea of how clusters are distributed using dendrogram, as shown below:

![](RackMultipart20200514-4-7k83uf_html_6e9937a55d1b237f.png)

**Table 14:** Dendrogram with p = 5

For dendrogram, it&#39;s a form of hierarchical clustering. The major difference between k-means clustering and hierarchical clustering is that k-means starts the evaluation from a centroid while the other is starting a value and work from the bottom up. In table 14, this dendrogram shows the distances relative to each individual value. Notice how the last 3 colours on the right hand side of table laid out. If we were to draw a horizontal line across the chart, it intersects with 6 different colors if we start the line at y = ~ 10 mark. If we were to draw a line slightly below, we get up to 8 different colors, which suggest a good number of clusters to start with.

## Finding the appropriate number clusters through the Elbow Method

A second method for determining an appropriate number of clusters is through the elbow method, we determine the cost (or the inertia) between clusters and data points. We hope to get the right balance, where we have short path from clusters and point, and we want to have a minimum number of clusters in order to have an easier calculations to work with.

![](RackMultipart20200514-4-7k83uf_html_4f2fd66f327257e3.png)

**Table 15:** The Elbow Method

## Silhouette Score for Determining the Optimal Number of Clusters

We run through different cluster sizes (ie. 2-8 clusters) and we choose number of clusters to be 6 for cost versus performance reasons. We found similar results in silhouette score charts from the below. Lower silhouette score indicating that clusters are closer to the centroid. N = 4 gives the best number of 0.1865. However, we will settle with 6 clusters with silhouette score of slightly worse number of 0.1980, because we wish to segregate 9000 customers into more segments for managerial reasons.

For n\_clusters = 2 The average silhouette\_score is : 0.2257

For n\_clusters = 3 The average silhouette\_score is : 0.2112

For n\_clusters = 4 The average silhouette\_score is : 0.1865

For n\_clusters = 5 The average silhouette\_score is : 0.1987

For n\_clusters = 6 The average silhouette\_score is : 0.1980

![](RackMultipart20200514-4-7k83uf_html_2515bc21309f2eb7.png)

**Table 16a:** Silhouette Analysis for n\_clusters = 2

![](RackMultipart20200514-4-7k83uf_html_e742164345ccb39d.png)

**Table 16b:** Silhouette Analysis for n\_clusters = 3

![](RackMultipart20200514-4-7k83uf_html_183747d345ff2cbd.png)

**Table 16c:** Silhouette Analysis for n\_clusters = 4

![](RackMultipart20200514-4-7k83uf_html_b5bb8a67b74d84b8.png)

**Table 16d:** Silhouette Analysis for n\_clusters = 5

![](RackMultipart20200514-4-7k83uf_html_45c843df48d0e5b4.png)

**Table 16e:** Silhouette Analysis for n\_clusters = 6

##


## A Comment on not achieving a Supervised Learning Model

Although we tried a few different supervised learning models (such as random forest tree) in both Jupyter Notebook and Rstudio, but we did not yield a good result because we are lacking of useful targets for any good supervised learning models to build. This is the limitation of our chosen dataset, as it did not give enough target information for any useful outcome to predict. Thus, we settle with the conclusion made by our clustering models.

##


## Final Analysis for k-means clustering with n\_clusters = 6

The final stage is to understand what is behind with the k-means clustering model. The bar graph below shows the accumulated value of occurrence within a cluster for individual variable. From these series of bar graphs, we can visually see how each individual variable affecting a given cluster.

Here, we provide a rundown of how to read the bar graph. It is important to note that the chart will change (i.e. cluster #) for each rerun of notebook. Therefore, cluster # does not necessarily match the behaviors and traits. But we can generalize six different groups and how they would behave.

## Understanding the meaning behind the 6 clusters

The number in the list below shows the tendency for how each 6 different cluster would behave, from cluster #0-5.

**Payment:**

- small: 3, 4, 5
- mid to high: 0, 1, 2

**Paying Full:**

- highly likely: 1, 3, 4
- neutral: 0, 2
- highly unlikely: 5

**Balance Frequency:**

- Active: 0, 1, 2, 4, 5
- Inactive: 3

**Credit Limit &amp; Balance:**

- 0 -\&gt; high credit, low balance
- 1, 2 -\&gt; high credit, high balance
- 3 -\&gt; all range of credit, strong low Balance
- 4 -\&gt; all range of credit, strong low Balance
- 5 -\&gt; higher range of credit, strong mid Balance

**Card Swiping:**

- highly likely buying Luxury: 0
- highly likely buying Small Stuff: 4
- random: 2, 3
- highly unlikely: 1, 5

**One-Off:**

- highly likely: 0
- random: 2
- highly unlikely: 1, 3, 4, 5

**Installment:**

- highly likely: 0, 4
- likely: 2
- highly unlikely: 1, 3, 5

**Cash Advance:**

- highly unlikely: 1, 2, 3, 5
- random: 0, 4

![](RackMultipart20200514-4-7k83uf_html_8a706728bfde9a83.png)

![](RackMultipart20200514-4-7k83uf_html_7389518d910cffb9.png)

![](RackMultipart20200514-4-7k83uf_html_74e6251b41a372ba.png)

![](RackMultipart20200514-4-7k83uf_html_e889b4441c0adcfb.png)

![](RackMultipart20200514-4-7k83uf_html_516a66ccfb31eaaa.png)

![](RackMultipart20200514-4-7k83uf_html_3b9f60c7e8f953f5.png)

![](RackMultipart20200514-4-7k83uf_html_8bab48a8b85996eb.png)

![](RackMultipart20200514-4-7k83uf_html_b911cb63be936ea7.png)

![](RackMultipart20200514-4-7k83uf_html_2ac5f6d647851751.png)

![](RackMultipart20200514-4-7k83uf_html_8567554e92deea87.png)

![](RackMultipart20200514-4-7k83uf_html_5f5eb3cf6fc57af9.png)

![](RackMultipart20200514-4-7k83uf_html_aa317e2897f09e34.png)

![](RackMultipart20200514-4-7k83uf_html_2b2ed14620ce7b22.png)

![](RackMultipart20200514-4-7k83uf_html_457820b05d2f0608.png)

![](RackMultipart20200514-4-7k83uf_html_9f4250bfa0f7f73a.png)

![](RackMultipart20200514-4-7k83uf_html_16cf2a59265c3cac.png)

**Table 17:** Facet Grid of 16 variables vs 6 clusters

## Matching Cluster Grouping with Customers ID

Finally, we attach the clustering results back into our dataframe. This will give us the result for customers who falls into each different segment.

![](RackMultipart20200514-4-7k83uf_html_3df3cbfbee018944.png)

**Table 18:** Customers who belongs to appropriate clusters.

## Visualization of the clusters

![](RackMultipart20200514-4-7k83uf_html_7b6e1803032da4d3.png)

**Table 19:** Customers Segmentation based on their Credit Card usage behaviors

| Colors | Names |
| --- | --- |
| redbluegreenyelloworangepurple | who make all types of purchasesmore people with due paymentswho purchases mostly in installmentswho take more cash in advancewho make expensive purchaseswho don&#39;t spend much money |

**Table 20:** Detail for each Customer Segment

# Conclusion

We have segmented the customers according to their credit card usage attributes into the numbers of clusters who share similar purchasing patterns, behaviours and traits.

We used Dendrogram and Elbow Method to find an appropriate number of clusters. We have chosen number of clusters to be 6 for cost over performance reasons. Similar results were found by using a Silhouette Score .

Due to the lack of labelled data, we were unable to build any classification/regression task. Although we tried a few different scenarios and models using random forest, but we did not yield a good result because we were lacking of useful targets for any good supervised learning models to build.

Based on the result we got, we can market different credit card products to different groups. For example, for yellow group who take more cash in advance, we can market them the credit cards with less interest on cash withdrawals. For the red group who make all types of purchases, we can market a card with higher percentage cashback so that they can get more cashback with the purchase. For the orange group who make expensive purchases, we can offer them the credit card with a higher credit card limit.

#


# Deployment

This model is useful for the financial institutions to target credit card holders based on their financial and spending habits. This model helps these institutions to arrange a better service for their customers. By using this clustering models, users can segregate customers into different categories when their financial and spending habits are given. This model can be improved by including the following information to complement the existing dataset, which predominantly based on financial and spending habits.

1. Provide gender and other related information about individual user
2. Provide geographical location on spending
3. provide further information on the type of spending made
4. Provide time-variant of this dataset, such as holiday spending

However, the first stage of deployment should be as follows:

1. create a pilot program for various departments that are interested in reaching out targeted customer base.
2. btain feedback from these departments to determine how successful with their campaigns.
3. adjust and fine-tune the model with timely and broadened information as indicated above.

This model should be reviewed and updated every 6-12 months, as we wish to find out whether there is a change of consumer behaviors. This might be due to changes in external factors that are not depicted in our model.

# References

[1] Arjun Bhasin, Credit Card Dataset for Clustering [https://www.kaggle.com/arjunbhasin2013/ccdata/data#](https://www.kaggle.com/arjunbhasin2013/ccdata/data#)

[2] Malik, U. Hierarchical Clustering with Python and Scikit-Learn. Stack Abuse. [https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/](https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/)

[3] Selecting the number of clusters with silhouette analysis on KMeans clustering. Scikit-learn.org. [https://scikit-learn.org/stable/auto\_examples/cluster/plot\_kmeans\_silhouette\_analysis.html](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)