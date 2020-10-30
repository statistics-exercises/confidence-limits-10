# Further histograms for continuous random variables

For this exercise I want you to write the code for computing the histogram for a continuous ranodm variable.  Now though we are going to make things slightly more complicated as you will be generating uniform random variable that lie between -1 and 3.  Most of the code is the same but you now need to use the following code when computing which of the n bins each data point falls within:

````
delr = 4 / n
mybin = int( np.floor( (U + 1)/delr ) )
where U is the uniform random variable that falls between -1 and 3.
`````

Furthermore, as we learned in the lectures and videos, a probability density function, ![](https://render.githubusercontent.com/render/math?math=f(x)) is normalised if:

![](https://render.githubusercontent.com/render/math?math=\int_{-\infty}^{\infty}f(x)\textrm{d}x=1)

So the area under your final histogram should be one.  When you normalise the points in the list called counts you should thus divide by the number of points sampled and the width of the bins (`delr`).

With all that in mind, to complete the task you will need to:

1. Write a function called `myrandom` that generates continuous uniform random variables that lie between -1 and 3.
2. Write a loop that generates 300 random variables using the function `myrandom`.
3. Use the list called `counts` to count how many of each of these random variables fall into each of the 100 bins that we have divided the line segment between -1 and 3 into.
4. Normalise the histogram in `counts` so that the integral under the curve that you will draw is one.  You thus need to divide each element of the list counts by the number of points you generated and the width of each of the bins in the histogram. 
5. Within the loop that normalises the `counts` array you should also generate the x-coordinates at which you will plot each of the data points in the `counts` list.  These x-coordinates should be placed at the midpoint of each of the bins.  Furthermore, as you can see the zeroth element of the histogram will be plotted at `(xdata[0], counts[0])`, the first element of the histogram will be plotted at `(xdata[1],counts[1])` and so on.  Your midpoints should thus be stored in the list called `xdata`.
