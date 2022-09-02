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
school_learn_mod.columns = school_learn_mod.columns.str.replace(
    '[^A-Za-z0-9]+', '_')  # regex
list(school_learn_mod)

# replace all whitespace in column names with an underscore
school_learn_mod.columns = school_learn_mod.columns.str.replace(' ', '_')

# get list of column types
# want to see if strings are really strings, number are numbers, dates are dates, and boolean are booleans
school_learn_mod.dtypes

# determine if date is on weekday or weekend
school_learn_mod['Week'] = pd.to_datetime(school_learn_mod['Week'])
school_learn_mod['Week'] = school_learn_mod['Week'].dt.dayofweek

# 8. look for duplicate rows and remove duplicate rows
school_learn_mod.drop_duplicates(
    subset=None, keep='first', inplace=False, ignore_index=False)

# get a count of missing values in each column
school_learn_mod.isnull().sum()


school_learn_mod['modality_inperson'] = np.where(school_learn_mod["Learning_Modality"] == 'In Person', True, False)

# confirm tthe new column and that it is a boolean
school_learn_mod.dtypes

# save the clean Version to a csv file in cleanData
school_learn_mod.to_csv(
    'data/School_Learning_Modalities_Clean.csv')
