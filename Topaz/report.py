from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('response.csv')

print(df['responseCode'])
print(df['timeStamp'][0])


df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='ms')
df['timeStamp'] = df['timeStamp'].dt.strftime('%m-%d %H:%M:%S')


plt.subplots(figsize=(15, 6), layout='constrained', nrows=2, ncols=1, sharex=True, sharey=True)

#========================================================= plot 1:
plt.subplot(1, 2, 1)
plt.yticks(df['responseCode'].values)
plt.plot(df['timeStamp'], df['responseCode'], 'o-', label='Response Code')
plt.legend(loc='best')

#========================================================= plot 2:
response_code_200_count = (df['responseCode'] == 200).sum()
response_code_403_count = (df['responseCode'] == 403).sum()
response_code_500_count = (df['responseCode'] == 500).sum()

plt.subplot(1, 2, 2)
plt.bar(['Ok'], [response_code_200_count], label='Ok', color='green')
plt.bar(['Forbidden'], [response_code_403_count], label='Forbidden', color='orange')
plt.bar(['Internal Server Error'], [response_code_500_count], label='Internal Server Error', color='red')
plt.legend(loc='best')

plt.show()
