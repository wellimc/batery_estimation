import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


SEQ_LEN = 5
FUTURE_PERIOD_PREDICT = 1
BITRATE_TO_PREDICT = "360" 

main_df = pd.DataFrame()
bitrates = ["360","480"]


from sklearn.linear_model import LinearRegression
lin_regression = LinearRegression()

from sklearn.linear_model import LogisticRegression
log_regression = LogisticRegression(solver='lbfgs')

from sklearn.metrics import mean_squared_error, r2_score

for bitrate in bitrates:
	#print(bitrate)
	dataset = f"BatteryLog_{bitrate}.csv"

	df = pd.read_csv(dataset,names=["time","level","temp","voltage"])
	#print(df.head())
	df.rename(columns={"level": f"{bitrate}_level"}, inplace=True )

	df.set_index("time",inplace=True)
	df = df[[f"{bitrate}_level"]]

	#print(df.head)    

	if len(main_df) == 0:
		main_df = df 
	else:
		main_df = main_df.join(df)


