# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 05:07:10 2015
@author: fch

Library for shaping the data to be to used in creating fraud person-of-interest
(POI) prediction model.

This module provides data shaping functions shape data for use in building
POI prediction models as part of the Udacity Data Analyst Nanodegree Program.

Available functions include:
- features_split_pandas: Splits pandas dataframe into one features df and 
    one labels df.
- fill_zeros: Convert NaN and/or Inf/-Inf to zeros.
- fix_records: Fix out-of-sync records.
- remove_invalid_entries: Remove invalid rows/entries.
- combine_to_dict: Reformat and combine features and labels pandas dataframes
     to data_dict format for tester.py script.
"""

import numpy as np
import pandas as pd

def features_split_pandas(df, remove_zeros_rows=True):
    '''Splits pandas dataframe into one features df and one labels df.
    
    Splits pandas dataframe into one features df and one labels df. Optionally, 
    rows with only zeros for values can be removed in this step.
    
    Args:
        df: Pandas dataframe with Enron features and target labels.
        remove_zeros_rows: Boolean flag whether to remove any rows that contain
            only zeros for all values.
    Returns:
        One pandas dataframe of all features columns.
        One pandas dataframe of the target 'poi' labels being predicted.
    '''
    
    features = df.drop('poi', axis=1).astype(float)
    labels = df['poi']
    
    # Remove any rows of the features which absolute values sum up to zero from
    # labels first, then features.
    labels = labels[features.abs().sum(axis=1) != 0]
    features = features[features.abs().sum(axis=1) != 0]
    return features, labels
    

def fill_zeros(df, include_inf=False):
    '''Convert 'NaN', np.nan, and/or Inf/-Inf to zeros.
    
    Convert NaN and/or Inf/-Inf to zeros. This includes 'NaN' as a string or 
        as np.nan.
    
    Args:
        df: Pandas dataframe containing NaN and/or Inf/-Inf.
        include_inf: Boolean flag whether to include Inf/-Inf
        in the conversion.
    
    Returns:
        Pandas dataframe with 0's in the place of NaN and/or Inf/-Inf.
    '''
    df = df.replace('NaN', 0)
    if include_inf:
        df = df.replace([np.inf, -np.inf], 0)
    return df.apply(lambda x: x.fillna(0), axis=0)
    
def remove_invalid_entries(df, invalid_name='TOTAL'):
    '''Remove invalid records.
    
    Removes any rows with the names in the index of the pandas dataframe.
    
    Args:
        df: A pandas dataframe of records.
        invalid: A string or list of strings name(s) of the person(S) to be
        removed from the dataframe.
    
    Returns:
        Pandas dataframe with the row entry removed.
    '''
    
    return df.drop(invalid_name, axis=0)    
    
def fix_records(data_dict):
    '''Fix two out-of-sync records.    
    
    Two records were found to be out of sync with the financial records PDF
    form which the financial data was scraped from. This function overwrites
    these two records with their correct values.
    
    Args:
        data_dict: Dictionary with records of all people in the Enron dataset
            being examined.
    
    Returns:
        Dictionary with two records properly synced to their correct values.  
    '''
    data_dict['BELFER ROBERT'] = {'bonus': 'NaN',
                              'deferral_payments': 'NaN',
                              'deferred_income': -102500,
                              'director_fees': 102500,
                              'email_address': 'NaN',
                              'exercised_stock_options': 'NaN',
                              'expenses': 3285,
                              'from_messages': 'NaN',
                              'from_poi_to_this_person': 'NaN',
                              'from_this_person_to_poi': 'NaN',
                              'loan_advances': 'NaN',
                              'long_term_incentive': 'NaN',
                              'other': 'NaN',
                              'poi': False,
                              'restricted_stock': -44093,
                              'restricted_stock_deferred': 44093,
                              'salary': 'NaN',
                              'shared_receipt_with_poi': 'NaN',
                              'to_messages': 'NaN',
                              'total_payments': 3285,
                              'total_stock_value': 'NaN'}

    data_dict['BHATNAGAR SANJAY'] = {'bonus': 'NaN',
                                 'deferral_payments': 'NaN',
                                 'deferred_income': 'NaN',
                                 'director_fees': 'NaN',
                                 'email_address': 'sanjay.bhatnagar@enron.com',
                                 'exercised_stock_options': 15456290,
                                 'expenses': 137864,
                                 'from_messages': 29,
                                 'from_poi_to_this_person': 0,
                                 'from_this_person_to_poi': 1,
                                 'loan_advances': 'NaN',
                                 'long_term_incentive': 'NaN',
                                 'other': 'NaN',
                                 'poi': False,
                                 'restricted_stock': 2604490,
                                 'restricted_stock_deferred': -2604490,
                                 'salary': 'NaN',
                                 'shared_receipt_with_poi': 463,
                                 'to_messages': 523,
                                 'total_payments': 137864,
                                 'total_stock_value': 15456290} 
    return data_dict
    
def combine_to_dict(features_df=None, labels_df=None):
    '''Reformat and combine features and labels pandas dataframes to data_dict
        format for tester.py script.
    
    Reformat and combine features and labels pandas dataframes to data_dict
        format for testing.py script.
        
    Args:
        features_df: Pandas dataframe containing features being used to create
            the predictive models.
        labels_df: Pandas dataframe containing labels being predicted.

    Returns:
        Data_dict dictionary to be used in tester.py
    '''
    features_df.insert(0, 'poi', labels_df)
    
    data_dict = features_df.T.to_dict()
    del features_df
    return data_dict