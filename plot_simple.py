#here's a line plot visualizing which birth dates are the most common in the dataset.
shelter_outcomes['date_of_birth'].value_counts().sort_values().plot.line()
'''
It looks like birth dates for the animals in the dataset peak at around 2015, but it's hard to tell for sure because the data is rather noisy.
Currently the data is by day, but what if we globbed all the dates together into years? This is known as resampling. 
We can do this to tweak the dataset, generating a result that's aggregated by year. The method for doing this in pandas, resample, is pretty simple. 
There are lots of potential resampling options: we'll use Y, which is short for "year".
'''
shelter_outcomes['date_of_birth'].value_counts().resample('Y').sum().plot.line()
shelter_outcomes['datetime'].value_counts().resample('Y').count().plot.line()
'''
Much clearer! It looks like, actually, 2014 and 2015 have an almost equal presence in the dataset.
This demonstrates the data visualization benefit of resampling: by choosing certain periods you can more clearly visualize certain aspects of the dataset.
Notice that pandas is automatically adapting the labels on the x-axis to match our output type. This is because pandas is "datetime-aware"; it knows that when we have data points spaced out one year apart from one another, we only want to see the years in the labels, and nothing else!
Usually the value of time-series data is exposed through this sort of grouping. For example, here's a similar simple bar chart which looks at the trade volume of the GOOG stock:
'''
stocks['volume'].resample('Y').mean().plot.bar()

'''
Lag plot
One of these plot types is the lag plot. A lag plot compares data points from each observation in the dataset against data points from a previous observation. So for example, data from December 21st will be compared with data from December 20th, which will in turn be compared with data from December 19th, and so on. For example, here is what we see when we apply a lag plot to the volume (number of trades conducted) in the stock data:
'''
from pandas.plotting import lag_plot
lag_plot(stocks['volume'].tail(250))

'''
Autocorrelation plot
A plot type that takes this concept and goes even further with it is the autocorrelation plot. The autocorrelation plot is a multivariate summarization-type plot that lets you check every periodicity at the same time. It does this by computing a summary statistic—the correlation score—across every possible lag in the dataset. This is known as autocorrelation.
In an autocorrelation plot the lag is on the x-axis and the autocorrelation score is on the y-axis. The farther away the autocorrelation is from 0, the greater the influence that records that far away from each other exert on one another.
Here is what an autocorrelation plot looks like when applied to the stock volume data:
'''
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(stocks['volume'])
'''
It seems like the volume of trading activity is weakly descendingly correlated with trading volume from the year prior. There aren't any significant non-random peaks in the dataset, so this is good evidence that there isn't much of a time-series pattern to the volume of trade activity over time.
Of course, in this short optional section we're only scratching the surface of what you can do with do with time-series data. There's an entire literature around how to work with time-series variables that we are not discussing here. But these are the basics, and hopefully enough to get you started analyzing your own time-dependent data!
'''
