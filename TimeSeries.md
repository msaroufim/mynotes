# Practical Time Series
Github repo: https://github.com/PracticalTimeSeriesAnalysis/BookRepo

Historical applications of time series analysis
* Audio processing
* Weather
* Economics: started after great depression
* Astronomy
* Medical: ECG, brain data
* Sensors: robots and IOT

A lot more applications than images or text

ML in time series started around 1980. Applications were
* Anomaly detection for network security (something I worked on at JPL)
* Measuring similarity between signals
* Recursive neural networks for salvaging corrupted data

Need to to be aware of lookahead problem where we leak information from future to the past. This can be an issue especially if different tables have different time resolutions.


Python data processing code
```
enails[emails.EmailsOpened < 1] 

YearJoined.groupby('memberId).count().
            groupby('memberStats).count()
```

The ```panda``` library makes working with time series much more sane


Index shows up a lot https://www.geeksforgeeks.org/python-pandas-index-values/

Timezones matter a lot, stuff like daylight savings time will trip you up

How to handle missing data
* Imputation: fill data based on global data
* Interpolation: Use neighboring data
* Deletion: of all affected time periods

The standard train and test split does not work for time series

When given a new dataset check
* Correlation of columns
* Mean and variance of each variable
* Stationarity
* Self correlation (e.g: ACF, PACF )
* Spurious correlations

Chapter 4-7 Look like the most interesting in the book