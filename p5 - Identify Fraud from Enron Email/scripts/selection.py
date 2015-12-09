import pickle
import sys
from pprint import pprint
from time import time
import numpy as np
import logging

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

from sklearn.feature_selection import SelectKBest
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.preprocessing import StandardScaler
from sklearn.grid_search import GridSearchCV


def select_k_best_features(dataset, features_list, k):
    """
    For E+F dataset, select k best features based on SelectKBest from 
    sklearn.feature_selection

    Input:
    dataset: data in dictionary format 
    features_list: the full list of features to selection from 
    k: the number of features to keep

    Return:
    the list of length of k+1 with the first element as 'poi' and other 
    k best features 

    """
    labels_train, __, features_train, __ = \
    test_training_stratified_split(dataset, features_list)
    
    k_best = SelectKBest(k=k)
    k_best.fit(features_train, labels_train)
    impt_unsorted = zip(features_list[1:], k_best.scores_)
    impt_sorted = list(sorted(impt_unsorted, key=lambda x: x[1], reverse=True))
    k_best_features = [elem[0] for elem in impt_sorted][:k]
    print k, "best features:"
    print k_best_features
    return ['poi'] + k_best_features

def test_training_stratified_split(dataset, features_list, testsize=0.2):
    """
    For E+F dataset, split dataset into the training and test 
    set using stratified method.

    Input:
    dataset: data in dictionary format 
    features_list: the full list of features to selection from 
    test: the proportion of the dataset to include in the test split

    Return:
    labels_train, labels_test, features_train, features_test

    """
    data = featureFormat(dataset, features_list, sort_keys = True)
    labels, features = targetFeatureSplit(data)
    labels = np.array([int(label) for label in labels])
    features = np.array(features)
    ### Split data into test set and training set
    sss = StratifiedShuffleSplit(labels, 1, test_size=testsize, random_state=0)

    for train_index, test_index in sss:
        labels_train, labels_test = labels[train_index].tolist(), labels[test_index].tolist()
        features_train, features_test = features[train_index].tolist(), features[test_index].tolist()
    return labels_train, labels_test, features_train, features_test


def best_parameter_from_search(pipeline, parameters, score_func, dataset, features_list, kf = 10):
    """ 
    print out the optimal parameters of pipeline classifier from grid search based on 
    score function of choice
    
    Input:
    pipeline: classifier in pipeline form
    parameters: the parameters to be grid searched
    score_func: Scorer function used on the held out data to choose the best parameters for the model
    dataset: data in dictionary format
    features_list: the list of feature after feature selection
    kf: kf-fold of cross validation for estimation
    """
    labels_train, labels_test, features_train, features_test = \
    test_training_stratified_split(dataset, features_list)

    ### Stratified ShuffleSplit cross validation iterator of the training set
    cv_sss = StratifiedShuffleSplit(labels_train, n_iter=kf, test_size=0.2, random_state=0)

    clf = GridSearchCV(pipeline, parameters, scoring=score_func, cv=cv_sss, n_jobs=-1, verbose=1)

    print("Performing grid search...")
    print("pipeline:", [name for name, _ in pipeline.steps])
    print("parameters:")
    pprint(parameters)
    t0 = time()
    clf.fit(features_train, labels_train)
    print "done in %0.3fs" % (time() - t0)
    print
    print("Best score: %0.3f" % clf.best_score_)
    print("Best parameters set:")
    best_parameters = clf.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))
    return clf

def precision_n_recall(pipeline, parameters, my_dataset, features_list):
    ## Two Scores for evaluation of the performance of different models
    scores = ['precision', 'recall', 'f1']

    for score_name in scores:
        print "# Tuning hyper-parameters for %s" % score_name
        print
        clf = best_parameter_from_search(pipeline, parameters, score_name, my_dataset, features_list)
        print "========================================================="