## Enron Fraud Detectors using Enron Emails and financial Data.
by Tommy Ly, in fulfillment of Udacity's [Data Analyst Nanodegree](https://www.udacity.com/course/nd002), Project 5

### Short Questions
__Question 1: *Summarize for us the goal of this project and how machine learning is useful in trying to accomplish it. As part of your answer, give some background on the dataset and how it can be used to answer the project question. Were there any outliers in the data when you got it, and how did you handle those?*__

The goal of this project is to use  financial and email data from [Enron corpus](https://www.cs.cmu.edu/~./enron/) - publicly maed by US Federal Energy Regulatory Comission during its investgiation of Enron, which comprised email and financial data of 146 people (records), most of which are senior management of Enron, to come up with a predictive model that could spot an individual as a "Person of Interest (POI). The corpus is widely used for various machine learning problem and although it has been labeled aready, the value is the potential application for similar cases in other companies or spam filtering application. The dataset contained 146 records with 1 labeled feature (POI), 14 financial features, 6 email feature. Within these record, 18 were labeled as a "Person Of Interest" (POI).

Enron was among Fortune 500 in U.S in 2000. By 2002, it collapsed due to corporate fraud resulting from Federal Investigation, there was thousands of records (e-mail & financial data). Most notable of which are Jefferey Skilling, Key Lay, and Fastow all have dumped large amounts of stock options, and they are all deemed guilty

I use `scikit-learn` & various machine learning techniques to predict "Person fo Interest", detecting culpable person using both financial & email-data. Through exploratory data analysis and CSV check, I was able 3 records need to be removed:

- `TOTAL`: Through visualising using scatter-plot matrix. We found `TOTAL` are the extreme outlier since it comprised every financial data in it.
- `THE TRAVEL AGENCY IN THE PARK`: This must be a data-entry error that it didn't represent an individual.
- `LOCKHART EUGENE E`: This record contained only NaN data.

__Question 2: *What features did you end up using in your POI identifier, and what selection process did you use to pick them? Did you have to do any scaling? Why or why not? As part of the assignment, you should attempt to engineer your own feature that does not come ready-made in the dataset -- explain what feature you tried to make, and the rationale behind it.*__

I used scikit-learn `SelectKBest` to select best 10 influential features and used those featuers for all the upcoming algorithm. Unsurprisingly, 9 out of 10 features related to financial data and only 1 features called `shared_receipt_with_poi` (messages from/to the POI divided by to/from messages from the person) were attempted to engineere by us. Main purpose of composing `ratio of POI message` is we expect POI contact each other more often than non-POI and the relationship could be non-linear. After feature engineering & using `SelectKBest`, I then scaled all features using `min-max scalers`. As briefly investigated through exporting CSV, we can see all email and financial data are varied by several order of magnitudes. Therefore, it is vital that we feature-scaling for the features to be considered evenly. 

__Question 3: *What algorithm did you end up using? What other one(s) did you try? How did model performance differ between algorithms?*__

After trying more than 10 algorithm and found K-Mean Clustering, Random Forest Classifer, Support Vector Machine & Logistic Regression (not covering in class) have the potential to be improved further. Without any tuning, K-means clustering performed reasonably sufficient with precision & recall rate both larger than 0.3. Logistic regression is using widely in medical & law field, most prominent case is to predict tumor benign/malignancy or guilty/no-guilty law case and I would love to test, and recently with e-mail spamming classifer. Although initially, the result was not as expected, I believe with further tuning we can come up with a much better result. 

With every algorithms, I tried to tune as much as I could with only marginal success & unremmarkable improvement but come up with significant success with Logistic Regression & K-Mean Clustering. Manually searching through the documentation, I came up with these following paremeters:

Logistic regression: C (inverse regularization), class weight (weights associated with classes), max iteration (maximum number of iterations taken for the solvers to converge), random_state (the seed of the pseudo random number generator to use when shuffling the data), solver (using 'liblinear' since we have very small dataset).

```
C=1e-08, class_weight=None, dual=False, fit_intercept=True, intercept_scaling=1, 
max_iter=100, multi_class='ovr', penalty='l2', random_state=42, solver='liblinear', tol=0.001, verbose=0))

```
K-means clustering: 

```
KMeans(copy_x=True, init='k-means++', max_iter=300, n_clusters=2, n_init=10,
       n_jobs=1, precompute_distances='auto', random_state=None, tol=0.001,
      verbose=0)
```

__Question3:*What is validation, and what’s a classic mistake you can make if you do it wrong? How did you validate your analysis?*__
