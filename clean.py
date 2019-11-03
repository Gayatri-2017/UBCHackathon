import pandas as pd
# Import the data
df = pd.read_csv("/Users/apple/Desktop/UBCHackathon/ubc_course_calendar_data_copy.csv")
#print(df.head(5))
#print(df['INSTRUCTORS'].head(20))

#df = pd.DataFrame({
#   'EmployeeId': ['001', '002', '003', '004', '005'],
#    'Age': [21, 23, 43, 52, 12],
#   'City': ['Mumbai|Bangalore', 'Pune|Mumbai|Delhi', 'Mumbai|Bangalore', 'Mumbai|Pune', 'Bangalore'] 
#})

# Step 1
# We start with creating a new dataframe from the series with EmployeeId as the index
#new_df = pd.DataFrame(df.City.str.split('|').tolist(), index=df.EmployeeId).stack()

new_df = pd.DataFrame(df['INSTRUCTORS'].str.split(';').tolist(), index=df["ID"]).stack()

# Step 2
# We now want to get rid of the secondary index
# To do this, we will make EmployeeId as a column (it can't be an index since the values will be duplicate)
#new_df = new_df.reset_index([0, 'EmployeeId'])

# Step 3
# The final step is to set the column names as we want them
#new_df.columns = ['EmployeeId', 'Age', 'City']