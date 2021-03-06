# -*- coding: utf-8 -*-
"""Copy_of_simple_linear_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qq9sJVANiPCN0BeJ5Jn9OI8WsmGqYGXM

# Simple Linear Regression

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset=pd.read_csv("Salary_Data.csv")
X=dataset.iloc[ : , :-1].values
Y=dataset.iloc[ : ,-1].values

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

"""## Training the Simple Linear Regression model on the Training set"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

"""## Predicting the Test set results"""

Y_pred=regressor.predict(X_test)

"""## Visualising the Training set results"""

plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary vs Experience(Training Set)')
plt.xlabel('Years Of Experience')
plt.ylabel('Salary')
plt.show()

"""## Visualising the Test set results"""

plt.scatter(X_test,Y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary vs Experience(Test Set)')
plt.xlabel('Years Of Experience')
plt.ylabel('Salary')
plt.show()

from sklearn.metrics import r2_score
print(r2_score(regressor.predict(X),Y))

"""**Determining the salary of an employee with 12 years of experience**"""

print(regressor.predict([[12]]))

"""**Determining the equation of line for our simple linear regression model and hence determining the coefficient b1 and the intercept b0**"""

print(regressor.coef_)
print(regressor.intercept_)