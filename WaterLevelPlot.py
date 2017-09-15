import requests
import matplotlib.pyplot as plt
import numpy as np
import json

url = requests.get('https://data.qld.gov.au/api/action/datastore_search?resource_id=7afe7233-fae0-4024-bc98-3a72f05675bd')
dataText = url.text
data = json.loads(dataText)

waterLevel = []
dateTime = []

for i in data['result']['records']:
	waterLevel.append(i['Water Level'])
	dateTime.append(i['DateTime'])


np_date = np.array(dateTime, dtype='datetime64')
#np_date = np.array(dateTime)
np_date2 = np_date.astype(object)
np_level = np.array(waterLevel)
title = data['result']['records'][0]['Site']


import matplotlib.dates as mdates


years = mdates.YearLocator()
months = mdates.MonthLocator()
#yearFmt = mdates.DateFormatter('%Y')
dateFmt = mdates.DateFormatter('%H:%M')
my = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')

#fig = pylab.figure()
fig, ax = plt.subplots()
ax.plot(np_date2, np_level)

#ax.xaxis.set_major_locator(years)
#ax.xaxis.set_minor_locator(months)
ax.xaxis.set_major_formatter(dateFmt)

fig.autofmt_xdate()

#plt.plot(np_date, np_level)
plt.xlabel("Date & Time")
plt.ylabel("Water Level")
plt.title("Water Level Indication at "+ title)

plt.show()
