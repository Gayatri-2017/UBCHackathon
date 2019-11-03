import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
csv_location = "/Users/apple/Desktop/UBCHackathon_Local/UBCHackathon/ubc_course_calendar_data_new.csv"
data = pd.read_csv(csv_location) 
# Preview the first 5 lines of the loaded data 
# dropping null value columns to avoid errors 
data.dropna(inplace = True) 
  
  
# substring to be searched 
sub ='introduction'
  
# creating and passsing series to new column 
#data["Indexes"]= data["COURSE_DESCRIPTION"].str.find(sub) 
data["Indexes"]= data["COURSE_DESCRIPTION"].str.contains(sub, case=False) 

#if (ind < 0):
#    data["Indexes"] = "False"
#else:
#    data["Indexes"] = "True"
# display 
data.loc[data['Indexes'] == True]['COURSE_TITLE']