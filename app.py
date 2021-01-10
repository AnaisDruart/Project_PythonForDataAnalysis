# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:44:51 2020

@author: anais
"""

# creation of the application instance (there could be many)
from flask import Flask
import pickle
import json
from flask import  request, jsonify
import numpy as np

app = Flask(__name__) # so flask knows where is the root path of the app
drugs_columns = [
        'Alcohol',
        'Amphetamines',
        'Amyl nitrite',
        'Benzodiazepine',
        'Caffeine',
        'Cannabis',
        'Chocolate',
        'Cocaine',
        'Crack',
        'Ecstasy',
        'Heroin',
        'Ketamine',
        'Legal highs',
        'Lysergic acid diethylamide',
        'Methadone',
        'Magic mushrooms',
        'Nicotine',
        'Volatile substance abuse'
    ]


# application instance is called `app`
# those routes are handled by the application instance 'app' (`app` may be imported from a different file or this code could be simply written in the same file after the previous code block)

# endpoint here is the root url '/'
# the decorator turns root_url function to a "route function"

@app.route('/fit/<drug_name>', methods=['POST'])
def fit(drug_name):
    
    if(drug_name in drugs_columns):
        filename = drug_name + " consumption"+ ".pkl"        
    else:
        filename =  "alcohol consumption" + ".pkl"
        #by default, the model used the best with the alcohol drug

    model = pickle.load(open(filename,'rb')) 
    #we load the model
    
    data_raw = request.get_json(force=True)
    data_input = np.array(data_raw['data_input'])
    prediction = model.predict(data_input)
    #we get the predictions
    
    pkl_filename = "predictions.pkl"
    with open(pkl_filename, 'wb') as f:
        pickle.dump(prediction, f)
    
    return ""

    

if __name__ == "__main__":
    app.run( port=5000,debug=True)