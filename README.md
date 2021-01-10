# Project_PythonForDataAnalysis

## Dataset : Drug consumption (quantified) Data Set

The dataset contains records for 1885 respondents. For each respondent 12 attributes are known: 
* personality measurements which include NEO-FFI-R
  * neuroticism 
  * extraversion
  * openness to experience 
  * agreeableness
  * conscientiousness
* BIS-11 (impulsivity) 
* impss (sensation seeking) 
* level of education 
* age
* gender 
* country of residence 
* ethnicity 

All input attributes were originally categorical and were quantified.
In addition, participants were questioned concerning their use of 18 legal and illegal drugs  : 
* alcohol
* amphetamines 
* amyl nitrite
* benzodiazepine
* cannabis 
* chocolate 
* cocaine 
* caffeine 
* crack 
* ecstasy 
* heroin 
* ketamine
* legal highs 
* LSD 
* methadone 
* mushrooms 
* nicotine 
* volatile substance abuse 
* Semeron

For each drug they had to select one of the following answers: 
* Never used
* Used over a decade ago 
* Used in the last decade
* Used in the last year
* Used in the last month
* Used in the week
* Used in the last day

## Problem

#### We have 12 attributes evaluated for each person, and a very large variety of drug (from common stimulants like chocolate and coffee, to strong drugs like LSD and heroin)
#### We want to produce a model able to predict if a person could be a drug consumer, for each type of drug

## Main Steps :

* #### Exploratory data analysis (EDA) of the dataset
* #### Model creation, comparison and selection
* #### Transformation of the model to an api

## Short conclusion :

I tested 5 models : Logistic Regression, Neural Network, Stochastic Gradient descent, K-NN and Decision Tree. I stocked which model was the most efficient with which drug, and the API is responding accordingly.
I'm pretty happy about my results, since i got an accuracy from 75% to 99.3% with each drug.
Please go check the Jupyter Notebook for more information ! :)

## Documents :

* The jupyter notebook, where the big part of the code is, is https://github.com/Anasarasa/Project_PythonForDataAnalysis/blob/main/Final_Project_Python.ipynb
* Its html version is https://github.com/Anasarasa/Project_PythonForDataAnalysis/blob/main/Final_Project_Python.html
* The power point (in pdf format) were i explain everything about the problem and my way of resolving it is https://github.com/Anasarasa/Project_PythonForDataAnalysis/blob/main/Python_for_data_analysis_DRUG_CONSUMPTION.pdf
* I made a script to clean more easily the dataset obtained here : https://github.com/Anasarasa/Project_PythonForDataAnalysis/blob/main/cleaning_dataset.py
* Finally, the Flask API is there : https://github.com/Anasarasa/Project_PythonForDataAnalysis/blob/main/app.py
