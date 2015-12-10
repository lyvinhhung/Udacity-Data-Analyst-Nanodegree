## Design and Analyze A/B Testing - Udacity Free Trial Screener
by Tommy Ly, in fulfillment of Udacity's [Data Analyst Nanodegree](https://www.udacity.com/course/nd002), Project 7

### 1. Experiment Design
#### 1.1 Metric Choice
> List which metrics you will use as invariant metrics and evaluation metrics here.

+ Invariant metrics: Number of cookies, Number of clicks, Click-through-probability
+ Evaluation metrics: Gross conversion, Retention, Net conversion
 

> For each metric, explain both why you did or did not use it as an invariant metric and why you did or did not use it as an evaluation metric. Also, state what results you will look for in your evaluation metrics in order to launch the experiment.

+ Number of cookies: Number of unique cooirs to visit the course overview page. Unit of Diversion is cookies, it's evenly distributed in control and experiment group. Also, the visits happen before the users see the experiment and thus independent from it.
+ Number of clicks: 
+ Gross conversion:
+ Retention:
+ Net conversion:

#### 1.2 Measuring Standard Deviation
> List the standard deviation of each of your evaluation metrics

#### 1.3 Sizing
##### 1.3.1 Number of Samples vs. Power
> Indicate whether you will use the Bonferroni correction during your analysis phase, and give the number of pageviews you will need to power you experiment appropriately.

##### 1.3.2 Duration vs. Exposure
> Indicate what fraction of traffic you would divert to this experiment and, given this, how many days you would need to run the experiment.

### 2. Experiment Analysis
#### 2.1 Sanity Checks
> For each of your invariant metrics, give the 95% confidence interval for the value you expect to observe, the actual observed value, and whether the metric passes your sanity check.

### References:
- [Introduction to Machine Learning (Udacity)](https://www.udacity.com/course/viewer#!/c-ud120-nd)
- [MITx Analytics Edge](https://www.edx.org/course/analytics-edge-mitx-15-071x-0)
- [scikit-learn Documentation](http://scikit-learn.org/stable/documentation.html)

### Files
- `readme`: main submission file - Analyze & Design A-B Testing


