## This script reads RPDR excel file, and outputs curated medication info with PIDs and Dates
## Author Tafadzwa Chaunzwa 3.26.18 

import numpy as np
import pandas as pd
import os
#import SimpleITK as sitk
import csv
import sys
import time, glob

#Define Data File
File = 'KA71__103117112956902332_BWH_Med.csv'
Directory = '/home/chintan/Desktop/RPDR/'
OpenFile = pd.read_csv(Directory+File)
print(OpenFile.shape) 

Meds = pd.Series.as_matrix(OpenFile.loc[:, 'Medication'])
Dates = pd.Series.as_matrix(OpenFile.loc[:, 'Medication_Date'])
PID = pd.Series.as_matrix(OpenFile.loc[:, 'EMPI'])
MRN = pd.Series.as_matrix(OpenFile.loc[:, 'MRN'])

#Aspirin File

results_array = np.array([])
for i in range(0,len(Meds)):
	if Meds[i].find('Aspirin') != -1:
		#print PID[i], MRN[i], Dates[i], Meds[i]
		results =  [PID[i], MRN[i], Dates[i], Meds[i]]
		#results_array = np.appen(results_array, [results])
		results_array = np.concatenate((results_array, results), axis =0)

#save results
num_par = 4
results_array = results_array.reshape(len(results_array)/num_par, num_par)	

#Save Aspirin File
np.savetxt('Aspirin.csv',results_array, fmt='%s', delimiter = ',')


# Statins
results_array = np.array([])
for i in range(0,len(Meds)):
	if Meds[i].find('astatin') != -1:
		#print PID[i], MRN[i], Dates[i], Meds[i]
		results =  [PID[i], MRN[i], Dates[i], Meds[i]]
		#results_array = np.appen(results_array, [results])
		results_array = np.concatenate((results_array, results), axis =0)

#save results
num_par = 4
results_array = results_array.reshape(len(results_array)/num_par, num_par)	

#Save Aspirin File
np.savetxt('Statins.csv',results_array, fmt='%s', delimiter = ',')



## Heparin
results_array2 = np.array([])
for i in range(0,len(Meds)):
	if Meds[i].find('heparin') != -1:
		#print PID[i], MRN[i], Dates[i], Meds[i]
		results =  [PID[i], MRN[i], Dates[i], Meds[i]]
		#results_array = np.appen(results_array, [results])
		results_array2 = np.concatenate((results_array2, results), axis =0)

#save results
num_par = 4
results_array2 = results_array2.reshape(len(results_array2)/num_par, num_par)	

np.savetxt('heparin.csv',results_array2, fmt='%s', delimiter = ',')


# Create Simvastatin file

results_array3 = np.array([])
for i in range(0,len(Meds)):
	if Meds[i].find('simvastatin') != -1:
		#print PID[i], MRN[i], Dates[i], Meds[i]
		results =  [PID[i], MRN[i], Dates[i], Meds[i]]
		#results_array = np.appen(results_array, [results])
		results_array3 = np.concatenate((results_array3, results), axis =0)

#save results
num_par = 4
results_array3 = results_array3.reshape(len(results_array3)/num_par, num_par)	

np.savetxt('simvastatin.csv',results_array3, fmt='%s', delimiter = ',')

## ACEi

results_array = np.array([])
for i in range(0,len(Meds)):
	if Meds[i].find('pril') != -1 and Meds[i].find('prilosec') == -1: # make sure to exclude prilosec
		#print PID[i], MRN[i], Dates[i], Meds[i]
		results =  [PID[i], MRN[i], Dates[i], Meds[i]]
		#results_array = np.appen(results_array, [results])
		results_array = np.concatenate((results_array, results), axis =0)

#save results
num_par = 4
results_array = results_array.reshape(len(results_array)/num_par, num_par)	

#Save Aspirin File
np.savetxt('ACEi_Clean.csv',results_array, fmt='%s', delimiter = ',')





#for item in Meds:
#    if item.find("Aspirin") != -1:
#        print item
#        print Dates

#for item in Meds:
#    if item.find("Aspirin") != -1:
#        print item, Dates


#for item in Meds:
#	i =np.where(item.find("Aspirin") != -1)
#	MedDate = Dates[i]
#	PtID = PID[i]
#	results = [PtID, MedDate]
#	print results
    

#for i in range(0,len(Meds)):
#	if Meds[i].find('Aspirin') != -1:
#		print Dates[i], PID[i]
 
#h = Meds[1].find('Aspirin') 
