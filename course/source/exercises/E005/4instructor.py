# import module
import numpy as np
import matplotlib.pyplot as plt
#
# ---- NORMAL DATA
#
# read files
dat_nrm = np.genfromtxt('test_rnd_normal.asc')
dat_exp = np.genfromtxt('test_rnd_exponential.asc')
#
# pass data from normal distribution to x and y vectors
x=dat_nrm[:,0]
y=dat_nrm[:,1]
# 
# create simple x-y plot
plt.figure(0)                          # number your figures
plt.plot(x, y)                         # create a simple x-y plot
plt.title('rnd: normal distribution')  # set a title
plt.xlabel('time steps')               # label the x axis
plt.ylabel('random number')            # label the y axis  
plt.axis([0, 100, -3, 6])              # give x and y bounds
#
# create and plot histogram
plt.figure(1)                          # advance figure to create new plot
plt.hist(y,bins='auto')                # plot histogram with automatic bin size
plt.title('Histogram of Normal Data')  # plot title
#
#
# ---- EXPONENTIAL DATA
# 
# pass data from exponential distribution to x and y vectors
x=dat_exp[:,0]
y=dat_exp[:,1]
# 
# create simple x-y plot
plt.figure(2)                          # advance figure to create new plot
plt.bar(x, y)                          # make this a bar plot
plt.title('rnd: exponential distribution') # set a title
plt.xlabel('time steps')               # label the x axis
plt.ylabel('random number')            # label the y axis  
plt.axis([0, 100, 0, 10])              # give x and y bounds
#
# create and plot histogram
plt.figure(3)                          # advance figure to create new plot
plt.hist(y,bins='auto')                # plot histogram with automatic bin size
plt.title('Histogram of Exponential Data')  # plot title
#
# create histogram and save in text file
y_hist=np.histogram(y,bins=10)         # creates a histogram of array y with bin number of 10
np.savetxt('histogram.asc', y_hist[1], fmt='%1.3f', delimiter=',')