# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 05:34:07 2018

@author: Ibrahim El-Shal
"""
# In[1]: Import Packages

import numpy as np
import time
import math 

# In[2]: Function Implementation

def Gererate_Distance_Matrix(Row,Column,Matrix):
    
    t1 = time.time()
    Distance = 0
    Distance_Vact = np.zeros((Row,1))            #Temp Distance Vector
    Distance_Mat = np.zeros((Column,Column))     #Distance Materix
    
    for Co in range(0,Column):
        for Ro in range(0,Column):
           
            for i in range(0,Row):
                Distance_Vact[i] = ((Matrix[i][Co] - Matrix[i][Ro])**2)
            Distance = math.sqrt(sum(Distance_Vact))
            
            Distance_Mat[Ro][Co] = Distance    
    
    t2 = time.time()
    time_elapsed = (t2-t1)                    #/60.0 #in minutes       
    return (Distance_Mat,time_elapsed) 

# In[3]: Enhanced Implementation of the Function

def Gererate_Enhanced_Distance_Matrix(Row,Column,Matrix):
    
    t1 = time.time()
    Distance = Flag = 0
    Distance_Mat = np.zeros((Column,Column))     #Distance Materix
   
    for Co in range(0,Column):
        for Next in range(0,Column):
            
            if(Flag != 0 and (Next < Co)):
                Distance_Mat[Next][Co] = Distance_Mat[Co][Next]  
                    
            if(Co != Next): 
                Distance = ((Matrix[0][Co] - Matrix[0][Next])**2) + ((Matrix[1][Co] - Matrix[1][Next])**2)

            Distance_Mat[Next][Co] = Distance
            Distance = 0
            Flag = 1
        
    t2 = time.time()
    time_elapsed = (t2-t1)                    #/60.0 #in minutes       
    return (Distance_Mat,time_elapsed)

# In[4]:
    
#Distance = np.abs((Matrix[i][Co] - Matrix[i][Next])) + Distance    #Absolute will Spend more much time
    