import pandas as pd 
import re

interest = "introduction"
csv_location = "/Users/apple/Desktop/UBCHackathon_Local/UBCHackathon/ubc_course_calendar_data_new.csv"
data = pd.read_csv(csv_location) 
data.dropna(inplace = True) 
sub = interest
data["Indexes"]= data["COURSE_DESCRIPTION"].str.contains(sub, case=False)
print("data = \n", data[data["Indexes"]==True])
# disp_str =  str(data.loc[data['Indexes'] == True]['COURSE_TITLE'])
df = pd.DataFrame(data[data['Indexes'] == True]['COURSE_TITLE'])
#fil1 = data["Indexes"] == "True"
#print("where clause\n", data.where(fil1, inplace=True))
#print("df = \n", df, "\n\n")	
courses_titles = df["COURSE_TITLE"].unique()
print("df[COURSE_TITLE]\n", courses_titles)

# disp_str = str(data[data['Indexes'] == True]['COURSE_TITLE'])
# print("before\n", disp_str)
# disp_str =  "<br>".join(data.loc[data['Indexes'] == True]['COURSE_TITLE'])
# disp_str =  str(data.loc[data['Indexes'] == True]['COURSE_TITLE'])

# disp_str = "".join(re.split("   ", disp_str))
# print("after split \n", disp_str)
if courses_titles is not None:
	# disp_str = re.split("Name", disp_str, flags=re.IGNORECASE)[0]
	disp_str = "<br>".join(courses_titles)
else:
	disp_str = "No results found for your search interest. Check spelling or try another broader search keyword"
print(disp_str)