import pandas as pd
import datetime as dt
import uuid
import numpy as np


# load in the hospital dataset A
hosA = pd.read_csv(
    'transformation/dataFiles/raw/113243405_StonyBrookUniversityHospital_standardcharges.csv')


# load in the hospital dataset B
hosB = pd.read_csv(
    'transformation/dataFiles/raw/113243405_StonyBrookUniversityHospital_standardcharges.csv')
