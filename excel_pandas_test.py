import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file_1 = 'shift-data.xlsx'
excel_file_2 = 'third-shift-data.xlsx'

df_first_shift = pd.read_excel(excel_file_1, sheet_name='first')
df_second_shift = pd.read_excel(excel_file_1, sheet_name='second')
df_third_shift = pd.read_excel(excel_file_2)

# print particular spreadsheet..
print(df_first_shift)

# get a specific column form spreadsheet..
print(df_first_shift['Product'])

# Combining all data among spreadsheet...
df_all = pd.concat([df_first_shift, df_second_shift, df_third_shift])
print(df_all)

# Calculations.. for productivity..
pivot = df_all.groupby(['Shift']).mean()
shift_productivity = pivot.loc[:, "Production Run Time (Min)": "Products Produced (Units)"]
print(shift_productivity)

# Graph for the productivity..
#shift_productivity.plot(kind='bar')
#plt.show()

# if you want all the information in one file.
df_all.to_excel("result.xlsx")





