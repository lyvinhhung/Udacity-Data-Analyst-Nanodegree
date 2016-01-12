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
> Follow up question: If you were given an identical box of chocolates and again eat four pieces in a row, what is the probability that exactly two contain coconut filling?

Within first 4 pieces of box of chocolates, there're 14 combinations 
```
Example:
Combination 1: Orange, Orange, Orange, Coconut 
Combination 2: Orange, Coconut, Coconut, Orange
Combination 3: Orange, Coconut, Coconut, Coconut
Combination 4: Coconut, Coconut, Coconut, Coconut
....
Combination 14.

Within those 14 combinations, there're 5 combinations have exactly 2 coconuts

Therefore, we have P(exactly 2 coconuts in 14 combinations) = 5/14 = 35.71%
```

##### 3. Programming

> Construct a query to find the top 5 states with the highest number of active users. Include the number for each state in the query result.

```
SELECT state, SUM(active)
from users
GROUP BY state
ORDER BY SUM(active) DESC
LIMIT 5
```

> Define a function `first_unique` that takes a string as input and returns the first non-repeated (unique) character in the input string. If there are no unique characters return None. Note: Your code should be in Python.

```
def first_unique(word):
    count = {}
    for c in word:
        if c not in count:
            count[c] = 0
        count[c] += 1
    for c in word:
        if count[c] == 1:
          return c
        elif count[c] != 1:
          return "None"
```

##### 4. Data Analysis

> What are underfitting and overfitting in the context of Machine Learning? How might you balance them?

Let's say we attend a symphony and want to get the clearest, most faithful sound possible. So we buy a extremely-sensitive microphone and hearing aid to pick up all the sounds in the auditorium.
Then we start "overfitting," hearing the noise on top of the symphony. We hear our neighbors moving in their seats, the musicians turning their pages or even sneezing of the audiences afar.
When we're at a concert, there's both the symphony and the random noise. Fitting a perfect model is only listening to the symphony. Over-fitting is when you hear more noise then you need to, and underfitting is the quality of the symphony sound is not as amazing as it should be since all the goodness of the symphony is not fully capture by a bad microphone.

To balance overfitting, we can go for simpler model with fewer parameters to tune & remove the parameters that add little improvement to the result. The other method is to use cross validation, splitting the data into 3:1 or 4:1 ratio and conduct multiple trials (if the dataset is too small).

##### 5. Future Plan

> If you were to start your data analyst position today, what would be your goals a year from now?

Job I want to apply to : https://careers-uber.icims.com/jobs/13612/global-data-analyst%2c-singapore/job?mobile=false&width=1048&height=500&bga=true&needsRedirect=false&jan1offset=420&jun1offset=420

Within the Uber sphere, my goal is to become technically sufficient in SQL & Python, matching with Uber needs as a Global Data Analyst. 

Within the first 3 months, my goal are:

1. Understand nuts and bolts of every single database scheme in Uber, especially Uber Asia Pacific.
2. Have a clear knowledge of every Uber metrics/KPIs needed to operate in Asia Pacific.
3. Ability to do fundamental data analysis task for Uber (A/B testing, statistical inference,etc.)

Within one year, my goal are:

1. Code fluently in Python to develop new innovative metrics to track for Uber.
2. Query database cold & create new assumptions/hypothesis and test it. For example: I'd suspect Uber customers are increasingly parents (doesn't have time to pick-up children & use Uber for alternative to school-bus) so I'd collect data & conduct a statistical test to test if this is true, and how could we target those new emerging segment.
3. Develop new data product (an internal platform for Uber drivers or Uber data team).E.g an automate tool to calculate A/B testing result & experiement (split the data & conduct statistical analysis automatically with a few click of a button).

