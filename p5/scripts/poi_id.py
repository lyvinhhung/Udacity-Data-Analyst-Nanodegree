#!/usr/bin/python
import pandas as pd
import sys
import pickle
import csv
import matplotlib.pyplot as plt

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import test_classifier, dump_classifier_and_data
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedShuffleSplit
from poi_model import *
from poi_add_features import *
from poi_data import *

pd.options.display.mpl_style = 'default'
############# Task 1: Select what features you'll use.############

target_label = 'poi'
email_features_list = [
    'from_messages',
    'from_poi_to_this_person',
    'from_this_person_to_poi',
    'shared_receipt_with_poi',
    'to_messages',
    ]
financial_features_list = [
    'bonus',
    'deferral_payments',
    'deferred_income',
    'director_fees',
    'exercised_stock_options',
    'expenses',
    'loan_advances',
    'long_term_incentive',
    'other',
    'restricted_stock',
    'restricted_stock_deferred',
    'salary',
    'total_payments',
    'total_stock_value',
]

features_list = [target_label] + financial_features_list + email_features_list

### Load the dictionary containing the dataset
data_dict = pickle.load(open("final_project_dataset.pkl", "r") )

### 1.1.0 Explore csv file 
def make_csv(data_dict):
    """ generates a csv file from a data set"""
    fieldnames = ['name'] + data_dict.itervalues().next().keys()
    with open('data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in data_dict:
            person = data_dict[record]
            person['name'] = record
            assert set(person.keys()) == set(fieldnames)
            writer.writerow(person)

### 1.1.1 Dataset Exploration
print('# Exploratory Data Analysis #')
data_dict.keys()
print('Total number of data points: %d' % len(data_dict.keys()))
num_poi = 0
for name in data_dict.keys():
    if data_dict[name]['poi'] == True:
        num_poi += 1
print('Number of Persons of Interest: %d' % num_poi)
print('Number of people without Person of Interest label: %d' % (len(data_dict.keys()) - num_poi))


###1.1.2 Feature Exploration
all_features = data_dict['ALLEN PHILLIP K'].keys()
print('Each person has %d features available' %  len(all_features))
### Evaluate dataset for completeness
missing_values = {}
for feature in all_features:
    missing_values[feature] = 0
for person in people:
    records = 0
    for feature in all_features:
        if data_dict[person][feature] == 'NaN':
            missing_values[feature] += 1
        else:
            records += 1

### Print results of completeness analysis
print('Number of Missing Values for Each Feature:')
for feature in all_features:
    print("%s: %d" % (feature, missing_values[feature]))

### Task 1.2: Fix out of sync records.
data_dict = fix_records(data_dict)

 
################# Task 2: Remove outliers #####################

def PlotOutlier(data_dict, feature_x, feature_y):
    """ Plot with flag = True in Red """
    data = featureFormat(data_dict, [feature_x, feature_y, 'poi'])
    for point in data:
        x = point[0]
        y = point[1]
        poi = point[2]
        if poi:
            color = 'red'
        else:
            color = 'blue'
        plt.scatter(x, y, color=color)
    plt.xlabel(feature_x)
    plt.ylabel(feature_y)
    plt.show()

# 2.1 Visualise outliers
print(PlotOutlier(data_dict, 'total_payments', 'total_stock_value'))
print(PlotOutlier(data_dict, 'from_poi_to_this_person', 'from_this_person_to_poi'))
print(PlotOutlier(data_dict, 'salary', 'bonus'))
#Remove outlier TOTAL line in pickle file.
data_dict.pop( 'TOTAL', 0 )


# 2.2 Function to remove outliers
def remove_outlier(dict_object, keys):
    """ removes list of outliers keys from dict object """
    for key in keys:
        dict_object.pop(key, 0)

outliers = ['TOTAL', 'THE TRAVEL AGENCY IN THE PARK', 'LOCKHART EUGENE E']
remove_outlier(data_dict, outliers)
    
################ Task 3: Create new feature(s) ####################

# create new copies of dataset for grading
my_dataset = data_dict

## add new features to dataset
def compute_fraction(poi_messages, all_messages):
    """ return fraction of messages from/to that person to/from POI"""    
    if poi_messages == 'NaN' or all_messages == 'NaN':
        return 0.
    fraction = poi_messages / all_messages
    return fraction

for name in my_dataset:
    data_point = my_dataset[name]
    from_poi_to_this_person = data_point["from_poi_to_this_person"]
    to_messages = data_point["to_messages"]
    fraction_from_poi = compute_fraction(from_poi_to_this_person, to_messages)
    data_point["fraction_from_poi"] = fraction_from_poi
    from_this_person_to_poi = data_point["from_this_person_to_poi"]
    from_messages = data_point["from_messages"]
    fraction_to_poi = compute_fraction(from_this_person_to_poi, from_messages)
    data_point["fraction_to_poi"] = fraction_to_poi

# create new copies of feature list for grading
my_feature_list = features_list+['to_messages', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi',
                                 'shared_receipt_with_poi', 'fraction_to_poi']

# extract the features specified in features_list
data = featureFormat(my_dataset, my_feature_list)
# split into labels and features (this line assumes that the first
# feature in the array is the label, which is why "poi" must always
# be first in the features list
labels, features = targetFeatureSplit(data)

df = add_totals(df, email_data=False, financial_data=True)

###############################################################################
# Uncomment to add more features. Docstrings can be found in poi_add_features.py
# df = add_financial_ratios(df, to_payment=True, to_stock=False, to_total=True)
# df = add_email_ratios(df, to_message=False, from_messages=False,             #
#                     to_total=False, active_ratios=True)                     #
# df = fill_zeros(df, include_inf=True)                                        #
# df = add_squares(df, square_email=False, square_financial=True)              #
###############################################################################

### Store to my_dataset for easy export below.
# my_dataset = data_dict



### Task 4: Try a variety of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html



## __name__ must == '__main__' to run parallel processing/forking in Windows
if __name__ == "__main__":
    #make_csv(data_dict)
    # Also removes any rows that have no entries at all. 
    # This includes only one records with no data, Eugene E. Lockhart
    X_df, y_df = features_split_pandas(df, remove_zeros_rows=True)

    X_features = list(X_df.columns)
    features_list = ['poi'] + X_features


    ### Task 5: Tune your classifier to achieve better than .3 precision and recall 
    ### using our testing script.
    ### Because of the small size of the dataset, the script uses stratified
    ### shuffle split cross validation. For more info: 
    ### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

    # StratifiedShuffleSplits for 1000 internal cross-validation splits
    # within the grid-search.
    sk_fold = StratifiedShuffleSplit(y_df, n_iter=1000, test_size=0.1)
    
    pipeline = get_LogReg_pipeline()
    params = get_LogReg_params(full_search_params=False)        
    
    #pipeline = get_LSVC_pipeline()
    #params = get_LSVC_params(full_search_params=False)
    
    #pipeline = get_SVC_pipeline()
    #params = get_SVC_params(full_search_params=False)
         
    # scoring_metric: average_precision, roc_auc, f1, recall, precision
    scoring_metric = 'recall'
    grid_searcher = GridSearchCV(pipeline, param_grid=params, cv=sk_fold,
                           n_jobs=-1, scoring=scoring_metric, verbose=0)
    ###########################################################################
    # Uncomment to see the tester.py cross-validated scores of the model      #
    # with the top 9 features selected from the entire dataset outside of     #
    # of the cross-validation loops. Also must import from poi_snoop.py                                        #
    # top_features_all = get_top_features_all_data(X_df, y_df, grid_searcher, top_N=9)    
    ###########################################################################
    grid_searcher.fit(X_df, y=y_df)
    
    mask = grid_searcher.best_estimator_.named_steps['selection'].get_support()
    top_features = [x for (x, boolean) in zip(X_features, mask) if boolean]
    n_pca_components = grid_searcher.best_estimator_.named_steps['reducer'].n_components_
    
    print "Cross-validated {0} score: {1}".format(scoring_metric, grid_searcher.best_score_)
    print "{0} features selected".format(len(top_features))
    print "Reduced to {0} PCA components".format(n_pca_components)
    ###################
    # Print the parameters used in the model selected from grid search
    print "Params: ", grid_searcher.best_params_ 
    ###################
    
    clf = grid_searcher.best_estimator_
    
    my_dataset = combine_to_dict(features_df=X_df, labels_df=y_df)
    ### Extract features and labels frouum dataset for local testing
    data = featureFormat(my_dataset, features_list, sort_keys = True)
    labels, features = targetFeatureSplit(data)
    
    test_classifier(clf, my_dataset, features_list)
    ### Dump your classifier, dataset, and features_list so 
    ### anyone can run/check your results.
    dump_classifier_and_data(clf, my_dataset, features_list)
