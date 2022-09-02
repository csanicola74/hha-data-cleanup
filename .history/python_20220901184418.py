import pandas as pd
import datetime as dt
import uuid
import numpy as np


# load in the hospital dataset A
school_learn_mod = pd.read_csv(
    'data/School_Learning_Modalities.csv')

# get a count of the number of rows and columns
school_learn_mod.shape

# looking at the data frame, it is currently in WIDE format, we want to make it STACKED format
# so first lets get a name of the columns
columnNames = list(school_learn_mod)

# this is identify the key variables that we want to keep to designate what is the lowest unit of each row
idVars = columnNames[:8]
# these are the idential variables that we want to 'stack'
valueVars = columnNames[8:]

# transofmring with the melt function from a wide dataframe to a stacked dataframe
hosA_long = hosA.melt(id_vars=idVars, value_vars=valueVars)

# load in the hospital dataset B
hosB = pd.read_csv(
    'transformation/dataFiles/raw/113243405_StonyBrookUniversityHospital_standardcharges.csv')


# concat the two files since they have the same column names (e.g., variables)
hosAB_long = pd.concat([hosA_long, hosB])


# create a pivot table of hosAB that summarizes at least two of the columns
pd.pivot_table(hosAB_long, index=['Class', 'Div'])


# get a count of missing values in each column
df.isnull().sum()
