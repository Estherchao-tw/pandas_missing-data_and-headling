import pandas as pd
import csv

df = pd.read_csv('mycsvfile.csv')
print(df)

# Pandas遺漏資料清理
## 遺漏資料泛指該筆資料含有空值、NULL或NaN等缺漏
df.dropna(inplace=True)
print(df)
##dropna(how="all")該筆資料的所有欄位皆遺漏才刪除。
#新增空資料
null0 = ['','','','','','','','','','','','']
with open('mycsvfile.csv','a+',encoding='utf-8-sig') as file:
    writer=csv.writer(file)
    writer.writerow(null0)
    
# file.close()
#刪除空資料
df.dropna(how='all',inplace=True)
print(df)
  
# Dropping the type with NULL and 0
df = df[df["type"].str.contains("NULL|0") == False]
print(df)

# ## keep unknown value and replace other value
df.fillna(value='unknown',inplace=True)
# Pandas重複資料清理
df.drop_duplicates(['type','country'],inplace=True)
print(df.head(5))
print(df)
print(df.info())



# Pandas拆分欄位資料
#  #str()：截取欄位資料的部分字串，範例截取描述(decription)欄位的前30個字，當作摘要(summary)新欄位的值。
df['summary'] = df.description.str[0:30]

#   #以逗號區分，取資料
df['list'] = df.listed_in.str.split(',')
df['list1'] = df.list.str.get(0)
df['list2'] = df.list.str.get(1)
df0 = df[['list','list1','list2']]

print(df0)


df1 = df[['date_added']]

df['date_added'] = pd.to_datetime(df.date_added,format= '%Y%m%d',errors='coerce')
#Passing errors='coerce' will force an out-of-bounds date to NaT, in addition to forcing non-dates (or non-parseable dates) to NaT.
print (df1)
print(df.dtypes)

# # round(decimals=小數位數)：四捨五入到自訂的小數位數。
df['rating'] = df['rating'].round(decimals=0)
df2 = df[['rating'] ]
# print(df2)


#apply()自訂函數
#將release_year 轉換成民國
def convert_chinese_year(year):
    return int(year)-1911

df['release_year'] = df['release_year'].apply(convert_chinese_year)
df3 = df['release_year']
print(df3)

#Ｌambda 在千分位的地方加上逗號
df['show_id'] = df['show_id'].apply(lambda x:format(x,','))
df4 = df['show_id']
# print(df4)


