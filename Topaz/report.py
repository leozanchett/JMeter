from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('response.csv')

print(df['responseCode'])
print(df['timeStamp'][0])


df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='ms')
df['timeStamp'] = df['timeStamp'].dt.strftime('%m-%d %H:%M:%S')


# fig, ax = plt.subplots(figsize=(10, 6.7), layout='constrained', constrained_layout=True, dpi=100)
# plt.plot(df['timeStamp'], df['responseCode'], 'o-', label='Response Code', linewidth=2, markersize=10, alpha=0.8, markeredgewidth=0.5)
# plt.plot([1,2,3], [4,5,6])
# plt.xlabel('Horário da requisição')
# plt.ylabel('Código de resposta')
# plt.title('Comportamento do servidor')
# plt.yticks([200, 403, 500])
# # set xticks only for visible data
# plt.xticks(df['timeStamp'], df['timeStamp'])
# plt.margins(0.2)
# plt.subplots_adjust(bottom=0.15)
# plt.legend(loc='best')


#plot 1:
plt.subplots(figsize=(15, 6), layout='constrained')
plt.subplot(1, 2, 1)
plt.plot(df['timeStamp'], df['responseCode'], 'o-', label='Response Code')
plt.legend(loc='best')

#plot 2:
x = df['responseCode'] == 200
# count the number of occurrences of true in x
print(x.value_counts()[True])
lista_total_response_codes = []
total_code_200 = 0;
for i in range(len(df['responseCode'])):
   print(df['responseCode'][i])
   if df['responseCode'][i] == 200:
      total_code_200 += 1

lista_total_response_codes.append(df['responseCode'][i])
   

plt.subplot(1, 2, 2)
plt.bar(df['responseMessage'], [3], label='Response Code')

plt.legend(loc='best')
plt.show()
