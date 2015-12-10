## Design and Analyze A/B Testing - Udacity Free Trial Screener
by Tommy Ly, in fulfillment of Udacity's [Data Analyst Nanodegree](https://www.udacity.com/course/nd002), Project 7

### 1. Experiment Design
#### 1.1 Metric Choice
> List which metrics you will use as invariant metrics and evaluation metrics here.

+ Invariant metrics: Number of cookies, Number of clicks, Click-through-probability
+ Evaluation metrics: Gross conversion, Retention, Net conversion
 

> For each metric, explain both why you did or did not use it as an invariant metric and why you did or did not use it as an evaluation metric. Also, state what results you will look for in your evaluation metrics in order to launch the experiment.

+ __Number of cookies__ (_Number of unique users to visit the course overview page_): Unit of Diversion is cookies, it's evenly distributed in control and experiment group. Also, the visits happen before the users see the experiment and thus independent from it.
+ __Number of clicks__ (_Numer of unique cookies to click the start free trial button_): As the click happen before the users see the experiement and independent from it. Explicitly speaking, the page asking the number of hours of the student devotion after clicking "Start free Trial" button, but the course overview page remains the same for both control & experiment group. 
+ __Gross conversion__ (_Number of users who enrolled in the free trial/Number of users who clicked the Start Free Trial button_): A good evaluation metrics since it's directly dependent on the effect of the experiment & allow us to show whether we managed to decrease the cost of enrolment aren't likely to be real customers. In detail, in the experiment group the user can make a decision, if he has enough time to devote for course, he will be enrolled or if not, he will continue with the free courseware without enrolling. Vice versa, for the control group, no pop-up would be displayed regardless of the time availabilit enrolls for the course. The underlying assumption would be the gross conversion in the control group is higher than experiment group Therefore, it can be used as an evaluation metric to check if the experiement makes a significant difference in the enrolment. 
+ __Retention__ (_Number of user-ids to remain enrlled for 14 days trial period and make their first payment/Number of users who enrolled in the free trial_): The rentention might be high for the experiment group, since few users enrolled based on their time commitment. But for the control group, many users enroll for the courseware, since not many of them have the required time, the cancellation rate might be high and hence the retention rate will be low. 
+ __Net conversion__ (_Number of user-ids remained enrolled for 14 days trial and at least make their first payment/Number of users clicked the Start Free Trial button_): For the experiment group, users aware of the time commitment requirement through the screener page and can make a decision to remain enrolled for the course past 14 days trial-period. However, on the control group side, they would be able to continue the payment wouthout aware of the minimum time requirement. Therfore, it can be used as Evaluation metric.

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


