# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 06:19:00 2015

@author: fch

Library for creating features to be used in creating fraud person-of-interest
(POI) prediction model.

This module provides feature creation functions to create features for use
in building POI prediction models as part of the Udacity Data Analyst
Nanodegree Program.

Available functions include:
- top_importances: Finds the top N importances using the ExtraTreesClassifier.
- add_totals: Creates totals features for the Enron dataset.
- add_financial_ratios: Add financial ratios features to Enron dataset.
- add_email_ratios: Add email ratios features to Enron dataset.
- add_squares: Add squared values as feature columns.
-

"""
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd



def top_importances(features_df=None, labels_df=None, top_N=10):
    ''' Finds the top N importances using the ExtraTreesClassifier.
        
    Finds the top N importances of a dataframe of features and a dataframe
        of labels using the ExtraTreesClassifier.
    
    Args:
        features_df: Pandas dataframe of features used to predict.
        labels_df: Pandas dataframe of labels to be predicted.
        top_N: interger value of the top N most importance features to return.
    Returns:
        Pandas dataframe containing the top N importances and their 
        importance scores.
    
    '''
    reducer = ExtraTreesClassifier(n_estimators=2000, bootstrap=False,
                                   oob_score=False, max_features=.10,
                                   min_samples_split=10, min_samples_leaf=2,
                                   criterion='gini')

    reducer.fit(features_df, labels_df)
    scores = pd.DataFrame(reducer.feature_importances_,
                          index=features_df.columns)
    scores.columns = ['Importances']
    scores = scores.sort(['Importances'], ascending=False)
    return scores[0:top_N]
    
def add_totals(df, email_data=True, financial_data=True):
    '''Creates totals features for the Enron dataset.
    
    Args:
        df: Pandas dataframe with Enron features to be aggregated.
        email_data: Boolean flag whether to create email totals.
        financial_data: Boolean flag whether to create financial totals.
    Returns:
        Pandas dataframe with aggregate statistics as a new column.
    '''
    
    if email_data:
        df['total_poi_interaction'] = df['shared_receipt_with_poi'] + \
                                      df['from_this_person_to_poi'] + \
                                      df['from_poi_to_this_person']
    if financial_data:
        df['total_compensation'] = df['total_payments'] + \
                                   df['total_stock_value']

    return df
    
def add_financial_ratios(df, to_payment=False, to_stock=False, to_total=True):
    '''Add financial ratios features to Enron dataset.
    
    Adds financial ratios data to dataset. This can include with each payments/
    stock section, and/or each sub-piece in relation to the aggregate.
    
    Args:
        df: Pandas dataframe with Enron data.
        to_payment: Boolean flag whether to create ratio data for each portion
            of payment data in relation to the payment total.
        to_stock: Boolean flag whether to create ratio data for each portion
            of stock data in relation to the stock total.
        to_total: Boolean flag whether to create ratio data for each portion
            of payment and stock data in relation to the overall total.
    Return:
        Pandas dataframe with financial ratios columns added.
    '''
    
    payment_comp = ['salary', 'deferral_payments','bonus', 'expenses',
                    'loan_advances', 'other', 'director_fees',
                    'deferred_income', 'long_term_incentive']

    stock_comp = ['exercised_stock_options', 'restricted_stock',
                  'restricted_stock_deferred']
    
    
    if to_total:
        all_comp = payment_comp + stock_comp 
        try:
            df['total_compensations']
        except KeyError:
            df = add_totals(df, email_data=False, financial_data=True)
        
        for each in all_comp:
            df['{0}_{1}_ratio'.format(each, 'total_compensation')] = \
            df[each]/df['total_compensation']
    
    if to_payment:
        for each in payment_comp:
            df['{0}_{1}_ratio'.format(each, 'total_pay')] = \
            df[each]/df['total_payments']
            
    if to_stock:
        for each in stock_comp:
            df['{0}_{1}_ratio'.format(each, 'total_stock')] = \
            df[each]/df['total_stock_value']
            
    return df
    
def add_email_ratios(df, to_message=True, from_messages=True,
                     to_total=False, active_ratios=True):
    '''Add email ratios features to Enron dataset.
    
    Adds email ratios data to dataset. This can include with each to/from 
        messages section, and/or each sub-piece in relation to the aggregate.
    
    Args:
        df: Pandas dataframe with Enron data.
        to_payment: Boolean flag whether to create ratio data for each portion
            'to messages' data in relation to the email total.
        to_stock: Boolean flag whether to create ratio data for each portion
            'from messages' in relation to the email total.
        to_total: Boolean flag whether to create ratio data for each 'to/from
            messages' data in relation to the overall total.
        active_ratios: Boolean flag whether to create ratio data for each
        'to/from messages' data in relation to the overall poi total.
        
    Return:
        Pandas dataframe with email ratios columns added.
    '''

    if to_total:
        email_comp = ['shared_receipt_with_poi', 'from_this_person_to_poi', 
                  'from_poi_to_this_person' ]        
        try:
            df['total_poi_interaction']
        except KeyError:
            df = add_totals(df, email_data=True, financial_data=False)
        
        for each in email_comp:
            df['{0}_{1}_ratio'.format(each, 'total_poi_int')] = \
            df[each]/df['total_poi_interaction']
            
    if active_ratios:
        df['total_active_poi_interaction'] = \
            df['from_this_person_to_poi'] + df['from_poi_to_this_person'] 
            
        df['from_poi_total_active_poi_ratio'] = \
            df['from_poi_to_this_person']/df['total_active_poi_interaction']
            
        df['to_poi_total_active_poi_ratio'] = \
            df['from_this_person_to_poi']/df['total_active_poi_interaction']
    
    if to_message:
        df['to_messages_to_poi_ratio'] = \
            df['from_this_person_to_poi']/df['to_messages']
    
    if from_messages:
        df['from_messages_from_poi_ratio'] = \
            df['from_poi_to_this_person']/df['from_messages']
            
        df['shared_poi_from_messages_ratio'] = \
            df['shared_receipt_with_poi']/df['from_messages']
    
    return df
    
    
def add_squares(df, square_financial=True, square_email=False):
    '''Add squared values as feature columns.
    
    Add squared values as features to the Enron dataset.
    
    Args:
        df: Pandas dataframe with Enron data.
        square_financial: Boolean flag whether to add squared financial 
            features.
        square_email: Boolean flag whether to add squared email features.
        
    Returns:
        Pandas dataframe with squared feature columns added.
    '''
    
    if square_email:
        email_comp = ['shared_receipt_with_poi', 'from_this_person_to_poi',
                      'from_poi_to_this_person' ]
        for each in email_comp:
            df['{0}_squared'.format(each)] = df[each]**2

    if square_financial:
        payment_comp = ['salary', 'deferral_payments','bonus', 'expenses',
                        'loan_advances', 'other', 'director_fees', 
                        'deferred_income', 'long_term_incentive']
        stock_comp = ['exercised_stock_options', 'restricted_stock',
                      'restricted_stock_deferred']
        all_comp = payment_comp + stock_comp
        
        for each in all_comp:
            df['{0}_squared'.format(each)] = df[each]**2
    
    return df
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    