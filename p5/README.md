## Enron Fraud Detectors using Enron Emails and financial Data.
by Tommy Ly, in fulfillment of Udacity's [Data Analyst Nanodegree](https://www.udacity.com/course/nd002), Project 5

### Short Questions
Question 1: *Summarize for us the goal of this project and how machine learning is useful in trying to accomplish it. As part of your answer, give some background on the dataset and how it can be used to answer the project question. Were there any outliers in the data when you got it, and how did you handle those?*
> The goal of this project is to use  financial and email data from [Enron corpus](https://www.cs.cmu.edu/~./enron/) - publicly maed by US Federal Energy Regulatory Comission during its investgiation of Enron, which comprised email and financial data of 146 people (records), most of which are senior management of Enron, to come up with a predictive model that could spot an individual as a "Person of Interest (POI). The corpus is widely used for various machine learning problem and although it has been labeled aready, the value is the potential application for similar cases in other companies or spam filtering application. The dataset contained 146 records with 1 labeled feature (POI), 14 financial features, 6 email feature. Within these record, 18 were labeled as a "Person Of Interest" (POI).

> Enron was among Fortune 500 in U.S in 2000. By 2002, it collapsed due to corporate fraud resulting from Federal Investigation, there was thousands of records (e-mail & financial data). Most notable of which are Jefferey Skilling, Key Lay, and Fastow all have dumped large amounts of stock options, and they are all deemed guilty

> I use `scikit-learn` & various machine learning techniques to predict "Person fo Interest", detecting culpable person using both financial & email-data. Through exploratory data analysis and CSV check, I was able 3 records need to be removed:

>
- `TOTAL`: Through visualising using scatter-plot matrix. We found `TOTAL` are the extreme outlier since it comprised every financial data in it.
- `THE TRAVEL AGENCY IN THE PARK`: This must be a data-entry error that it didn't represent an individual.
- `LOCKHART EUGENE E`: This record contained only NaN data.

Question 2: *What features did you end up using in your POI identifier, and what selection process did you use to pick them? Did you have to do any scaling? Why or why not? As part of the assignment, you should attempt to engineer your own feature that does not come ready-made in the dataset -- explain what feature you tried to make, and the rationale behind it. (You do not necessarily have to use it in the final analysis, only engineer and test it.) In your feature selection step, if you used an algorithm like a decision tree, please also give the feature importances of the features that you use, and if you used an automated feature selection function like SelectKBest, please report the feature scores.*



