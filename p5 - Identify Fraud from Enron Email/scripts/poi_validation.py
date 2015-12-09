# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:03:40 2015

@author: fch

Library for validating an sk-learn predictive model.

This module provides validation functions for sk-learn POI prediction models built
    as part of the Udacity Data Analyst Nanodegree Program.

Available functions include:
- validate: Make a pipeline for cross-validated grid search for the
        first model reported.
"""

import sys

from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score

def validate(clf=None, labels_df=None, features_df=None, 
             n_iter=1000, test_size=0.1):
    '''Validates an sk-learn calssification model using StratifiedShuffleSplit 
    with metrics averaged over N different randomized cross-validation splits.
        
    Validates an sk-learn model using classification metrics(F1-score, recall, 
       and precision) averaged over N different randomized stratified cross-
       validation splits.
       
    Args:
        clf: The sk-learn classification model being validated.
        labels_df: Pandas dataframe of labels to predict.
        features_df: Pandas dataframe of features used to predict labels.
        n_iter: Number of random cross validation runs to average over.
        test_size: The percentage size of the test set to split off during each
            run.
    Returns:
        Prints to stdout the evaluation average evaluation metrics for F1
            score, recall, and precission.
    '''
    n_iter = 1000
    sk_fold = StratifiedShuffleSplit(labels_df, n_iter=n_iter, test_size=0.1)
    f1_avg = []
    recall_avg = []
    precision_avg = []
    # Enumerate through the cross-validation splits get an index i for a timer
    for i, all_index in enumerate(sk_fold):
        train_index = all_index[0]
        test_index = all_index[1]

        X_train = features_df.irow(train_index)
        y_train = labels_df[train_index]
        
        X_test = features_df.irow(test_index)        
        y_test = labels_df[test_index]
        
        # Use the best estimator trained earlier to fit
        # grid_search_object.best_estimator_.fit(X_train, y=y_train)
        test_pred = clf.predict(X_test)
        
        # Each time i is divsible by 10, print the 10% to console.
        if i % round(n_iter/10) == 0:
            sys.stdout.write('{0}%.. '.format(float(i)/n_iter*100)) 
            sys.stdout.flush()        
        f1_avg.append(f1_score(y_test, test_pred))
        precision_avg.append(precision_score(y_test, test_pred))
        recall_avg.append(recall_score(y_test, test_pred))
    
    print "Done!"
    print ""
    print "F1 Avg: ", sum(f1_avg)/n_iter
    print "Precision Avg: ", sum(precision_avg)/n_iter
    print "Recall Avg: ", sum(recall_avg)/n_iter