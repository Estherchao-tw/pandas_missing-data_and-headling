import pandas as pd
from ydata_profiling import ProfileReport

#call pandas  read_csv() read csv files
df = pd.read_csv('../mycsvfile.csv')
# print(df)

profile = ProfileReport(df,title='Netflix Profile Report', explorative=True)
print(profile)

profile.to_file('NetflixProfileReport.html')

# Deprecated 'pandas-profiling' package, use 'ydata-profiling' instead
















