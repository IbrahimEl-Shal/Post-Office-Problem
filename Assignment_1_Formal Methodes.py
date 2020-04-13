# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 11:49:07 2018

@author: Ibrahim El-Shal
"""
# In[1]: Import Packages and Files

import time
import random
import numpy as np
import matplotlib.pyplot as plt 
from Distance_Matrix_Generator import Gererate_Distance_Matrix
from Distance_Matrix_Generator import Gererate_Enhanced_Distance_Matrix

# In[2]: Main Programme 

def Main_Algorithm(NV):  #NV : Number of Villages (Cities)

    T1 = time.time()
    ## Variables Initialization ##
    
    Max_X = 10000                  #Max_X : Maximum distance of area in X-axis (Meter) 
    Max_Y = 10000                  #Max_Y : Maximum distance of area in Y-axis (Meter) 
    Minimum_Value_1 = Minimum_Value_2 = 0    #Represents to the best candidates
    Maximum_Mat_values = np.zeros((NV,1))    #Materix to save the maximum value in each Row

    ## Generate the Nodes Coordinates (Cartesian Coordinate) ##
    
    X_Coordinate = np.array(random.sample(range(Max_X), NV))
    Y_Coordinate = np.array(random.sample(range(Max_Y), NV))
    Coordinates = (np.column_stack((X_Coordinate,Y_Coordinate))).T   #The (x,y) Coordinates of Villages
    
    ## Get the Euclidean Distance Matrix ##
    
    Matrix_of_Distance , time_elapsed = Gererate_Distance_Matrix(2,NV,Coordinates)
    #Matrix_of_Distance , time_elapsed = Gererate_Enhanced_Distance_Matrix(2,NV,Coordinates)

    ## Algorithm to find the office location minimizing the average distance ##
    T2 = time.time()
    Matrix_of_Average = np.mean(Matrix_of_Distance, axis=0)
    Minimum_Value_1 = int(np.argmin(Matrix_of_Average)) 
    Best_Candidate_1 = Minimum_Value_1 + 1      #Best Post-office location (Minimize Avg.)

    T3 = time.time()
    ## Algorithm to find the office location minimizing the maximum distance ##
   
    Maximum_Mat_index = np.argmax(Matrix_of_Distance,axis=0)

    for Ro in range(0,NV):
        Maximum_Mat_values[Ro] =  Matrix_of_Distance[Ro][Maximum_Mat_index[Ro]]

    Minimum_Value_2 = int(np.argmin(Maximum_Mat_values))
    Best_Candidate_2 = Minimum_Value_2 + 1      #Best Post-office location (Minimize Max.)
    
    T4 = time.time()
    
    TA = T3 - T1
    TM = T4 - T1 -(T3-T2) 
    
    return (TA,TM,Best_Candidate_1,Best_Candidate_2)

# In[9]: Running code at different [n]
 
Villages_No = np.array([10,100,1000,5000,10000])
Time_Max_Matrix = np.zeros(shape=(len(Villages_No),1))
Time_Avg_Matrix = np.zeros(shape=(len(Villages_No),1))

for V in range(0,len(Villages_No)):
    
    TA,TM,Best_Candidate_1,Best_Candidate_2 = Main_Algorithm(Villages_No[V])

    Time_Avg_Matrix[V] = TA
    Time_Max_Matrix[V] = TM
    
# In[10]: Plotting data

fig1 = plt.figure()

plt.title('Order of Growth')
plt.xlabel('Number of Villages (N)')
plt.ylabel('Time Elapsed [Avg Case] (Sec)')
plt.plot(Villages_No,Time_Avg_Matrix,'k',Villages_No,Time_Avg_Matrix,'bo')

fig1.savefig('Order of Growth[Avg Case].jpg')

fig2 = plt.figure()
plt.title('Order of Growth')
plt.xlabel('Number of Villages (N)')
plt.ylabel('Time Elapsed [Max Case] (Sec)')
plt.plot(Villages_No,Time_Avg_Matrix,'r',Villages_No,Time_Avg_Matrix,'bo')

fig2.savefig('Order of Growth[Max Case].jpg')