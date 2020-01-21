import os
import logging
import pyxdf 

from python_xdf_interp import Xdf_file_read

# First two inputs are the path
# The last input is the xdf_file
streams, fileheader = Xdf_file_read.Xdf_Load('xdf_files','Darpa_Subject_1','sub_P001_ses_S001_task_T1_run_001_eeg.xdf')


# Example
# stream[0...n] coresponds to the different streams (EEG, eye tracker)
# print(streams)

eyetracker =streams[0]
EEG = streams[1]

EEGdata = EEG['time_series']
timestamps = EEG['time_stamps']
# for i in range(len(EEG)):
#     channels = EEG[i]['label']

print(timestamps)
print(EEGdata)
# print(timestamps)

# print(eyetracker)

# streams[0...n]['whatever string you want in the dictionary] gives you the values corresponding to that string

# eyedata = eyetracker['time_series']
# timestamps = eyetracker['time_stamps']

# print(eyedata)
# print(timestamps)

