import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

df = pd.read_csv('Microsoft_Stock.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 1. Побудова графіків зміни ціни на час відкриття біржі

# а) Загальний графік
df['Open'].plot(label='Загальний графік')
plt.legend()
plt.show()

# б) Графік за 2020 рік
df_2020 = df.loc['2020']
df_2020['Open'].plot(label='Графік за 2020 рік')
plt.legend()
plt.show()

# в) Графік за лютий 2021 року
df_feb_2021 = df.loc['2021-02']
df_feb_2021['Open'].plot(label='Графік за лютий 2021 року')
plt.legend()
plt.show()

# г) Графік за травень 2017 – червень 2019
df_may_2017_jun_2019 = df.loc['2017-05':'2019-06']
df_may_2017_jun_2019['Open'].plot(label='Графік за травень 2017 – червень 2019')
plt.legend()
plt.show()

# д) Графік за 2019 та 2020 на одному графіку
plt.figure(figsize=(10, 6))

plt.plot(df.loc['2019']['Open'], label='2019', linestyle='-')
plt.plot(df.loc['2020']['Open'], label='2020', linestyle='-')

plt.title('Зміна ціни на час відкриття біржі в 2019 та 2020 роках')
plt.xlabel('Дата')
plt.ylabel('Ціна при відкритті')
plt.legend()
plt.show()

# 2. Знаходження середніх значень найменшої ціни за день

# а) За 2019 рік
mean_open_2019 = df.loc['2019']['Low'].mean()
print(f'Середнє значення найменшої ціни за день за 2019 рік: {mean_open_2019}')

# б) За кожний місяць
mean_open_by_month = df.asfreq('M')['Low'].mean()
print(f'Середнє значення найменшої ціни за день за кожен місяць: {mean_open_by_month}')

# в) За кожні два тижні літа та осені 2020 року
mean_open_summer_fall_2020 = df.loc['2020-06':'2020-09'].resample('2W')['Low'].mean()
print(
    f'Середнє значення найменшої ціни за день за кожні два тижні літа та осені 2020 року: {mean_open_summer_fall_2020}')

# г) Зміни найменшої ціни за день у відсотках за кожен день впродовж осені 2018 року
pct_change_fall_2018 = df.loc['2018-09':'2018-12']['Low'].pct_change()
print(f'Зміни найменшої ціни за день у відсотках за кожен день впродовж осені 2018 року: {pct_change_fall_2018}')

# д) Графічно ковзне середнє найменшої ціни за день за 2018 рік з вікном в місяць
rolling_mean_2018 = df.loc['2018']['Low'].rolling(window='30D').mean()
rolling_mean_2018.plot(label='Ковзне середнє за 2018 рік')
plt.legend()
plt.show()
