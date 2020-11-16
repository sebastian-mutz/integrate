import numpy as np
import math
from scipy.stats import norm
#
#
# BAYESIAN LEARNING FUNCTION
# ==========================
def update_posteriori(pri,nm,models,x):
    """
    update probabilities for different models based on new data, using bayes theorem

    takes:
    pri - priori probabilitties
    nm - number of models
    models - models
    x - new data point

    returns:
    pst - posteriori probabilities
    """
    #
    # update relative probabilities
    for i in range(nm):
        likelihood=norm.pdf(x,loc=models[i][0],scale=models[i][1])        
        pst[i]=likelihood*pri[i]    
    # normalising
    tmp=sum(pst)    
    for i in range(nm):
        pst[i]=pst[i]/tmp        
    return pst
#
#
#
#
# input files
infile=['Antofagasta.csv','Quintero.csv','Puerto_Montt_el_Tepual.csv']
#
# CONSTRUCT MODELS (PDF) 
# =======================
#
# create lists to store means and standard deviations for 3 wind direction models (for each month)
a_mean=['']*len(infile)
a_stdv=['']*len(infile)
for i in range(len(infile)):
    a_mean[i]=[0.0]*12  
    a_stdv[i]=[0.0]*12
#       
# loop over 3 datasets
for i in range(len(infile)):
    # read files
    data = np.genfromtxt(infile[i], delimiter=',')
    u=data[1::,3]   # skip first line, read column 4 (u wind)
    v=data[1::,4]   # skip first line, read column 5 (v wind)
    nt=len(u)
    ny=nt//12       # rounds off to full year, floor division
    #
    # calculate wind speed
    #w=(u**2+v**2)**0.5    
    # calculate wind direction
    a=[0.0]*nt
    for j in range(nt):
        a[j]=math.degrees(math.atan(u[j]/v[j])) # clockwise deviation from N     
    #
    # calculate monsthly statistics
    x=[0.0]*ny
    #
    # get means and standard deviations
    for m in range(12):        # loop through months
        # construct mean and stdv for wind angles 
        for y in range(ny):
            x[y]=a[(y*12)+m]   # pass month-specific wind angles to x vector 
        a_mean[i][m]=np.mean(x)        
        a_stdv[i][m]=np.std(x)
#
# print summary
for i in range(len(infile)):
    print(i,' '.join('{:0.2f}'.format(i) for i in a_mean[i]))        
    print(i,' '.join('{:0.2f}'.format(i) for i in a_stdv[i]))
#
#
#
#
# BAYESIAN CATEGORISATION
# =======================
#
nm=3                  # number of models
x=[11.4, -30.8, 60.2] # data to be categorised
models=[0.0]*nm       # construct models for June wind directions: nm models consisting of 2 parameters (mean and standard deviation)
for i in range(nm):
    models[i]=a_mean[i][5], a_stdv[i][5]
#
for d in range(len(x)):
    pri=[1/float(nm)]*nm  # non-informative priors
    pst=pri               # posteriori probabilities (set to priors before learning)
    pst=update_posteriori(pri,nm,models,x[d])
    print('pst_p for ', x[d] , ' :    ', ' '.join('{:0.2f}'.format(j) for j in pst)) 
    
#





























