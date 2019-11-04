import pandas as pd 
import re
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
# csv_location = "/Users/apple/Desktop/UBCHackathon_Local/UBCHackathon/ubc_course_calendar_data_new.csv"
# data = pd.read_csv(csv_location) 
# Preview the first 5 lines of the loaded data 
# dropping null value columns to avoid errors 
# data.dropna(inplace = True) 
  
  
# substring to be searched 
# sub ='introduction'
  
# creating and passsing series to new column 
#data["Indexes"]= data["COURSE_DESCRIPTION"].str.find(sub) 
# data["Indexes"]= data["COURSE_DESCRIPTION"].str.contains(sub, case=False) 

#if (ind < 0):
#    data["Indexes"] = "False"
#else:
#    data["Indexes"] = "True"
# display 
# data.loc[data['Indexes'] == True]['COURSE_TITLE']

def search_interests(interest):
	csv_location = "/Users/apple/Desktop/UBCHackathon_Local/UBCHackathon/ubc_course_calendar_data_new.csv"
	data = pd.read_csv(csv_location) 
	data.dropna(inplace = True) 
	sub = interest
	data["Indexes"]= data["COURSE_DESCRIPTION"].str.contains(sub, case=False)
	# disp_str =  str(data.loc[data['Indexes'] == True]['COURSE_TITLE'])
	df = pd.DataFrame(data[data['Indexes'] == True]['COURSE_TITLE'])
	courses_titles = df["COURSE_TITLE"].unique()

	# disp_str =  "<br>".join(data.loc[data['Indexes'] == True]['COURSE_TITLE'])
	# disp_str =  str(data.loc[data['Indexes'] == True]['COURSE_TITLE'])
	# if disp_str is not None:
	# 	disp_str = re.split("Name", disp_str, flags=re.IGNORECASE)[0]
	# else:
	# 	disp_str = "<br>No results found for your search interest. <br>Check spelling or try another broader search keyword"
	disp_str = "<br>"
	if courses_titles is not None:
	# disp_str = re.split("Name", disp_str, flags=re.IGNORECASE)[0]
		disp_str += "<br>".join(courses_titles)
	else:
		disp_str += "No results found for your search interest. Check spelling or try another broader search keyword"
	return disp_str