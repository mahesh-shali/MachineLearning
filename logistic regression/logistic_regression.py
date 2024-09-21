# -*- coding: utf-8 -*-
"""Logistic regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S4XL0mLFS3QzNfexF0JLV5vl07K6WZLm
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
from matplotlib import pyplot as plt
# %matplotlib inline

df = pd.read_csv("insurance_data.csv")
df.head()

plt.scatter(df.age,df.bought_insurance,marker='+',color='red')

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.8)

X_test

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_train, y_train)

X_test

y_predicted = model.predict(X_test)

model.predict_proba(X_test)

model.score(X_test,y_test)

y_predicted

X_test

"""model.coef_ indicates value of m in y=m*x + b equation"""

model.coef_

"""model.intercept_ indicates value of b in y=m*x + b equation"""

model.intercept_

"""Lets defined sigmoid function now and do the math with hand"""

import math
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def prediction_function(age):
    z = 0.042 * age - 1.53 # 0.04150133 ~ 0.042 and -1.52726963 ~ -1.53
    y = sigmoid(z)
    return y

"""0.485 is less than 0.5 which means person with 35 age will not buy insurance"""

age = 35
prediction_function(age)

"""0.485 is more than 0.5 which means person with 43 will buy the insurance"""

age = 43
prediction_function(age)

"""# Exercise"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
from matplotlib import pyplot as plt
# %matplotlib inline

d = pd.read_csv("HR_comma_sep.csv")
d.head()

"""**Data exploration and visualization**"""

left = d[d.left==1]
left.shape

retained = d[d.left==0]
retained.shape

"""Average numbers for all columns"""

print(d.head())

d.groupby('left').mean(numeric_only=True)

"""Impact of salary on employee retention"""

pd.crosstab(df.salary,df.left).plot(kind='bar')

"""Department wise employee retention rate"""

pd.crosstab(df.Department,df.left).plot(kind='bar')

"""**From the data analysis so far we can conclude that we will use following variables as independant variables in our model**



1.   Satisfaction Level
2.   Average Monthly Hours
3.   Promotion Last 5 Years
4.   Salary



"""

subdf = df[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]
subdf.head()

"""Tackle salary dummy variable"""

salary_dummies = pd.get_dummies(subdf.salary, prefix="salary")

df_with_dummies = pd.concat([subdf,salary_dummies],axis='columns')

df_with_dummies.head()

df_with_dummies.drop('salary',axis='columns',inplace=True)
df_with_dummies.head()

X = df_with_dummies
X.head()

y = df.left

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.3)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_train, y_train)

model.predict(X_test)

"""**Accuracy of the model**"""

model.score(X_test,y_test)

"""# Logistic Regression: Multiclass Classification"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.datasets import load_digits
# %matplotlib inline
import matplotlib.pyplot as plt
digits = load_digits()

plt.gray()
for i in range(5):
    plt.matshow(digits.images[i])

dir(digits)

digits.data[0]

"""**Create and train logistic regression model**"""

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target, test_size=0.2)

model.fit(X_train, y_train)

"""**Measure accuracy of our model**"""

model.score(X_test, y_test)

model.predict(digits.data[0:5])

"""**Confusion Matrix**"""

y_predicted = model.predict(X_test)

from sklearn.metrics import confusion_matrix
import numpy as np
cm = confusion_matrix(y_test, y_predicted)
cm = cm.astype(np.int64)
cm

import seaborn as sn
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')