import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('BatteryLog_360.csv',index_col='time',parse_dates=True)
print(df)
df.head()
df.plot(figsize=(12,6))