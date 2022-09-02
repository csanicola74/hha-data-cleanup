import pandas as pd
import datetime as dt
import uuid
import numpy as np


# load in the hospital dataset A
hosA = pd.read_csv(
    'transformation/dataFiles/raw/113243405_StonyBrookUniversityHospital_standardcharges.csv')

# looking at the data frame, it is currently in WIDE format, we want to make it STACKED format
# so first lets get a name of the columns
columnNames = list(hosA)

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
combined = pd.concat([hosA_long, hosB])


# get a count of missing values in each column
df.isnull().sum()
