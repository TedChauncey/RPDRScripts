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
MedsFile = 'FirstMedDates.csv'  # this is the file with the clean Meds Start dates 
MedFile = pd.read_csv(Directory+MedsFile)
MedMRN = pd.Series.as_matrix(MedFile.loc[:, 'MRN'])
 
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
RTDates = RTData.reshape(len(RTData)/RTparams, RTparams) 

#np.savetxt('RTStartDates.csv', RTDates , fmt='%s', delimiter = ',')


