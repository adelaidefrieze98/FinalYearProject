## import dependencies 
import tensorflow as tf
import numpy as np 
import pandas as pd 

##loading data as a pandas dataframe 
data = pd.read_csv("C1S1Excel.csv", index_col=0)
##show first few rows of datset 
data.head()