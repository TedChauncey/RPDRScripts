## This script reads RPDR excel file, and outputs curated medication info with EMPIs, MRNs and Dates
## Author Tafadzwa Chaunzwa 3.26.18 
## Make sure the dates are in the format YYYY-MM-DD for proper date based sorting 

import numpy as np
import pandas as pd
import os
import csv
import sys
import time, glob

#Define Data File
File = 'RPDRSourceFile.csv'
Directory = '/home/chintan/Desktop/RPDR/'
OpenFile = pd.read_csv(Directory+File)
print(OpenFile.shape) 

Meds = pd.Series.as_matrix(OpenFile.loc[:, 'Medication'])
Dates = pd.Series.as_matrix(OpenFile.loc[:, 'Medication_Date'])
PID = pd.Series.as_matrix(OpenFile.loc[:, 'EMPI'])
MRN = pd.Series.as_matrix(OpenFile.loc[:, 'MRN'])


## Save respective Medication Data
## Aspirin
results_array = np.array([])
for i in range(0,len(Meds)):
	if Meds[i].find('Aspirin') != -1:
		results =  [PID[i], MRN[i], Dates[i], Meds[i]]
		results_array = np.concatenate((results_array, results), axis =0)

num_par = 4
results_array = results_array.reshape(len(results_array)/num_par, num_par)	

#create dictionary series
d = {'EMPI': results_array[:,0], 'MRN': results_array[:,1], 'Date': results_array[:,2], 'Medication': results_array[:,3]}
#create a DataFrame
df = pd.DataFrame(d)
# Sort data by MRN/EMPHI then Date
SortedMedData = df.sort_values(by = ['EMPI', 'Date'], ascending = [True, True])
#Save Aspirin File
np.savetxt('Aspirin.csv',SortedMedData, fmt='%s', delimiter = ',')

## Statins
results_array = np.array([])
for i in range(0,len(Meds)):
	if Meds[i].find('astatin') != -1:
		results =  [PID[i], MRN[i], Dates[i], Meds[i]]
		results_array = np.concatenate((results_array, results), axis =0)

num_par = 4
results_array = results_array.reshape(len(results_array)/num_par, num_par)	

d = {'EMPI': results_array[:,0], 'MRN': results_array[:,1], 'Date': results_array[:,2], 'Medication': results_array[:,3]}
df = pd.DataFrame(d)
SortedMedData = df.sort_values(by = ['EMPI', 'Date'], ascending = [True, True])

np.savetxt('Statins.csv',SortedMedData, fmt='%s', delimiter = ',')


## ARBS
results_array2 = np.array([])
for i in range(0,len(Meds)):
	if Meds[i].find('sartan') != -1:
		results =  [PID[i], MRN[i], Dates[i], Meds[i]]
		results_array2 = np.concatenate((results_array2, results), axis =0)

num_par = 4
results_array2 = results_array2.reshape(len(results_array2)/num_par, num_par)

d = {'EMPI': results_array2[:,0], 'MRN': results_array2[:,1], 'Date': results_array2[:,2], 'Medication': results_array2[:,3]}
df = pd.DataFrame(d)
SortedMedData2 = df.sort_values(by = ['EMPI', 'Date'], ascending = [True, True])	

np.savetxt('ARBs.csv',SortedMedData2, fmt='%s', delimiter = ',')


## BBs
results_array3 = np.array([])
for i in range(0,len(Meds)):
	if Meds[i].find('lol') != -1:
		results =  [PID[i], MRN[i], Dates[i], Meds[i]]
		results_array3 = np.concatenate((results_array3, results), axis =0)
		
num_par = 4
results_array3 = results_array3.reshape(len(results_array3)/num_par, num_par)	

d = {'EMPI': results_array3[:,0], 'MRN': results_array3[:,1], 'Date': results_array3[:,2], 'Medication': results_array3[:,3]}
df = pd.DataFrame(d)
SortedMedData3 = df.sort_values(by = ['EMPI', 'Date'], ascending = [True, True])	

np.savetxt('BetaBlockers.csv',SortedMedData3, fmt='%s', delimiter = ',')

##ACE Inhibitors
results_array = np.array([])
for i in range(0,len(Meds)):
	if Meds[i].find('pril') != -1 and Meds[i].find('prilosec') == -1: # make sure to exclude prilosec
		results =  [PID[i], MRN[i], Dates[i], Meds[i]]
		results_array = np.concatenate((results_array, results), axis =0)

num_par = 4
results_array = results_array.reshape(len(results_array)/num_par, num_par)	

d = {'EMPI': results_array[:,0], 'MRN': results_array[:,1], 'Date': results_array[:,2], 'Medication': results_array[:,3]}
#create a DataFrame
df = pd.DataFrame(d)

SortedMedData = df.sort_values(by = ['EMPI', 'Date'], ascending = [True, True])
np.savetxt('ACEi.csv',SortedMedData, fmt='%s', delimiter = ',')


