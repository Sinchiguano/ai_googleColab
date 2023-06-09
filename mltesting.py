# -*- coding: utf-8 -*-
"""Copy of classifierIris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tWcgLRJVkP6gAYEPccm2-KUkzM0N-b3t
"""

url='https://raw.githubusercontent.com/Sinchiguano/ai_googleColab/main/datasetUleamMl/IRIS.csv'
import pandas as pd
dataset=pd.read_csv(url)

"""Exploring the dataset"""

# dataset.head(10)

# dataset.shape

# dataset.describe()

# dataset.index

# dataset.columns

# dataset.head(10)

# dataset['species'].unique()

# dataset['species'].value_counts()

# dataset['target']=dataset['species']

# dataset['target']=dataset[dataset['target']=='Iris-setosa']=1 or dataset[dataset['target']=='Iris-versicolor']=2 or dataset[dataset['target']=='Iris-virginica']=3
tmp=list()
for label in dataset['species']:
  if  label == 'Iris-setosa':
    tmp.append(1)
  elif label=='Iris-versicolor':
    tmp.append(2)
  elif label=='Iris-virginica':
    tmp.append(3)

dataset['target']=tmp

# dataset.tail()

# dataset['target'][50:]

# dataset.shape

# dataset['target'].unique()

# dataset.groupby('species').count()

# dataset.groupby('species').size()

"""Plotting the dataset

Plotting a dataset is a great way to explore its distribution. Plotting the iris dataset can be done using matplotlib, a Python library for 2D plotting.
"""

import matplotlib.pyplot as plt
#array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], dtype=object)


#CREATE SOME FILTER IN ORDER TO ISOLATE SPECIES FROM EACH OTHER
setosaMask=dataset['species']=='Iris-setosa'
versicolorMask=dataset['species']=='Iris-versicolor'
virginicaMask=dataset['species']=='Iris-virginica'



setosa=dataset[setosaMask]
versicolor=dataset[versicolorMask]
virginica=dataset[virginicaMask]

print(setosa.shape)
print(versicolor.shape)
print(virginica.shape)
print(setosa.columns)

fig,ax=plt.subplots()
fig.set_size_inches(14,6)

ax.scatter(setosa['sepal_length'],setosa['sepal_width'],facecolor='blue',label='setosa')
ax.scatter(versicolor['sepal_length'],versicolor['sepal_width'],facecolor='red',label='versicolor')
ax.scatter(virginica['sepal_length'],virginica['sepal_width'],facecolor='green',label='virginica')

ax.set_xlabel('sepal length')
ax.set_ylabel('sepal width')
ax.grid()
ax.set_title('IRIS CLASSIFIER')
ax.legend()

fig,ax=plt.subplots()
fig.set_size_inches(12,6)

ax.scatter(setosa['petal_length'],setosa['petal_width'],facecolor='blue',label='setosa')
ax.scatter(versicolor['petal_length'],versicolor['petal_width'],facecolor='red',label='versicolor')
ax.scatter(virginica['petal_length'],virginica['petal_width'],facecolor='green',label='virginica')

ax.set_xlabel('petal length')
ax.set_ylabel('petal width')
ax.grid()
ax.set_title('IRIS CLASSIFIER')
ax.legend()
# plt.show()


# print('hi')

print('++++++++++++++++++++++++++++')
"""Performing classification

When you look at the petal measurements of the three species of iris shown in the plot above, what do you see? It’s pretty obvious to us humans that Iris-virginica has larger petals than Iris-versicolor and Iris-setosa. But computers cannot understand like we do. It needs some algorithm to do so. In order to achieve such a task, we need to implement an algorithm that is able to classify the iris flowers into their corresponding classes.
"""

from sklearn.model_selection import train_test_split
from sklearn import *

x=dataset.drop(['species','target'],axis=1)
print(x.head(3))

# x.info()

x=x.to_numpy()[:,(2,3)]
y=dataset['target']



# SPLITTING INTO TRAIN AND TEST
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.8,random_state=45)

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()
model.fit(x_train,y_train)
predictions=model.predict(x_test)

# predictions

# """Performance Measures

# Performance measures are used to evaluate the effectiveness of classifiers on different datasets with different characteristics. For classification problems, there are three main measures for evaluating the model, the precision(the accuracy of positive predictions or the number of most relevant values from retrieved values.), Recall(ratio of positive instances that are truly detected by the classifier), and confusion matrix.

# """

# from sklearn import metrics

# print('PRECISION, RECALL, CONFUSION MATRIX IN TESTING')
# #PRECISION RECALL SCORES
# print(metrics.classification_report(y_test, predictions))

# #CONFUSION MATRIX
# print('CONFUSION MATRIX ')
# print(metrics.confusion_matrix(y_test, predictions))

import pickle
filename='savedModel.pkl'
pickle.dump(model,open(filename, 'wb'))


# # load the model from disk
# loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, Y_test)
# print(result)

#https://machinelearningmastery.com/gentle-introduction-bag-words-model/
