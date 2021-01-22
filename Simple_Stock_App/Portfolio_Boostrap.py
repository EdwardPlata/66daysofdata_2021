# Taking code from here https://quantdare.com/bootstrapping-portfolio-management/#:~:text=Bootstrapping%20method&text=Faced%20with%20growing%20uncertainty%20in,the%20future%20of%20their%20investments.&text=Bootstrapping%20is%20a%20financial%20technique,sample%20of%20historical%20portfolio%20returns.

import pandas as pd 
import numpy as np
import yfinance as yf
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

from scipy.stats.kde import gaussian_kde
from scipy.stats import norm

start,end = datetime.datetime(2009,12,30), datetime.datetime(2016,12,31)
tickers = ["TLT", "HYG", "^GSPC", "^STOXX50E", "^N225", "^FTSE"]

universe = yf.downlaod(tickers,start=start,end=end)

