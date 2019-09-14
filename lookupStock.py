import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2018,5,1)
end = dt.datetime(2018,7,30)

df = web.DataReader('F', 'google', start, end)
print(df.tail(6))
