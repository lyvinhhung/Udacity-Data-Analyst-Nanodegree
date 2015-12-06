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

Question 2: *What features did you end up using in your POI identifier, and what selection process did you use to pick them? Did you have to do any scaling? Why or why not? As part of the assignment, you should attempt to engineer your own feature that does not come ready-made in the dataset -- explain what feature you tried to make, and the rationale behind it. *

> I used scikit-learn `SelectKBest` to select best 10 influential features and used those featuers for all the upcoming algorithm. Unsurprisingly, 9 out of 10 features related to financial data and only 1 features called `shared_receipt_with_poi` (messages from/to the POI divided by to/from messages from the person).
were attempted to engineere by us. Main purpose of composing `ratio of POI message` is we expect POI contact each other more often than non-POI and the relationship could be non-linear. After feature engineering & using `SelectKBest`, I then scaled all features using `min-max scalers`. As briefly investigated through exporting CSV, we can see all email and financial data are varied by several order of magnitudes. Therefore, it is vital that we feature-scaling for the features to be considered evenly. 

Question 3: *What algorithm did you end up using? What other one(s) did you try? How did model performance differ between algorithms?*

> After trying more than 10 algorithm and found K-Mean Clustering, Random Forest Classifer, Support Vector Machine & Logistic Regression (not covering in class) have the potential to be improved further. Without any tuning, K-means clustering performed reasonably sufficient with precision & recall rate both larger than 0.3. Logistic regression is using widely in medical & law field, most prominent case is to predict tumor benign/malignancy or guilty/no-guilty law case and I would love to test 

The final algorithm that I ended up using was a logistic regression. Although not covered in class, the primary reason and motivation for using this was because the prediction outcomes were of binary classification (POI or non-POI). A canonical case use for logistic regression is tumor benign/malignancy prediction based off of measurements and medical test results, and I sought to emulate this behavior in predicting whether or not someone was a person of interest based off of their financial and email behavior.

I tried several algorithms, with a K-means clustering algorithm performing reasonably sufficient. Unsurprisingly, K-means clustering performed well, as the objective was to segregate the dataset into POI/non-POI groups. I also tested, with marginal success, an AdaBoost classifier, a support vector machine, a random forest classifier, and stochastic gradient descent (using logistic regression).

I tuned the parameters of the logistic regression and K-means clustering classifiers using exhaustive searches with the following parameters:

Logistic regression: C (inverse regularization parameter), tol (tolerance), and class_weight (over/undersampling)
K-means clustering: tol
K-means clustering was initialized with K (n_clusters) of 2 to represent POI and non-POI clusters. Additionally, K-means performed better by including only the 8 best features and the 2 additional features.

Interestingly, the inclusion of auto-weighting in logistic regression (selection of feature weights inversely proportional to class frequencies) improved recall at the expense of precision. I opted to remove auto-weighting and maintain the evenly weighted feature-scaling discussed in the previous section.

The other algorithms were tuned experimentally, with unremarkable improvement.


