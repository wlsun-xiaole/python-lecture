import requests
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date=20210301&stockNo=2330"
resp = requests.get(url)
raw_data = resp.text
clean_data = raw_data.split('\r\n')[1:-6]
clean_data[0] = '"date","deal_amount","deal_price","open_price","highest_price","lowest_price","end_price","diff_pirce","deal_num",'

sum_str = ""
for data in clean_data:
    sum_str += data + '\r\n'

df = pd.read_csv(StringIO(sum_str), index_col=0)
df.to_csv("stock.csv")
df['end_price'].plot()
plt.show()

