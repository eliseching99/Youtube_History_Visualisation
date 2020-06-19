import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import json
from pandas.io.json import json_normalize
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator



st.title('Youtube Data Visualisation')
st.subheader("Seach History Analysis:Word Cloud")
'''
Hypothesis: BTS would definitely be one of my most searched words\n 
Results: Following my hypothesis, 'BTS' did come out to be one of my most searched key words
         As a dancer, it also proves that the words "choreo" and "mirror" came out to be in my top 2 search words as well

'''
df= pd.read_json('history/search-history.json')
search_df = pd.read_json('history/search-history.json')
search_df['time']=pd.to_datetime(search_df['time'])
search_df['title']=search_df['title'].str.replace('Searched for ', '')
search_df['Year'],search_df['Month']=search_df['time'].dt.year,search_df['time'].dt.month_name()
search_df['Day']=search_df['time'].dt.day
search_df['Day_of_week']=search_df['time'].dt.day_name()
wordcloud2 = WordCloud(background_color="white").generate(' '.join(search_df['title']))
print(wordcloud2)
plt.imshow(wordcloud2, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()


#print(search_df['Year'],search_df['Month'])
#print(search_df['Day'])
print(search_df.head())
search_df=search_df.drop(columns=['details','products','titleUrl'])

#keywords to look for in search title 
search_df['title']=search_df['title'].str.lower()
#st.write(search_df)

Year_freq=search_df['Year'].value_counts()
#print(Year_freq)

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
st.write(Year_freq)

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

st.title("Watch History")
watch_hist= pd.read_json('history/watch-history.json')
watch_hist['title']=watch_hist['title'].str.replace('Watched ', '')

watch_hist=watch_hist.drop(columns=['products','description','details','header','titleUrl'])

subtitles=watch_hist.subtitles
# st.write(subtitles)


def flatten_json(nested_json, exclude=['']):
    """Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
            exclude: Keys to exclude from output.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name='', exclude=exclude):
        if type(x) is dict:
            for a in x:
                if a not in exclude: flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out
test=pd.DataFrame([flatten_json(x) for x in watch_hist['subtitles']])
# print(test)
name=test['0_name']
watch_hist = watch_hist.join(name)
watch_hist=watch_hist.rename(columns = {'0_name':'channel_name'})
watch_hist=watch_hist.drop(columns=['subtitles'])



watch_hist['time']=pd.to_datetime(watch_hist['time'])
watch_hist['Year'],watch_hist['Month']=watch_hist['time'].dt.year,watch_hist['time'].dt.month_name()
watch_hist['Day']=watch_hist['time'].dt.day
watch_hist['Day_of_week']=watch_hist['time'].dt.day_name()

#print(watch_hist['Year'])
st.subheader("Watch Frequency per annum")
st.write(watch_hist['Year'].value_counts())
year_2019=watch_hist.loc[watch_hist['Year'] == 2019]

st.subheader("Monthly Watch Frequency in 2019")
'''
Conclusions: 
It seems that June and July are where my watch frequencies seemed to spike. This could be due to my mid sem break falling around
those months. I find it quite strange that my watch frequency from december to january was not really high as it seems that
this was during the time of my internship. Therefore, I wasn't able to watch Youtube as often during these months. 
'''
st.write(year_2019['Month'].value_counts())
monthly_freq=year_2019['Month'].value_counts()
# monthly_freq = monthly_freq.sort_values(by="Month")
colors=['#00876c'
,'#439981'
,'#6aaa96'
,'#8cbcac'
,'#aecdc2'
,'#cfdfd9'
,'#f1f1f1'
,'#f1d4d4'
,'#f0b8b8'
,'#ec9c9d'
,'#e67f83'
,'#de6069'
,'#d43d51']


print(monthly_freq,"2019 yall")
print(type(monthly_freq))


new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

monthly_freq = monthly_freq.reindex(new_order, axis=0)
print(monthly_freq)
ax = monthly_freq.plot(kind='bar',
                                    figsize=(14,8),
                                    title="Monthly Frequency in 2019",color=colors)
ax.set_xlabel("Months")
ax.set_ylabel("Frequency watch times")
st.pyplot()

#for year of 2019, get monthly frequency

#for year of 2019, which day of the week i watch the most
new_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

daily_freq=year_2019['Day_of_week'].value_counts()
daily_freq = daily_freq.reindex(new_order, axis=0)
colors=['#F7D9C4','#FAEDCB','#C9E4DE','#C6DEF1','#DBCDF0','#F2C6DE','#F9C6C9']
ax = daily_freq.plot(kind='bar',
                                    figsize=(14,8),
                                    title="Daily Frequency in 2019",color=colors)
ax.set_xlabel("Days of the Week")
ax.set_ylabel("Daily Frequency")
st.subheader('Days of the Week')
st.pyplot()

#CHANNELS get top 10 most watched of all time
st.write(watch_hist['channel_name'].value_counts())


st.subheader('Top 10 Channels I watch in All Time')
'''
My hypothesis would be that BTS would be on my most watched channel. However it seems that a bigger KPOP channel "Mnet Kpop" which is the distributor of multiple kpop artists music is my number 1 most watched channel. Interestingly enough, I knew that Pewdiepie
would be on my top 10 list as well as I watch him on a daily basis. As always fitness channels were also in my top 10 list.
'''
n = 10
st.write(watch_hist['channel_name'].value_counts()[:n])
mostwatched=watch_hist['channel_name'].value_counts()[:n]
colors=['#F7D9C4','#FAEDCB','#C9E4DE','#C6DEF1','#DBCDF0','#F2C6DE','#F9C6C9']
ax = mostwatched.plot(kind='bar',
                                    figsize=(14,8),
                                    title="Top 10 channels I watch",color=colors)
ax.set_xlabel("Channels")
ax.set_ylabel("Frequency")
st.pyplot()






# for i in subtitles:
#     #print(i)
#     print(i)
#     if i:
#         print(i[0]['name'])
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





