# -*- coding: utf-8 -*-
"""save_mdoel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OyQmtWjMXJdTeW4aG11YF1fd8HHp9Q1a
"""

import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv("homeprices.csv")
df.head()

model = linear_model.LinearRegression()
model.fit(df[['area']],df.price)

model.coef_

model.intercept_

model.predict([[5000]])

"""# Save Model To a File Using Python Pickle"""

import pickle

with open('model_pickle','wb') as file:
    pickle.dump(model,file)

"""# Load Saved Model"""

with open('model_pickle','rb') as file:
    mp = pickle.load(file)

mp.coef_

mp.intercept_

mp.predict([[5000]])

"""# Save Trained Model Using joblib"""

!pip install joblib --upgrade

import joblib

joblib.dump(model, 'model_joblib')

"""# Load Saved Model"""

mj = joblib.load('model_joblib')

mj.coef_

mj.intercept_

mj.predict([[5000]])

