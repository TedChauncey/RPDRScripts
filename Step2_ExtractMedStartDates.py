## This script reads a meds file (e.g for Statins.csv/Aspirin.csv), and outputs medication start date
## Author Tafadzwa Chaunzwa 3.31.18
## Make sure the dates are in the format YYYY-MM-DD 

import numpy as np
import pandas as pd
import os
import csv
import sys
import time, glob

File = 'Statins.csv'
Directory = '/home/chintan/Desktop/RPDR/'
OpenFile = pd.read_csv(Directory+File)
print(OpenFile.shape) 

# make sure these are all sorted before importing
Meds = pd.Series.as_matrix(OpenFile.loc[:, 'Medication'])
Dates = pd.Series.as_matrix(OpenFile.loc[:, 'Date'])
PID = pd.Series.as_matrix(OpenFile.loc[:, 'EMPI'])
MRN = pd.Series.as_matrix(OpenFile.loc[:, 'MRN'])


a = np.array([]) # where a is dummy variable for saving first instances
for i in range(0,len(PID)-1):
	if np.diff(PID)[i] != 0:
		first_instance = [PID[i+1].reshape(1,), MRN[i+1], Dates[i+1]]
		a = np.concatenate((a, first_instance), axis = 0)

params = 3 # number of returned parameters
a = a.reshape(len(a)/params, params)  
#include the first value of first patient
in_val = [PID[0].reshape(1,), MRN[0], Dates[0]]
in_val = np.asarray(in_val).reshape(1,params)

MedDates = np.concatenate((in_val, a), axis =0)

#Save MedStart dates
np.savetxt('MedStartDates.csv', MedDates , fmt='%s', delimiter = ',')
