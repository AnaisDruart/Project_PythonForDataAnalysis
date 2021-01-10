# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:12:18 2021

@author: anais
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler



def cleaning(df_values,not_bool=False):
    all_columns = [
    'ID', 
    'Age', 
    'Gender', 
    'Education', 
    'Country',
    'Ethnicity',
    'Neuroticism',
    'Extraversion',
    'Openness to experience',
    'Agreeableness',
    'Conscientiousness',
    'Impulsiveness',
    'Sensation seeking',
    'Alcohol consumption',
    'Amphetamines consumption',
    'Amyl nitrite consumption',
    'Benzodiazepine consumption',
    'Caffeine consumption',
    'Cannabis consumption',
    'Chocolate consumption',
    'Cocaine consumption',
    'Crack consumption',
    'Ecstasy consumption',
    'Heroin consumption',
    'Ketamine consumption',
    'Legal highs consumption',
    'Lysergic acid diethylamide consumption',
    'Methadone consumption',
    'Magic mushrooms consumption',
    'Nicotine consumption',
    'Fictitious drug Semeron consumption',
    'Volatile substance abuse consumption'
    ]

    demographic_columns = [
        'Age', 
        'Gender', 
        'Education', 
        'Country',
        'Ethnicity',
    ]

    personality_columns = [
        'Neuroticism',
        'Extraversion',
        'Openness to experience',
        'Agreeableness',
        'Conscientiousness',
        'Impulsiveness',
        'Sensation seeking'
    ]

    drugs_columns = [
        'Alcohol consumption',
        'Amphetamines consumption',
        'Amyl nitrite consumption',
        'Benzodiazepine consumption',
        'Caffeine consumption',
        'Cannabis consumption',
        'Chocolate consumption',
        'Cocaine consumption',
        'Crack consumption',
        'Ecstasy consumption',
        'Heroin consumption',
        'Ketamine consumption',
        'Legal highs consumption',
        'Lysergic acid diethylamide consumption',
        'Methadone consumption',
        'Magic mushrooms consumption',
        'Nicotine consumption',
        'Fictitious drug Semeron consumption',
        'Volatile substance abuse consumption'
    ]
    
    data = pd.DataFrame(df_values, columns = all_columns)
    
    for i in drugs_columns:
        data[i] = data[i].map({'CL0': 0, 'CL1': 1, 'CL2': 2, 'CL3': 3, 'CL4': 4, 'CL5': 5, 'CL6': 6})
    
    if('Fictitious drug Semeron consumption' in drugs_columns):
        data = data[data['Fictitious drug Semeron consumption'] == 0]
        drugs_columns.remove('Fictitious drug Semeron consumption')
    
    age = ['18-24' if a <= -0.9 else 
       '25-34' if a >= -0.5 and a < 0 else 
       '35-44' if a > 0 and a < 1 else 
       '45-54' if a > 1 and a < 1.5 else 
       '55-64' if a > 1.5 and a < 2 else 
       '65+' 
       for a in data['Age']]

    gender = ['Female' if g > 0 else "Male" for g in data['Gender']]

    education = ['Left school before 16 years' if e <-2 else 
                 'Left school at 16 years' if e > -2 and e < -1.5 else 
                 'Left school at 17 years' if e > -1.5 and e < -1.4 else 
                 'Left school at 18 years' if e > -1.4 and e < -1 else 
                 'Some college or university, no certificate or degree' if e > -1 and e < -0.5 else 
                 'Professional certificate/ diploma' if e > -0.5 and e < 0 else 
                 'University degree' if e > 0 and e < 0.5 else 
                 'Masters degree' if e > 0.5 and e < 1.5 else 
                 'Doctorate degree' 
                 for e in data['Education']]

    country = ['United States' if c < -0.5 else 
               'New Zealand' if c > -0.5 and c < -0.4 else 
               'Other' if c > -0.4 and c < -0.2 else 
               'Australia' if c > -0.2 and c < 0 else 
               'Ireland' if c > 0 and c < 0.23 else 
               'Canada' if c > 0.23 and c < 0.9 else 
               'United Kingdom' 
               for c in data['Country']]

    ethnicity = ['Black' if e < -1 else 
                 'Asian' if e > -1 and e < -0.4 else 
                 'White' if e > -0.4 and e < -0.25 else 
                 'Mixed-White/Black' if e >= -0.25 and e < 0.11 else 
                 'Mixed-White/Asian' if e > 0.12 and e < 1 else 
                 'Mixed-Black/Asian' if e > 1.9 else 
                 'Other' 
                 for e in data['Ethnicity']]


    data['Age'] = age
    data['Gender'] = gender
    data['Education'] = education
    data['Country'] = country
    data['Ethnicity'] = ethnicity
    data.drop("ID", axis=1, inplace=True)
    
    for i in drugs_columns:
        data[i] = data[i].map({ 0 : 0,  1 : 0, 2 : 1, 3 : 1, 4 : 1, 5 : 1, 6 : 1})
    
    
    
    if not not_bool:
        data = data.values
    return data


def encoding(drug_column, df):
    drugs_columns = [
    'Alcohol consumption',
    'Amphetamines consumption',
    'Amyl nitrite consumption',
    'Benzodiazepine consumption',
    'Caffeine consumption',
    'Cannabis consumption',
    'Chocolate consumption',
    'Cocaine consumption',
    'Crack consumption',
    'Ecstasy consumption',
    'Heroin consumption',
    'Ketamine consumption',
    'Legal highs consumption',
    'Lysergic acid diethylamide consumption',
    'Methadone consumption',
    'Magic mushrooms consumption',
    'Nicotine consumption',
    'Fictitious drug Semeron consumption',
    'Volatile substance abuse consumption'
]
    if(drug_column in drugs_columns ):
        X, y = df.drop(drug_column, axis=1), df[drug_column]
        return X,y