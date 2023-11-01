# Data Science Salary Estimator: Project Overview

* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job 
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model
* Built a client facing API using flask
* _Please note that this project was originally created by Ken Jee and replicated by myself as part of my Data Science learning journey_
* _I also want to emphasize that I did all of the code work on my own to get the most out of it and did some adjustments in favor of my coding style_

## Code and Resources used

**Python version**: 3.10 <br>
**Packages**: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle <br>
**Ken Jee's Project Walk-Through**: https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t <br>
**Original Project Github**: https://github.com/PlayingNumbers/ds_salary_proj <br>
**Scraper Github**: https://github.com/arapfaik/scraping-glassdoor-selenium <br>
**Scraper Article**: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905 <br>
**Flask Productionization**: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2
