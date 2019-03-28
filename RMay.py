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
        newy=[]
        for r in range(1,len(y_val)):
            newy.append((y_val[r]-y_val[r-1])/y_val[r-1])
        y_val.remove(y_val[len(y_val)-1])
        t=np.array(y_val)      
        a=np.array(newy)
        plt.plot(t,a)
        plt.xlabel('N(t)')
        plt.ylabel('(N(t+1)-N(t))/N(t)')
        print('r=',rval[i],'k=',kval[j])
        plt.show()
        y_val.clear()