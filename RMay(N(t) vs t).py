import math
import numpy as np
import matplotlib.pyplot as plt

rval=[1,2,3,4]
kval=[1000,10000]
x=[]
for m in range (0,151):
    x.append(m)
for j in range(0,2):
    
    for i in range(0,len(rval)):
        y_val=[2]
        y_val.append(2*np.exp(rval[i]*(1-(2/kval[j]))))    
        while len(y_val)<151:    
            y_val.append(y_val[len(y_val)-1]*np.exp(rval[i]*(1-((y_val[len(y_val)-1])/kval[j]))))
        
        
        t=np.array(x)      
        a=np.array(y_val)
        plt.plot(t,a)
        plt.xlabel('t')
        plt.ylabel('N(t)')
        plt.show()
        y_val.clear()
   
