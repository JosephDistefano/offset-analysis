import os
import os.path
from Python_xdf.Python.python_xdf_interp import Xdf_file_read
import pandas as pd
import time


# Initial Variables
Levels = ['Baseline','StaticRed','DynamicRed']

# Getting subject name and length of subject list
subjectdir = os.getcwd() +'\\data\\raw'
subjects = os.listdir(subjectdir)
numbersubject = len(os.listdir(subjectdir))
initialsubjectid = 1001

# Initializing hdf file

# Iterating through the subject
for item in range(numbersubject):
    subjectid = str(initialsubjectid +item)
    subjectstr = 'sub_OFS_'+ subjectid
    xdfpath = subjectdir + '\\' + subjectstr + '\\xdf'
    VSpath = subjectdir + '\\' + subjectstr + '\\VS'
    MOTpath = subjectdir + '\\' + subjectstr + '\\MOT'

    # Initial set up of the HDF file


    # XDF data Extraction
    for xdf in range(len(os.listdir(xdfpath))):
        xdffilename = 'sub_OFS_' + subjectid + '_ses-s00' + str(xdf+1) + '_task-T1_run-001_eeg.xdf'
        streams, fileheader = Xdf_file_read.Xdf_Load(xdfpath + '\\' + xdffilename) 
        streamslist = []
        streamslist.append(streams[0]['info']['name'])
        streamslist.append(streams[1]['info']['name'])
        streamslist.append(streams[2]['info']['name'])
        streamslist.append(streams[3]['info']['name'])
        
        # Identifying the right stream (each xdf is different)
        for i in range(len(streamslist)):
            if streamslist[i] == ['CGX Quick-30 30CH Q30-0083 Impedance']:
                Impedance = streams[i]
            if streamslist[i] ==  ['CGX Quick-30 30CH Q30-0083']:
                EEG = streams[i]
            if streamslist[i] == ['Tobii_Eye_Tracker']:
                eyetracker = streams[i]
            if streamslist[i] == ['parameter_server_states']:
                server = streams [i]

    # Storing the xdf files in the hdf file
    
        

    # Visual Search Data Extraction
    VSfilename = 'VS_OFS_' + subjectid + '.csv'
    VSdatapath = VSpath + '\\' + VSfilename
    VSdata = pd.read_csv(VSdatapath)

    # Storing the VS data in the HDF file

    # Multi Object Search Data Extraction
    MOTfilename = 'MOT_OFS_' + subjectid + '.csv'
    MOTdatapath = MOTpath + '\\' + MOTfilename
    MOTdata = pd.read_csv(MOTdatapath)

    # Storing the MOT data in the HDF file







#### If you want to extract the time series and time stamp data

# EEGdata = EEG['time_series']
# EEGtimestamps = EEG['time_stamps']
# eyedata = eyetracker['time_series']
# eyetimestamps = eyetracker['time_stamps']
# serverdata = parameter_server['time_series']
# servertimestamps = parameter_server['time_stamps']
# Impedancedata = Impedance['time_series']
# Impedancetimestamps = Impedance['time_stamps']
