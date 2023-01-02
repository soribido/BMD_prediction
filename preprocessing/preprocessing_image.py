import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut

window_center = 400
window_width = 1800
count = 0

#%% read excel file
data = pd.read_csv('./L1_CT.csv')

bmdall = data.L1_BMD
dcmfileall = data.dcmfile

bmd = []
dcmfile = []
tsc = []
for i in range(len(data.dcmfile)):
    if os.path.isfile('total/'+data.dcmfile[i]):
        dcmfile.append(data.dcmfile[i])
        bmd.append(data.L1_BMD[i])
        tsc.append(data.L1_Tscore[i])
    else:
        pass
#%% dicom preprocessing

# Repeat this process for the pre and post sections of L1.
window_center = 400
window_width = 1800
count = 0
imgf = np.zeros((len(bmd),512,512,1))
for i in range(len(bmd)):
    totalpath=dcmf[i] #private(path)

    slice = pydicom.read_file(totalpath)
    s = int(slice.RescaleSlope)
    b = int(slice.RescaleIntercept)
    image = s * slice.pixel_array + b

    slice.WindowCenter = window_center
    slice.WindowWidth = window_width

    image3 = np.clip(image, window_center - (window_width / 2), window_center + (window_width / 2))
    # img_crop_ravel=image3.ravel()
    img_reshape = image3.reshape(512, 512, 1)
    
    imgf[i] = img_reshape
    
    
#%%
mask = np.load('mask2239c_dice.npy')
maskt = np.load('mask457c_dice.npy') 
roi_tr = np.load('256d1_train2239.npy')

l = len(roi_tr)
roi256 = np.zeros((l,256,256,1))

for j in range(len(roi256)):
    inx1 = np.where(mask[j]<0.2)    
    # inx1 = np.where((imgt[:,:,1]>0.4) & (imgt[:,:,2]>0.4))
    imgtt=roi_tr[j]    
    for i in range(len(inx1[0])):        
        imgtt[inx1[0][i],inx1[1][i],:]=-500
    roi256[j]=imgtt       
#%%
roi_tt = np.load('256d1_test2239.npy')   
lt = len(roi_tt)
roi256t = np.zeros((lt,256,256,1))

for j in range(len(roi256t)):
    inx1 = np.where(maskt[j]<0.2)    
    # inx1 = np.where((imgt[:,:,1]>0.4) & (imgt[:,:,2]>0.4))
    imgtt=roi_tt[j]    
    for i in range(len(inx1[0])):    
        imgtt[inx1[0][i],inx1[1][i],:]=-500
    roi256t[j]=imgtt      
    
#%%
def imgsave(xx):
    nn = (xx-np.min(xx))/(np.max(xx)-np.min(xx))*255
    nn1 = np.uint8(nn)
    for i in range(len(xx)):    
        img = np.squeeze(nn1[i])
        cv2.imwrite('sample/'+str(i)+'.png', img)    