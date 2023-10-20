# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 10:56:30 2023

@author: DarkPalad1n
"""

import glassdoor_webscraper as gs
import pandas as pd

#path = "C:/Users/seitz/Documents/ds_salary_project/chromedriver_win32/chromedriver"
#df = gs.get_jobs("data scientist", 15, False, path, 8)

df = pd.read_csv("ds_salary_data_cleaned.csv")
