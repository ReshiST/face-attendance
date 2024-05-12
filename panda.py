import pandas as pd
data= pd.read_csv("Attendance.csv")
df=pd.DataFrame(data)
print(df.groupby(['Name']))