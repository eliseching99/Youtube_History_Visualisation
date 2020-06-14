import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import json
from pandas.io.json import json_normalize




st.title('Youtube Data Visualisation')
'''
Search History Analysis
'''
df= pd.read_json('history/search-history.json')
search_df = pd.read_json('history/search-history.json')
search_df['time']=pd.to_datetime(search_df['time'])
search_df['title']=search_df['title'].str.replace('Searched for ', '')


#print(search_df.columns())
#print(cleaned_titles.head())
#print(df.head())
#print(search_df['time'].head())
search_df['Year'],search_df['Month']=search_df['time'].dt.year,search_df['time'].dt.month_name()
search_df['Day']=search_df['time'].dt.day
search_df['Day_of_week']=search_df['time'].dt.day_name()
#print(search_df['Year'],search_df['Month'])
#print(search_df['Day'])
print(search_df.head())
search_df=search_df.drop(columns=['details','products','titleUrl'])

#keywords to look for in search title 
search_df['title']=search_df['title'].str.lower()
#st.write(search_df)

Year_freq=search_df['Year'].value_counts()
#print(Year_freq)
st.write(Year_freq)

fig1, ax1 = plt.subplots()
piechart_labels=[]
year_freq=[]
for index,value in Year_freq.items():
    #print(index)
    piechart_labels.append(index)
    year_freq.append(value)

#print(Year_freq['Year'])
#year_values=Year_freq['Year'].tolist()

# colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
# explode = (0.1, 0, 0, 0)
# ax1.pie(year_freq, explode=explode, labels=piechart_labels, colors=colors, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')
# plt.tight_layout()
# st.pyplot()
st.subheader("Pie Chart of Search History Annually")
# if st.checkbox("Show Pie Charts"):
labels = piechart_labels
sizes = year_freq
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
colors = ['#F0725C','#F6AC5A','#80CEBE','#B9C0EA']

ax1.pie(sizes, explode=explode,colors=colors, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
#ax1.pie(sizes, explode=explode, labels=labels, shadow=True,autopct='', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot()

st.subheader("Watch History")
watch_hist= pd.read_json('history/watch-history.json')
watch_hist['title']=watch_hist['title'].str.replace('Watched ', '')
watch_hist=watch_hist.drop(columns=['products','description','details','header','titleUrl'])

st.write(watch_hist)
subtitles=watch_hist.subtitles
for i in subtitles:
    #print(i)
    print(i)
    if i:
        print(i[0]['name'])
# print(watch_hist['subtitles'][0]['name'])
# with open('history/watch-history.json') as data_file:    
#     data = json.load(data_file)
# watch_hist2=pd.json_normalize(data)
# print(watch_hist2.head)
# st.write(watch_hist2)





#how many times i watch youtube in a year which is my businest month
#watch history json


#how many times i watch youtube in a month?

#how many times i watch youtube in a day?

#which are the hours where i watch youtube the most





