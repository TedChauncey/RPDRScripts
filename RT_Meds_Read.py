## This script reads a meds file (e.g statin/aspirin), and outputs first date of 
## medication for each patient 
## Author Tafadzwa Chaunzwa 3.31.18

import numpy as np
import pandas as pd
import os
#import SimpleITK as sitk
import csv
import sys
import time, glob

File = 'Aspirin.csv'
Directory = '/home/chintan/Desktop/RPDR/'
OpenFile = pd.read_csv(Directory+File)
print(OpenFile.shape) 

# make sure these are all sorted before importing
Meds = pd.Series.as_matrix(OpenFile.loc[:, 'Medication'])
Dates = pd.Series.as_matrix(OpenFile.loc[:, 'Medication_Date'])
PID = pd.Series.as_matrix(OpenFile.loc[:, 'EMPI'])
MRN = pd.Series.as_matrix(OpenFile.loc[:, 'MRN'])


a = np.array([]) # where a is dummy variable for saving first instances
for i in range(0,len(PID)-1):
	if np.diff(PID)[i] != 0:
		first_instance = [PID[i+1].reshape(1,), MRN[i+1], Dates[i+1]]
		a = np.concatenate((a, first_instance), axis = 0)

#	
params = 3 # number of returned parameters
a = a.reshape(len(a)/params, params)  
#include the first value of first patient
in_val = [PID[0].reshape(1,), MRN[0], Dates[0]]
in_val = np.asarray(in_val).reshape(1,params)

MedDates = np.concatenate((in_val, a), axis =0)

#Save the dates
np.savetxt('FirstMedDates2.csv', MedDates , fmt='%s', delimiter = ',')

###import RT data ###

File = 'RTDates.csv'
Directory = '/home/chintan/Desktop/RPDR/'
OpenFile = pd.read_csv(Directory+File)
print(OpenFile.shape) 
 
# make sure these are all sorted before importing
RTDates = pd.Series.as_matrix(OpenFile.loc[:, 'radstartdate'])
RTPID = pd.Series.as_matrix(OpenFile.loc[:, 'pin'])            
RTMRN = pd.Series.as_matrix(OpenFile.loc[:, 'bwhmrn'])

##extract RT dates only for patients with Rx of interest ##

MedMRN = MedDates[:,1]  # alternatively change this to the saved file 
idx1 = pd.Index(MedMRN) # change this to match the patients with the drug only
idx2 = pd.Index(RTMRN)
#Overlap2 = idx1.intersection(idx2)

Overlap = idx2.intersection(idx1)

indexes = pd.np.where(idx2.isin(Overlap))[0]  ## change idx1 as needed

RTData = np.array([])
for x in range(0,len(indexes)):
	RadDates = [RTMRN[indexes[x]], RTDates[indexes[x]]]
	RTData = np.concatenate((RTData, RadDates), axis = 0)

RTparams = 2 # number of returned parameters
RTData = RTData.reshape(len(RTData)/RTparams, RTparams) 

np.savetxt('RTStartDates.csv', RTData , fmt='%s', delimiter = ',')


