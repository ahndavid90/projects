import pandas as pd
import os

file1 = os.path.join(os.getcwd(), 'US 2019 Population by States.xlsx')
file2 = os.path.join(os.getcwd(), 'COVID19_Stats.xlsx')

#df1 = pd.DataFrame({'Name': ['Andy', 'Jess', 'Ben'], 'Number': [100,200,300]}, index=[1,2,3])


df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

dataframes = [df1, df2]
df_new1 = pd.concat(dataframes)
df_new2 = pd.concat(dataframes, axis=1)

#print(df_new1)
#print(df_new2)

df_new = pd.merge(df1, df2, on = 'State')

df_new['COVID19_Rate'] = df_new['COVID19_Cases']/df_new['Population']
df_new.sort_values(by = 'COVID19_Rate', ascending = False, inplace = True)


print(df_new)
number_rows = len(df_new.index)
number_columns = len(df_new.columns)

print(number_rows)
print(number_columns)