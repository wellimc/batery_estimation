import pandas as pd 


SEQ_LEN = 5
FUTURE_PERIOD_PREDICT = 1
BITRATE_TO_PREDICT = "360" 

main_df = pd.DataFrame()
bitrates = ["360"]


def classify( current, future):
	if float(future) < (float(current) - (float(current) * 0.1)):
		return 1
	else: 
	 	return 0



for bitrate in bitrates:
for bitrate in bitrates:
	#print(bitrate)
	dataset = f"BatteryLog_{bitrate}.csv"

	df = pd.read_csv(dataset,names=["time","level","temp","voltage"])
	#print(df.head())
	df.rename(columns={"level": f"{bitrate}_level","voltage": f"{bitrate}_voltage"}, inplace=True )

	df.set_index("time",inplace=True)
	df = df[[f"{bitrate}_level",f"{bitrate}_voltage"]]

	#print(df.head)    

	if len(main_df) == 0:
		main_df = df 
	else:
		main_df = main_df.join(df)

main_df['future'] = main_df[f"{BITRATE_TO_PREDICT}_level"].shift(-FUTURE_PERIOD_PREDICT)
print(main_df.head())
