import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Task 1
# ======

# given data
m1_m=24.2   # population 1 mean 
m1_s=6.1    # population 1 standard deviation
m2_m=25.9   # population 2 mean
m2_s=5.5    # population 2 standard deviation
t2m=24.5
n=30

# calculations
m1_error=m1_s/(float(n))**0.5   # standard error if we sampled from pop 1
m2_error=m2_s/(float(n))**0.5   # standard error if we sampled from pop 2
m1_z=(t2m-m1_m)/m1_error        # standard score if sampled from pop 1
m2_z=(t2m-m2_m)/m2_error        # standard score if sampled from pop 2

print ("P(T>24.5 | M1) :",1-(norm.cdf(m1_z, 0, 1)))   
print ("P(T>24.5 | M2) :",1-(norm.cdf(m2_z, 0, 1)))   

# plotting
x1 = np.linspace(m1_m - 3*m1_s, m1_m + 3*m1_s, 100)   # create data from population parameters
x2 = np.linspace(m2_m - 3*m2_s, m2_m + 3*m2_s, 100)   # create data from population parameters
plt.plot(x1, norm.pdf(x1, m1_m, m1_s))                # create plot
plt.plot(x2, norm.pdf(x2, m2_m, m2_s))                # create plot

x1 = np.linspace(m1_m - 3*m1_error, m1_m + 3*m1_error, 100)   # create data from distribution
x2 = np.linspace(m2_m - 3*m2_error, m2_m + 3*m2_error, 100)   # create data from distribution
plt.plot(x1, norm.pdf(x1, m1_m, m1_error))                # create plot
plt.plot(x2, norm.pdf(x2, m2_m, m2_error))                # create plot

plt.show()                                           


# Task 2
# ======

s=1.1 # estimate for population standard deviation
# Find distance in standard deviations for a confidence interval of 95. Note that this function in python takes the left integral. To get the distance from the mean, integrate to 1-0.25 (because you leave out the 0.25 tails on each side). The following give you the upper and lower bound. 
z1=norm.ppf(.975)    # percent point function 
z2=norm.ppf(.025)    # percent point function 
# Since the distribution is symmetrical, we can only use one of the z's from now on. The question wants to know the sample number required to make sure that the 95% confidence interval is the true mean +/- 0.5. We can therefore say abs(z2) = z1 = 0.5. We have an estimate for the population standard deviation and can estimate our sampling distribution standard deviation from by: 0.5/z1. Therefore, we can calculate the samples required for this interval as:
ns=(1.1/(0.5/z1))**2
print ('min. no. of samples required: ', ns)






