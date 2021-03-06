import matplotlib.pyplot as plt
import numpy as np

def myrandom() : 
  # Your code to generate a uniform random variable between -1 and 3 goes here.

n = 100     # This is the number of bins in your histogram
counts = np.zeros(n)
delr =      # this is the widths of the bins in the histogram
# Here you need a loop to generate 300 continuous uniform random variables using the 
# function myrandom.  You should use the list called counts to count how many of 
# these random variables fall in each of the 100 bins that we divide the line segment between 
# -1 and 3 into.


# Here you should write a loop to normalise the histogram and to generate the x coordinate
# at which to plot each of the values in the list called count.  Remember that the x-coordinates
# should be placed at the midpoint of each bin.  
xdata = np.zeros(n)


plt.plot( xdata, counts, 'k-' )
plt.savefig("mypdf.png")
