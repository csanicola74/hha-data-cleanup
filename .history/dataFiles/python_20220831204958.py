import pandas as pd
import datetime as dt
import uuid
import numpy as np


# load in the hospital dataset A
hosA = pd.read_csv(
    'transformation/dataFiles/raw/113243405_StonyBrookUniversityHospital_standardcharges.csv')

# looking at the data frame, it is currently in WIDE format, we want to make it STACKED format
# so first lets get a name of the columns
columnNames = list(stonybrook)


# load in the hospital dataset B
hosB = pd.read_csv(
    'transformation/dataFiles/raw/113243405_StonyBrookUniversityHospital_standardcharges.csv')


# get a count of missing values in each column
df.isnull().sum()
