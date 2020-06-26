import pandas as pd

#read a csv file
data = pd.read_csv("./SMSSpamData", sep='\t', names=['label', 'message'])

#save a csv file
data.to_csv('file1.csv') 

print("Number of rows,: ", len(data), "\tNumber of columns: ", len(data.columns))