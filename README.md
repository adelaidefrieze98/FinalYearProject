# FinalYearProject

This is a short explanation of what each file does. 

# dataToCSV

The optical data provided by Microsoft came in the form of .txt files. This program took the ~4000 files and converted them into .csv files one by one. .csv files are one of the forms possible to extract data from and into InfluxDB

# dataIntoInflux

Added columns and assigned types using pandas dataframe to the data in the .csv files. Set up and construction of various required variables to access InfluxDB database. Writing the data into the InfluxDB database. Looping through each .csv files.

#stationaritytest

Data is extracted from InfluxDB and tested for stationarity.

#modelTrainingActual

Non-anomalous data is split into validation, training and testing sets. Model trained with fine-tuned parameters, and trained on validation and training sets. The model then successfully predicts test sets. 

#modelTrainingActual-Anomaly and modelTrainingActual-Anomaly-Multivariate

Different attempts to predict anomalous data using single-variate and multi-variate data. Unfortunately, due to time constraints and resource limitations, anomaly was not predicted, but was fun to explore the different ways of using the data and the challenge. 
