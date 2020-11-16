import numpy as np
import math
from scipy.stats import norm
#
#
# SOME STATISTICS FUNCTIONS
# =========================

def xmean(x,n):
    """
    computes mean
    """
    a=0.0
    for i in range(n):
        a=a+x[i]    
    a=a/float(n)
    return a

def variance(x,n):
    """
    computes variance
    """
    mu=xmean(x,n)
    a=0.0
    for i in range(n):
        a=a+(x[i]-mu)*(x[i]-mu)
    a=a/float(n)
    return a

def covariance(x,y,n):
    """
    computes covariance
    """
    mux=xmean(x,n)
    muy=xmean(y,n)    
    a=0.0
    for i in range(n):
        a=a+(x[i]-mux)*(y[i]-muy)
    a=a/float(n)  
    return a

def correlation(x,y,n):
    """
    computes pearson correlation coefficient
    """
    a=covariance(x,y,n)/math.sqrt(variance(x,n)*variance(y,n))
    return a
#
#
#
#
#
# DETERMINING DEPENDENCE
# ======================
#
# input files
infile=['Antofagasta.csv','Quintero.csv','Puerto_Montt_El_Tepual.csv']
#
# read aaoi and mei data
ydat = np.genfromtxt('aaoi.csv', delimiter=',')
y1   = ydat[1::,1]
y2   = np.genfromtxt('mei.csv')
#
# loop over 3 datasets
for i in range(len(infile)):
    # read files
    xdat = np.genfromtxt(infile[i], delimiter=',')
    var=xdat[1::,2]               # temperature in 3rd column 
    nt=len(var)
    na=nt//12
    x=['']*(na)
    #
    # extract individual month (alternatively loop over all months)
    m=0
    for j in range (5,nt,12):    # start with 5th month, go in steps of 12
        m=m+1
        x[m-1]=var[j]       
    print ('station', i, ', AAOI PCC: ', correlation(x,y1,na))    
    print ('station', i, ', MEI PCC: ', correlation(x,y2,na))        
















