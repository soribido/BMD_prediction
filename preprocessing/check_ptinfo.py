import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import copy

#%%
path2 = 'private' # private
df_tr = pd.read_excel(path2+'traininfo.xlsx')
df_te = pd.read_excel(path2+'testinfo.xlsx')

#%%
from scipy.stats import sem
age = df_tr['Age']
print(np.std(age))

aget = df_te['Age']
print(np.mean(aget))
print(np.std(aget))

#%%
sex = df_tr['Sex']

se = list(sex)

idtr = list(df_tr.ID)
eg = list(set(df_tr.ID))

x1 = []
for i in range(len(eg)):
    x1.append(idtr.index(eg[i]))

x11 = []
for i in range(len(x1)):
    x11.append(se[x1[i]])
# df_tr2 = copy.deepcopy()


men = (np.array(x11)==1).sum()
women = (np.array(x11)==2).sum()

#%%
sex2 = df_te['Sex']

ns2 = np.array(list(sex2))
eg2 = np.array(list(set(df_te.ID)))

men2 = (sex2==1).sum()
women2 = (sex2==2).sum()
#%%
from datetime import datetime

now  = datetime.now()
print("현재 :", now)
#%%
ct = df_tr['CT']
dxa = df_tr['BMD']
diff=[]
for i in range(len(ct)):
    compare1 = datetime.strptime(str(ct[i]), "%Y%m%d")
    compare2 = datetime.strptime(str(dxa[i]), "%Y%m%d")
    dd = compare2-compare1
    diff.append(dd.days)
    
#%%
ctt = df_te['CT']
dxat = df_te['BMD']
diff2=[]
for i in range(len(ctt)):
    compare1 = datetime.strptime(str(ctt[i]), "%Y%m%d")
    compare2 = datetime.strptime(str(dxat[i]), "%Y%m%d")
    dd = compare2-compare1
    diff2.append(dd.days)

#%%
"_".join(df_te.ID[0],df_te.CT[0])
#%%
bmdtest=[]
testkey = list(df_te.key)

#%%
key_list = pd.read_excel('private')
df_list = pd.read_excel('private')
for i in range(len(df_te)):
    keyindex = key_list.index(testkey[i])
    bmdtest.append(df_list['BMD'][keyindex])    #key중 test의 key값과 같은 위치 찾기
    
#%%
df_te['BMD']=bmdtest
df_te.to_excel(path2+'testinfo0923.xlsx')    
#%%
dcmfile = []
for i in range(len(df_te)):
    name = df_te.key[i]+'_'+str(1)+'_'+str(df_te["L1 cut"][i])+'.dcm'
    dcmfile.append(name)
#%%
df_te['dcmfile']=dcmfile 
df_te.to_excel('__')     

#%%
age = df_te.Age
gen = df_te.Sex

age4 =[]
for i in range(len(age)):
    if age[i]<50:
        age4.append('<50')
    if ((age[i]>=50) and (age[i]<60)):
        age4.append('50~60')
    if ((age[i]>=60) and (age[i]<70)):    
        age4.append('60~70')
    if age[i]>=70:
        age4.append('>70')
#%%
df_te['bin']=age4        

#%%
import seaborn as sns
plt.figure()
sns.set_style("whitegrid")
sns.boxplot(data=df_te, y='BMD',x='bin')
plt.show()
# sns.boxplot()



