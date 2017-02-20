import numpy as np
import pandas as pd
import pylab
from statsmodels.graphics.mosaicplot import mosaic
from itertools import product

rand = np.random.random

tuples = list(product(['bar', 'baz', 'foo', 'qux'], ['one', 'two']))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
data = pd.Series(rand(8), index=index)
mosaic(data, title='hierarchical index series')
pylab.show()
