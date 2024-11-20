import pandas as pd

data={
    'Name':['Oleksandr','Olga','Oleksandr','Denis','Anna'],
    'School_Number':['One','One','Two','Three','One'],
    'Class':[10,9,11,11,10]
}

df=pd.DataFrame(data)
print(df)
aggregated_df=df.groupby('School_Number')['Class'].mean()
print("\nАгрегація та угрупування:")
print(aggregated_df)