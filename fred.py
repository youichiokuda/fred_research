import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2020, 12, 30)

df = web.DataReader(["DEXJPUS"], "fred", start, end)
df.plot()

plt.xlabel("Date")
plt.ylabel("Yen / Doller")
plt.savefig("JPNUSD.jpg")

df2 = web.DataReader(["NIKKEI225", "DJIA",'SP500'], "fred", start, end)

df2.plot()


plt.xlabel("Date")
plt.ylabel("NIKKEI225/DJIA")
plt.savefig("NIKKEI225-DJIA.jpg")


df3= web.DataReader(["SP500"], "fred", start, end)
df3.plot()

#アメリカの失業率
df4= web.DataReader(["UNRATE"], "fred", start, end)
df4.plot()

#アメリカのGDP
df5= web.DataReader(["A191RL1Q225SBEA"], "fred", start, end)
df5.plot()

#日本の銀行の資産
df6= web.DataReader(["JPNASSETS"], "fred", start, end)
df6.plot()

#ロンドンの金取引
df7= web.DataReader(["GOLDPMGBD228NLBM"], "fred", start, end)
df7.plot()
