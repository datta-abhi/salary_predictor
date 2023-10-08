import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('Data/salary_data.csv')

# Create and fit a linear regression model
X= df[['YearsExperience']]
y = df['Salary']
lr = LinearRegression()

lr.fit(X,y)

# Save the model to a pickle file
with open('linear_regression_model.pkl', 'wb') as file:
    pickle.dump(lr, file)