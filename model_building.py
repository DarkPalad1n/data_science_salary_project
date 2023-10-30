# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:00:20 2023

@author: DarkPalad1n
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/seitz/Documents/ds_salary_project/ds_salary_data_cleaned_eda.csv")

# Choose relevant columns
df_model = df[["avg_salary", "Rating", "Size", "Type of ownership", "Industry", "Sector",
             "Revenue", "number_competitors", "hourly", "employer_provided",
             "job_state", "same_state", "age", "Python", "Spark", "AWS", "Excel",
             "job_description_simplified", "seniority", "desc_len"]]


# Get dummy data
df_dum = pd.get_dummies(df_model)


# Train test split
from sklearn.model_selection import train_test_split

X = df_dum.drop("avg_salary", axis = 1) # Independant variable X
y = df_dum.avg_salary.values # Dependet variable y saved as array

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42) # 20 % of the data is used for testing and 80 % for training


# Multiple linear regression
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y, X_sm)
results = model.fit()

print(results.summary()) # Shows results on console

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm, X_train, y_train, scoring = "neg_mean_absolute_error", cv = 3)) # Prints results in separate variable


# Lasso regression
lm_l = Lasso()
lm_l.fit(X_train, y_train)
np.mean(cross_val_score(lm_l, X_train, y_train, scoring = "neg_mean_absolute_error", cv = 3))

alpha = []
error = []

for i in range(1, 100):
    alpha.append(i / 100)
    lml = Lasso(alpha = (i / 100))
    error.append(np.mean(cross_val_score(lm_l, X_train, y_train, scoring = "neg_mean_absolute_error", cv = 3)))
    
plt.plot(alpha, error)

err = list(zip(alpha, error))
df_err = pd.DataFrame(err, columns = ["alpha", "error"])
df_err[df_err.error == max(df_err.error)]


# Random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

np.mean(cross_val_score(rf, X_train, y_train, scoring = "neg_mean_absolute_error", cv = 3))


# Tune models GridSearchCV
from sklearn.model_selection import GridSearchCV
parameters = {"n_estimators": range(10, 100, 10), "criterion":("mse", "mae"), "max_features":("auto", "sqrt", "log2")}

gs = GridSearchCV(rf, parameters, scoring = "neg_mean_absolute_error", cv = 3)
gs.fit(X_train, y_train)

gs.best_score_ # Run this cell as single call
gs.best_estimator_ # Run this cell as single call


# Test ensambles
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test) # As rf resulted as best estimator

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, tpred_lm)
mean_absolute_error(y_test, tpred_lml)
mean_absolute_error(y_test, tpred_rf)

mean_absolute_error(y_test, (tpred_lm + tpred_rf) / 2)

import pickle
pickl = {"model": gs.best_estimator_}
pickle.dump(pickl, open("model_file" + ".p", "wb"))

file_name = "model_file.p"
with open(file_name, "rb") as pickled:
    data = pickle.load(pickled)
    model = data["model"]
    
model.predict(X_test.iloc[1, :].values.reshape(1, -1))

list(X_test.iloc[1, :].values)