## This script reads RPDR excel file, and outputs curated mediation info with PIDs and Dates
## Author Tafadzwa Chaunzwa 3.26.18 

import numpy as np
import pandas as pd
import os
#import SimpleITK as sitk
import csv
import sys
import time, glob

#Define Data File
File = 'KA71__103117112956902332_BWH_Dia.csv'
Directory = '/home/chintan/Desktop/RPDR/'
OpenFile = pd.read_csv(Directory+File)
print(OpenFile.shape) 

Dia = pd.Series.as_matrix(OpenFile.loc[:, 'Diagnosis_Name'])
Code = pd.Series.as_matrix(OpenFile.loc[:, 'Code'])
Dates = pd.Series.as_matrix(OpenFile.loc[:, 'Date'])
PID = pd.Series.as_matrix(OpenFile.loc[:, 'EMPI'])
MRN = pd.Series.as_matrix(OpenFile.loc[:, 'MRN'])

#Stroke Diagnosis
results_array = np.array([])
for i in range(0,len(Dia)):
	if Dia[i].find('Cerebral') != -1:
		#print PID[i], MRN[i], Dates[i], Dia[i], Code[i]
		
		results =  [PID[i], MRN[i], Dates[i], Dia[i], Code[i]]
		#results_array = np.appen(results_array, [results])
		results_array = np.concatenate((results_array, results), axis =0)

#save results
num_par = 5
results_array = results_array.reshape(len(results_array)/num_par, num_par)	

#Save File
np.savetxt('Cerebral.csv',results_array, fmt='%s', delimiter = ',')


