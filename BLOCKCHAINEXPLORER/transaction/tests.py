from django.test import TestCase

import requests
import plotly.express as px

url = "https://api.coingecko.com/api/v3/global"


response = requests.request('GET', url)
json = response.json()
"""df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()"""
percentage = 0
tab = []
for i in json['data']["market_cap_percentage"].values() :
    percentage += i
    tab.append(i)


restant = 1-percentage
tab.append(restant)
df = px.data.tips()
fig = px.pie(df, values=tab, names='day')
fig.show()


