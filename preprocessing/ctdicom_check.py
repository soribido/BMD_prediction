import numpy as np
import os
import pydicom
import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_voi_lut
import cv2
import pandas as pd
from sklearn.model_selection import train_test_split
#%%
path1 = 'D:/research/Data정리0501/CT정리본/558073_20200507_1/558073_20200507_1_0095.dcm'
path2 = 'D:/research/Data정리0501/CT정리본/558073_20200507_1/558073_20200507_1_0202.dcm'
path3 = 'D:/research/Data정리0501/CT정리본/560573_20180208_1/560573_20180208_1_0202.dcm'
path4 = 'D:/research/Data정리0501/CT정리본/560573_20180208_1/560573_20180208_1_0095.dcm'
#%%
slice = pydicom.read_file(path1)
s = int(slice.RescaleSlope)
b = int(slice.RescaleIntercept)
image1 = s * slice.pixel_array + b

slice = pydicom.read_file(path2)
s = int(slice.RescaleSlope)
b = int(slice.RescaleIntercept)
image2 = s * slice.pixel_array + b

slice = pydicom.read_file(path3)
s = int(slice.RescaleSlope)
b = int(slice.RescaleIntercept)
image3 = s * slice.pixel_array + b

slice = pydicom.read_file(path4)
s = int(slice.RescaleSlope)
b = int(slice.RescaleIntercept)
image4 = s * slice.pixel_array + b

#%%
print(np.max(image1), np.min(image1))
print(np.max(image2), np.min(image2))
print(np.max(image3), np.min(image3))
print(np.max(image4), np.min(image4))
