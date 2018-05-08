## This script correlates RT MRNs and relavant MRNs corresponding to med start dates
## Author Tafadzwa Chaunzwa 3.31.18

import numpy as np
import pandas as pd
import os
import csv
import sys
import time, glob

File = 'RTDates.csv'
Directory = '/home/chintan/Desktop/RPDR/'
OpenFile = pd.read_csv(Directory+File)
print(OpenFile.shape) 

## import RT data 
RTDates = pd.Series.as_matrix(OpenFile.loc[:, 'radstartdate'])
RTPID = pd.Series.as_matrix(OpenFile.loc[:, 'pin'])            
RTMRN = pd.Series.as_matrix(OpenFile.loc[:, 'bwhmrn'])

##extract RT dates only for patients with Rx of interest ##
MedsFile = 'MedStartDates.csv'  # Change this to relavant Med start file
MedFile = pd.read_csv(Directory+MedsFile)
MedMRN = pd.Series.as_matrix(MedFile.loc[:, 'MRN']) # make sure this column label is present

#find indeces in RT patient list that correspond to patients started on pertinent drug
idx1 = pd.Index(MedMRN) 
idx2 = pd.Index(RTMRN)
Overlap = idx2.intersection(idx1)
indexes = pd.np.where(idx2.isin(Overlap))[0]

RTData = np.array([])
for x in range(0,len(indexes)):
	RadDates = [RTMRN[indexes[x]], RTDates[indexes[x]], RTPID[indexes[x]]]
	RTData = np.concatenate((RTData, RadDates), axis = 0)

RTparams = 3 # number of returned parameters
RTDates = RTData.reshape(len(RTData)/RTparams, RTparams) 

np.savetxt('RTStartDates.csv', RTDates , fmt='%s', delimiter = ',')

## After running this script you can compare MedStartDates.csv with RTStartDates.csv
