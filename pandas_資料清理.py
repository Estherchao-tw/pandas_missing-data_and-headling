import pandas as pd 


#西元年轉為民國年
def convert_chinese_year(year):
    return int(year)-1911
 
 
df = pd.read_csv('mycsvfile.csv', converters={
    'date_added': lambda x: pd.to_datetime(x,errors='coerce'),  #「新增日期」轉為日期型態
    'rating': lambda x:int(round(float(x), 0))  #「評價」欄位四捨五入且轉為整數型態
})
 
print(df)