## Udacity Data Analyst Sample Interview Questions

by Tommy Ly, in fulfillment of Udacity's [Data Analyst Nanodegree](https://www.udacity.com/course/nd002), Project Dry-run interview.

##### 1. Data Project Experience

> Describe a data project you worked on recently.

The goal of my project is to use financial and email data from Enron - which comprised email and financial data of 146 people (records), most of which are senior management of Enron, to come up with a predictive model that could spot an individual as a "Person of Interest (POI). I use `scikit-learn` & various machine learning techniques to predict "Person fo Interest", detecting culpable person using both financial & email-data. 

First, I used scikit-learn `SelectKBest` to select best 10 influential features and used those featuers for all the upcoming algorithm. After feature engineering & using `SelectKBest`, I then scaled all features using `min-max scalers` so we can prevent data not to have several of magnitudes difference . Next, I use parameter tuning in order to improve the fit on the test set, there're multiple parameters can be tuned for logistic regression. 

Next, I use validation techniques to make sure our model generalizes with the remaining part of the dataset. In detail, I split the data into 3:1 ratio & create 1000 trials. Main reason why I'd create too many trials since the dataset is very small and with small number of trials, the data might be bias. Finally, I evaluate the mdel using `precision` & `recall` rather than `accuracy` since if everyone is flagged as Person of Interest, the accuracy would be 100% and shows irrelevant data.

##### 2. Probability

> You are given a ten piece box of chocolate truffles. You know based on the label that six of the pieces have an orange cream filling and four of the pieces have a coconut filling. If you were to eat four pieces in a row, what is the probability that the first two pieces you eat have an orange cream filling and the last two have a coconut filling?

The problem is within `dependent probabilities` sphrere and can be calculated as follow:

Probability of first choice to be orange: 
```
P(1st orange): 6/10
```
Probability of second choice to be orange: 
```
P(2nd orange): 5/9
```
Probability of third choice to be coconut: 
```
P(3rd coconut): 4/8
```
Probability of fourth choice to be coconut: 
```
P(4th coconut): 3/7
```
Total Probably 
```
P(1st orange and 2nd orange and 3rd cocut and 4th coconut) = P(1)*P(2)*P(3)*P(4) = 7.14%
```

##### 3. Programming

> Construct a query to find the top 5 states with the highest number of active users. Include the number for each state in the query result.



> Define a function `first_unique` that takes a string as input and returns the first non-repeated (unique) character in the input string. If there are no unique characters return `None`. Note: Your code should be in Python.

##### 4. Data Analysis

> What are underfitting and overfitting in the context of Machine Learning? How might you balance them?

##### 5. Future Plan

> If you were to start your data analyst position today, what would be your goals a year from now?
