import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pymsteams

df = pd.read_csv('response.csv')

df['responseCode'] = df['responseCode'].astype(str)

# Cleaning the data
df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='ms')
df['timeStamp'] = df['timeStamp'].dt.strftime('%m-%d %H:%M:%S')

# remove columns with nan value
df = df.dropna(axis=1, thresh=len(df) - 1)

for x in range(len(df['responseCode'])):
    if not df['responseCode'][x].isnumeric():
        df = df.drop(index=x)

df['responseCode'] = df['responseCode'].astype(int)



def __organize_colors() -> list:
    colors = []
    for x in df['responseCode'].value_counts().index.values:
        if x == 200:
            colors.append('green')
        elif x == 404 or x == 403:
            colors.append('yellow')
        elif x == 500:
            colors.append('red')
    return colors

#plt.subplots(figsize=(17, 6), nrows=2, ncols=1, sharex=True, sharey=True)

# ========================================================= plot 1:
'''plt.subplot(1, 2, 1)
#plt.plot()
plt.xticks()
plt.yticks(df['responseCode'].unique())
plt.title('Requisições por data e períodos')
plt.plot(df['timeStamp'], df['responseCode'], label='Response Code',
         linewidth=2, ls='dashed', marker='o', ms=5)
plt.grid(True)
plt.legend(loc='best')
plt.title('Timeline Requests')

# ========================================================= plot 2:
plt.subplot(1, 2, 2)
# plt.plot()
plt.pie(df['responseCode'].value_counts().values, labels=df['responseCode'].value_counts(
).index.values, autopct='%1.1f%%', colors=__organize_colors(), shadow=True, startangle=90)
plt.title('Response Message 02/08/2022')
plt.suptitle(df['URL'][0])

plt.show()'''

print(df.to_string())


# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard("https://ailos.webhook.office.com/webhookb2/4427da1f-69b4-4070-b06e-bfc22b49ba0c@7e15f674-853f-4708-8271-75b08833eb8c/IncomingWebhook/0db913ee7bb147bb8423d501d94fe7c6/4b62fc67-7cbd-42b5-83fc-c1cfb8435b11")

# Add text to the message.
myTeamsMessage.text(df.to_html())

# send the message.
myTeamsMessage.send()