# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:47:22 2023

@author: DarkPalad1n
"""

import pandas as pd
import re

df = pd.read_csv("ds_salary_data_raw.csv")

# Salary parsing
df["hourly"] = df["Salary Estimate"].apply(lambda x: 1 if "per hour" in x.lower() else 0)
df["employer_provided"] = df["Salary Estimate"].apply(lambda x: 1 if "employer provided salary:" in x.lower() else 0)

df = df[df["Salary Estimate"] != "-1"] # -1 in quotes due to Salary Estimate is currently a text field
salary = df["Salary Estimate"].apply(lambda x: x.split("(")[0]) # get rid of Est. in salary
minus_k_and_dollar_sign = salary.apply(lambda x: x.replace("K", "").replace("$", ""))

minus_hour = minus_k_and_dollar_sign.apply(lambda x: x.lower().replace("per hour", "").replace("employer provided salary:", ""))

# Split lower and upper salary values into separate columns and change type "str" to "int"
df["min_salary"] = minus_hour.apply(lambda x: int(x.split("-")[0]))
df["max_salary"] = minus_hour.apply(lambda x: int(x.split("-")[1]))
df["avg_salary"] = (df.min_salary + df.max_salary) / 2


# Company name text only
df["company_text"] = df.apply(lambda x: x["Company Name"] if x["Rating"] < 0 else x["Company Name"][:-3], axis = 1)


# State field (state the company's in)
df["job_state"] = df["Location"].apply(lambda x: x.split(",")[1])
df.job_state.value_counts()
df["same_state"] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)


# Age of company
df["age"] = df.Founded.apply(lambda x: x if x < 1 else 2023 - x)


# Job description parsing (technologies like Python etc.)
df["Python"] = df["Job Description"].apply(lambda x: 1 if "python" in x.lower() else 0) # lower ignores case sensitivity
df.Python.value_counts()

df["R"] = df["Job Description"].apply(lambda x: 1 if "r studio" in x.lower() or "r-studio" in x.lower() else 0)
df.R.value_counts()

df["Spark"] = df["Job Description"].apply(lambda x: 1 if "spark" in x.lower() else 0)
df.Spark.value_counts()

df["AWS"] = df["Job Description"].apply(lambda x: 1 if "aws" in x.lower() else 0)
df.AWS.value_counts()

df["Excel"] = df["Job Description"].apply(lambda x: 1 if "excel" in x.lower() else 0)
df.Excel.value_counts()

df["SQL"] = df["Job Description"].apply(lambda x: 1 if "sql" in x.lower() else 0)
df.SQL.value_counts()

df["SAS"] = df["Job Description"].apply(lambda x: 1 if "sas" in x.lower() else 0)
df.SAS.value_counts()

df["Keras"] = df["Job Description"].apply(lambda x: 1 if "keras" in x.lower() else 0)
df.Keras.value_counts()

df["Pytorch"] = df["Job Description"].apply(lambda x: 1 if "pytorch" in x.lower() else 0)
df.Pytorch.value_counts()

df["Scikit"] = df["Job Description"].apply(lambda x: 1 if "scikt" in x.lower() else 0)
df.Scikit.value_counts()

df["Tensor"] = df["Job Description"].apply(lambda x: 1 if "tensor" in x.lower() else 0)
df.Tensor.value_counts()

df["Hadoop"] = df["Job Description"].apply(lambda x: 1 if "hadoop" in x.lower() else 0)
df.Hadoop.value_counts()

df["Tableau"] = df["Job Description"].apply(lambda x: 1 if "tableau" in x.lower() else 0)
df.Tableau.value_counts()

df["BI"] = df["Job Description"].apply(lambda x: 1 if "bi" in x.lower() else 0)
df.BI.value_counts()

df["Flink"] = df["Job Description"].apply(lambda x: 1 if "flink" in x.lower() else 0)
df.Flink.value_counts()

df["Mongo"] = df["Job Description"].apply(lambda x: 1 if "mongo" in x.lower() else 0)
df.Mongo.value_counts()

df["Google_an"] = df["Job Description"].apply(lambda x: 1 if "google_an" in x.lower() else 0)
df.Google_an.value_counts()

# Regex
df["Degree"] = df["Job Description"].str.extract(r'(\bBachelor\b|\bMaster\b|\bPh\.D\b)')
df["Job Title Category"] = df["Job Title"].str.extract(r'(Data\sScientist|Data\sEngineer|Data\sAnalyst)')

# Get rid of column "index"
df.columns
df_out = df.drop(["index"], axis = 1)

# Export cleaned df to csv
df_out.to_csv("ds_salary_data_cleaned.csv", index = False)