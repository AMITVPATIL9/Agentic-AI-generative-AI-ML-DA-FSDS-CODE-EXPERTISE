#  IMPORTNING THE LIBRARY

import numpy as np 	#Array		

import matplotlib.pyplot as plt		

import pandas as pd		



#--------------------------------------------

# import the dataset & divided my dataset into independe & dependent
#dataset = pd.read_csv(r"C:\Users\Admin\Desktop\A3MAX\2. A3MAX BATCHES\Agentic AI, Gen AI, FSDS_ 1\4. Nov\5th, 6th- ML\5. Data preprocessing\Data.csv")
dataset = pd.read_csv(r"C:\Users\ammyg\Desktop\DATA SCIENCE\clasroom material\13 dec\13th - ML\5. Data preprocessing\Data.csv")
X = dataset.iloc[:, :-1].values	

Y = dataset.iloc[:,3].values  

#--------------------------------------------

from sklearn.impute import SimpleImputer
imp = SimpleImputer(strategy = 'mean')

# x mein changes karte hai
X[:,1:3] = imp.fit_transform(X[:,1:3])
#imp.fit(X[:,1:3])
#imp.transform(X[:,1:3])

# encode categorical data and create dummy variable
from sklearn.preprocessing import LabelEncoder
label_enc_x = LabelEncoder()
label_enc_x.fit_transform(X[:,0])
X[:,0] = label_enc_x.fit_transform(X[:,0])

# SPLITTING THE DATASET INTO TRAINING AND TESTING SET
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size= 0.2, random_state=0) 
# if you remaove random state the your model will not behave accurately
#--------------------------------------------------------------------------
#FEATURE SCALING

#from sklearn.preprocessing import Normalizer

#sc_X = Normalizer() 

#X_train = sc_X.fit_transform(X_train)

#X_test = sc_X.transform(X_test)

#---------------------------------------------------------------------
































#--------------------------------------------
#from sklearn.model_selection import train_test_split(dataset,test_size = 20,train_size = 80,)

