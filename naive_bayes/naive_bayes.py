# -*- coding: utf-8 -*-
"""naive_bayes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/130D8kfu-I_ekYuspdUoaUpPnctg3ggq1

# Naive Bayes Tutorial Part 1: Predicting survival from titanic crash
"""

import pandas as pd

df = pd.read_csv("titanic.csv")
df.head()

df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns',inplace=True)
df.head()

inputs = df.drop('Survived',axis='columns')
target = df.Survived

dummies = pd.get_dummies(inputs.Sex)
dummies = dummies.astype(int)
dummies.head(3)

inputs = pd.concat([inputs,dummies],axis='columns')
inputs.head(3)

"""**I am dropping male column as well because of dummy variable trap theory. One column is enough to repressent male vs female**"""

inputs.drop(['Sex','male'],axis='columns',inplace=True)
inputs.head(3)

inputs.columns[inputs.isna().any()]

inputs.Age[:10]

inputs.Age = inputs.Age.fillna(inputs.Age.mean())
inputs.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.3)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()

model.fit(X_train,y_train)

model.score(X_test,y_test)

X_test[0:10]

y_test[0:10]

model.predict(X_test[0:10])

model.predict_proba(X_test[:10])

"""**Calculate the score using cross validation**"""

from sklearn.model_selection import cross_val_score
cross_val_score(GaussianNB(),X_train, y_train, cv=5)

"""# Email spam filter"""

import pandas as pd

df = pd.read_csv("spam.csv")
df.head()

df.groupby('Category').describe()

df['spam']=df['Category'].apply(lambda x: 1 if x=='spam' else 0)
df.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.Message,df.spam)

from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()
X_train_count = v.fit_transform(X_train.values)
X_train_count.toarray()[:2]

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X_train_count,y_train)

emails = [
    'Hey mohan, can we get together to watch footbal game tomorrow?',
    'Upto 20% discount on parking, exclusive offer just for you. Dont miss this reward!'
]
emails_count = v.transform(emails)
model.predict(emails_count)

X_test_count = v.transform(X_test)
model.score(X_test_count, y_test)

"""**Sklearn Pipeline**"""

from sklearn.pipeline import Pipeline
clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

clf.fit(X_train, y_train)

clf.score(X_test,y_test)

clf.predict(emails)

"""# Excercise"""

from sklearn import datasets
wine = datasets.load_wine()

dir(wine)

wine.data[0:2]

wine.feature_names

wine.target_names

wine.target[0:2]

import pandas as pd
df = pd.DataFrame(wine.data,columns=wine.feature_names)
df.head()

df['target'] = wine.target
df[50:70]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3, random_state=100)

from sklearn.naive_bayes import GaussianNB, MultinomialNB
model = GaussianNB()
model.fit(X_train,y_train)

model.score(X_test,y_test)

mn = MultinomialNB()
mn.fit(X_train,y_train)
mn.score(X_test,y_test)