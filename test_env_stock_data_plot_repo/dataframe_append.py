import os
import pandas as pd
from general_functions import convert_list_elements_to_date_instance

fileA = os.getcwd() + "\\a.csv"
fileC = os.getcwd() + "\\b.csv"

output = os.getcwd() + "\\aa.csv"

df_csvA = pd.read_csv(fileA, sep=';')
df_csvC = pd.read_csv(fileC, sep=';')

# if element is later then in the base array add to array
# get values of column 1
a_column_dates = df_csvA.iloc[:, 0]
c_column_dates = df_csvC.iloc[:, 0]

# convert to dates
datesA = convert_list_elements_to_date_instance(a_column_dates)
datesC = convert_list_elements_to_date_instance(c_column_dates)

# sort base array A
datesA.sort()

# get the latest date
latest_dateA = datesA[len(datesA) - 1]

# iterate over every element and find out if there is new data
for dateC in datesC:
    if dateC > latest_dateA:
        print(f"{dateC} is older then {latest_dateA}")

        # convert to string
        dateC = dateC.strftime("%Y-%m-%d")
        # access row data
        row = df_csvC.loc[df_csvC['index'] == dateC]

        # append row to base row
        concat = pd.concat([row,df_csvA], ignore_index=True)

        concat.to_csv(output, sep=';')


''' 
# check if quarterly dates are equal
if df_csvA['index'].equals(df_csvC["index"]):
    # access first value in column named 'index'
    print(df_csvA['index'][0])
    print("same")

    for counter, column in enumerate(df_csvC):
        values = df_csvC.iloc[:, counter]
        df_csvA[column] = values
        counter += 1
    df_csvA.to_csv(output, sep=';')

'''