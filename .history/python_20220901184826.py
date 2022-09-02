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
