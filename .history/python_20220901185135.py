import pandas as pd
import datetime as dt
import uuid
import numpy as np


# load in the hospital dataset A
school_learn_mod = pd.read_csv(
    'data/School_Learning_Modalities.csv')

# get a count of the number of rows and columns
school_learn_mod.shape

# list columns
list(school_learn_mod)

############## CLEANNING THE DATA ##############

# remove all special characters and whitespace ' ' from column names
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')  # regex
list(df)

# replace all whitespace in column names with an underscore
df.columns = df.columns.str.replace(' ', '_')


# get list of column types
# want to see if strings are really strings, number are numbers, dates are dates, and boolean are booleans
df.dtypes

# create a list of columns that are strings, and save as strings
strings = df.select_dtypes(include=['object']).columns
# create a list of columns that are numbers, and save as numbers
numbers = df.select_dtypes(include=['int64', 'float64']).columns
# create a list of columns that are dates, and save as dates
dates = df.select_dtypes(include=['datetime64[ns]']).columns
# create a list of columns that are booleans, and save as booleans
booleans = df.select_dtypes(include=['bool']).columns
# create a list of columns that are objects, and save as objects
objects = df.select_dtypes(include=['object']).columns


# dealing with dates
# convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])
# convert date column to datetime format like this: '%Y-%m-%d'
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
# convert date column to datetime format like this: '%Y_%M_%D'
df['date'] = pd.to_datetime(df['date'], format='%Y_%M_%D')
# convert date to quarter format
df['date'] = df['date'].dt.quarter
# convert date to year format
df['date'] = df['date'].dt.year
# determine if date is on weekday or weekend
df['date'] = df['date'].dt.dayofweek


# get a count of missing values in each column
df.isnull().sum()

# save the clean Version to a csv file in cleanData
df.to_csv('/Users/hantswilliams/Documents/development/python_projects/hospitalPriceline/cleanData/mountSinai_clean.csv')
