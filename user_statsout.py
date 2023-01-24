"""

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics
import math

# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]
print(f"{statistics.mean(scores)}")
print(f"{statistics.median(scores)}")
print(f"{statistics.mode(scores)}")
print(f"{statistics.pvariance(scores)}")
print(f"{math.sqrt(statistics.mean(scores))}")

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)

import pandas as pd
import numpy as np
import scipy
from scipy import stats

x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]
intercept = np.polyfit(x_times, y_temps, 1)
print(intercept)

linear_regression = stats.linregress(x=x_times, y=y_temps)
linear_regression.slope
linear_regression.intercept

# slope and intercept copied from terminal
y_future = (2.776223776223776 * 13) + 3.1212121212121247
print(f"{y_future: 0.2f}")

