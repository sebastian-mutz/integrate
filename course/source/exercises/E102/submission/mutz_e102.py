import numpy as np
import math
from scipy.stats import norm
#
# CONSTRUCT MODELS (PDF) 
# =======================
#
# read files
data = np.genfromtxt('Antofagasta.csv', delimiter=',')
t2m=data[1::,2] # skip first line, read column 2 (2m air temperature)
nt=len(t2m)
ny=nt//12       # rounds off to full year, floor division
#
# calculate monsthly statistics
t2m_mean=[0.0]*12
t2m_stdv=[0.0]*12
x=[0.0]*ny
#
# get means and standard deviations
for m in range(12):        # loop through months
    # construct mean and stdv for temperatures
    for y in range(ny):
        x[y]=t2m[(y*12)+m] # pass month-specific temperature to x vector 
    t2m_mean[m]=np.mean(x)        
    t2m_stdv[m]=np.std(x)     
#
# print summary
print(' '.join('{:0.2f}'.format(i) for i in t2m_mean))        
print(' '.join('{:0.2f}'.format(i) for i in t2m_stdv))        
#
#
# HYPOTHESES TST
# ==============
# NOTE: here we use the normal distribution. t may be more fitting given the relatively small sample size.
#
# H0: the mean is still the one caulculated from observations
# HA: the mean is different from the one calculated from observations
# We test this by assuming H0 is correct and calculating the probability of getting a signal (temperature difference) at least as extreme as the observed.
#
# this is the data we were given (temperatures are converted to Kelvin like in dataset)
tm_jan=23.6+273.15    # predicted january temperatures
tm_jun=17.2+273.15    # predicted june temperatures
df=30                 # degrees of freedom (years in simulation)
#
# we calculate the standard error (standard deviation of sampling distribution)
serr_jan=t2m_stdv[0]/(float(df))**0.5    # standard error january
serr_jun=t2m_stdv[5]/(float(df))**0.5    # standard error june
#
# calculate the z-score/look at how far away we are from the mean (expressed in standard deviations of the sampling distribution)
z_jan=tm_jan-t2m_mean[0]/serr_jan
z_jun=tm_jun-t2m_mean[5]/serr_jun
#
# calculate p-values (2-tailed test)
p_jan=2*(1-(norm.cdf(z_jan, 0, 1)))   
p_jun=2*(1-(norm.cdf(z_jun, 0, 1)))   
#
print ("P(Jan signal or more extreme | H0) :",p_jan)
print ("P(Jun signal or more extreme | H0) :",p_jun)




















