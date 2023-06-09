#!/usr/bin/env python
# coding: utf-8

# # Introduction

# The National Longitudinal Survey of Youth 1997-2011 dataset is one of the most important databases available to social scientists working with US data. 
# 
# It allows scientists to look at the determinants of earnings as well as educational attainment and has incredible relevance for government policy. It can also shed light on politically sensitive issues like how different educational attainment and salaries are for people of different ethnicity, sex, and other factors. When we have a better understanding how these variables affect education and earnings we can also formulate more suitable government policies. 
# 
# <center><img src=https://i.imgur.com/cxBpQ3I.png height=400></center>
# 

# ### Upgrade Plotly

# In[1]:


get_ipython().run_line_magic('pip', 'install --upgrade plotly')


# ###  Import Statements
# 

# In[3]:


import pandas as pd
import numpy as np

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# ## Notebook Presentation

# In[4]:


pd.options.display.float_format = '{:,.2f}'.format


# # Load the Data
# 
# 

# In[10]:


df_data = pd.read_csv('NLSY97_subset.csv')


# ### Understand the Dataset
# 
# Have a look at the file entitled `NLSY97_Variable_Names_and_Descriptions.csv`. 
# 
# ---------------------------
# 
#     :Key Variables:  
#       1. S           Years of schooling (highest grade completed as of 2011)
#       2. EXP         Total out-of-school work experience (years) as of the 2011 interview.
#       3. EARNINGS    Current hourly earnings in $ reported at the 2011 interview

# # Preliminary Data Exploration 🔎
# 
# **Challenge**
# 
# * What is the shape of `df_data`? 
# * How many rows and columns does it have?
# * What are the column names?
# * Are there any NaN values or duplicates?

# In[6]:


import pandas as pd

# Load the data from the CSV file
df_data = pd.read_csv("NLSY97_Variable_Names_and_Descriptions.csv")

# Check the shape of the DataFrame
shape = df_data.shape
print("Shape of df_data:", shape)

# Get the number of rows and columns
num_rows = shape[0]
num_cols = shape[1]
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)

# Get the column names
column_names = df_data.columns.tolist()
print("Column names:", column_names)

# Check for NaN values
has_nan_values = df_data.isnull().values.any()
print("Has NaN values:", has_nan_values)

# Check for duplicates
has_duplicates = df_data.duplicated().any()
print("Has duplicates:", has_duplicates)


# ## Data Cleaning - Check for Missing Values and Duplicates
# 
# Find and remove any duplicate rows.

# In[7]:


# Find and remove duplicate rows
df_data.drop_duplicates(inplace=True)

# Verify if duplicates have been removed
has_duplicates = df_data.duplicated().any()
print("Has duplicates:", has_duplicates)


# ## Descriptive Statistics

# In[8]:


# Compute descriptive statistics
statistics = df_data.describe()

# Print the statistics
print(statistics)


# ## Visualise the Features

# In[11]:


import seaborn as sns

# Create a histogram of the 'S' column
sns.histplot(data=df_data, x='S', bins=20)
plt.xlabel('Years of Schooling')
plt.ylabel('Frequency')
plt.title('Distribution of Years of Schooling')
plt.show()

# Create a scatter plot of 'EXP' vs 'EARNINGS'
sns.scatterplot(data=df_data, x='EXP', y='EARNINGS')
plt.xlabel('Years of Experience')
plt.ylabel('Earnings')
plt.title('Scatter Plot of Experience vs Earnings')
plt.show()


# # Split Training & Test Dataset
# 
# We *can't* use all the entries in our dataset to train our model. Keep 20% of the data for later as a testing dataset (out-of-sample data).  

# In[12]:


from sklearn.model_selection import train_test_split

# Separate the features (X) from the target variable (y)
X = df_data.drop('EARNINGS', axis=1)
y = df_data['EARNINGS']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# # Simple Linear Regression
# 
# Only use the years of schooling to predict earnings. Use sklearn to run the regression on the training dataset. How high is the r-squared for the regression on the training data? 

# In[13]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Prepare the training data
X_train = df_data[['S']]
y_train = df_data['EARNINGS']

# Create and fit the linear regression model
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

# Predict the target variable for the training data
y_train_pred = regression_model.predict(X_train)

# Calculate the R-squared value for the training data
r2_train = r2_score(y_train, y_train_pred)
print("R-squared (Training):", r2_train)


# ### Evaluate the Coefficients of the Model
# 
# Here we do a sense check on our regression coefficients. The first thing to look for is if the coefficients have the expected sign (positive or negative). 
# 
# Interpret the regression. How many extra dollars can one expect to earn for an additional year of schooling?

# In[14]:


# Get the coefficient for 'Years of Schooling'
coefficient = regression_model.coef_[0]

# Interpret the coefficient
print("For an additional year of schooling, one can expect to earn approximately $", coefficient, " more.")


# ### Analyse the Estimated Values & Regression Residuals
# 
# How good our regression is also depends on the residuals - the difference between the model's predictions ( 𝑦̂ 𝑖 ) and the true values ( 𝑦𝑖 ) inside y_train. Do you see any patterns in the distribution of the residuals?

# In[15]:


import numpy as np

# Calculate the residuals
residuals = y_train - y_train_pred

# Plot a histogram of the residuals
plt.hist(residuals, bins=20)
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Distribution of Residuals')
plt.show()

# Plot a scatter plot of the predicted values vs. residuals
plt.scatter(y_train_pred, residuals)
plt.xlabel('Predicted Earnings')
plt.ylabel('Residuals')
plt.title('Scatter Plot of Predicted Earnings vs. Residuals')
plt.show()


# # Multivariable Regression
# 
# Now use both years of schooling and the years work experience to predict earnings. How high is the r-squared for the regression on the training data? 

# In[16]:


# Prepare the training data
X_train = df_data[['S', 'EXP']]
y_train = df_data['EARNINGS']

# Create and fit the linear regression model
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

# Predict the target variable for the training data
y_train_pred = regression_model.predict(X_train)

# Calculate the R-squared value for the training data
r2_train = r2_score(y_train, y_train_pred)
print("R-squared (Training):", r2_train)


# ### Evaluate the Coefficients of the Model

# In[17]:


# Get the coefficients and intercept of the model
coefficients = regression_model.coef_
intercept = regression_model.intercept_

# Print the coefficients and intercept
print("Intercept:", intercept)
print("Coefficient for Years of Schooling (S):", coefficients[0])
print("Coefficient for Years of Work Experience (EXP):", coefficients[1])


# ### Analyse the Estimated Values & Regression Residuals

# In[18]:


# Predict the target variable for the training data
y_train_pred = regression_model.predict(X_train)

# Calculate the residuals
residuals = y_train - y_train_pred

# Create a DataFrame to compare actual values, estimated values, and residuals
comparison_df = pd.DataFrame({'Actual Earnings': y_train, 'Estimated Earnings': y_train_pred, 'Residuals': residuals})

# Print the first few rows of the DataFrame
print(comparison_df.head())

# Plot a scatter plot of the actual values vs. estimated values
plt.scatter(y_train, y_train_pred)
plt.xlabel('Actual Earnings')
plt.ylabel('Estimated Earnings')
plt.title('Scatter Plot of Actual Earnings vs. Estimated Earnings')
plt.show()

# Plot a histogram of the residuals
plt.hist(residuals, bins=20)
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Distribution of Residuals')
plt.show()


# # Use Your Model to Make a Prediction
# 
# How much can someone with a bachelors degree (12 + 4) years of schooling and 5 years work experience expect to earn in 2011?

# In[19]:


# Prepare the input data for prediction
years_of_schooling = 12 + 4  # Bachelor's degree (12 years) + 4 additional years
years_of_work_experience = 5

# Predict the earnings using the regression model
predicted_earnings = regression_model.predict([[years_of_schooling, years_of_work_experience]])

print("Estimated earnings for someone with a bachelor's degree and 5 years of work experience in 2011: $", predicted_earnings[0])


# # Experiment and Investigate Further
# 
# Which other features could you consider adding to further improve the regression to better predict earnings? 

# To further improve the regression model and better predict earnings, you can consider adding additional relevant features that may have an impact on earnings. Here are some potential features you could consider:
# 
# 1. Gender: The gender of an individual may have an influence on earnings due to potential gender-based wage gaps or differences in occupational choices.
# 
# 2. Age: Age can be an important factor as earnings tend to vary with different stages of a person's career.
# 
# 3. Household Income: The overall household income may impact individual earnings, as it reflects the economic resources available within the household.
# 
# 4. Geographic Location: Considering factors such as the region, city, or urban/rural classification can account for variations in cost of living, job opportunities, and wage levels.
# 
# 5. Occupation: The type of occupation can significantly affect earnings, as different professions have different salary structures.
# 
# 6. Industry: The industry in which an individual works can also impact earnings, as certain industries tend to offer higher salaries or have more lucrative opportunities.
# 
# 7. Education Level: In addition to years of schooling, considering the specific education level attained (e.g., high school diploma, bachelor's degree, advanced degree) may provide more precise information about the impact of education on earnings.
# 
# 8. Marital Status: Marital status can affect earnings through factors such as dual-income households or potential differences in job opportunities for married individuals.
# 
# 9. Employment Sector: Distinguishing between the public sector, private sector, and non-profit sector may capture variations in earnings associated with different employment sectors.
# 
# 10. Additional Skills or Certifications: Including information about specific skills or certifications that individuals possess can provide insights into their earning potential.
# 
# It's important to note that the selection of additional features should be guided by domain knowledge, data availability, and the specific context in which the regression model is being applied. Adding more relevant features can help capture additional factors that influence earnings and potentially improve the model's predictive performance.
